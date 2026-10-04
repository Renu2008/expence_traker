import json
import os

from dotenv import load_dotenv
from groq import Groq

from tools import (
    calculate_category_total,
    get_highest_spending_category,
    get_monthly_summary
)


# Load .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key or api_key == "YOUR_GROQ_API_KEY_HERE":
    print("Error: Please add your Groq API key to the .env file.")
    exit()


# Create Groq client
client = Groq(api_key=api_key)


# Define tools for the agent
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_category_total",
            "description": "Calculate total spending for a specific category.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "The expense category"
                    }
                },
                "required": ["category"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_highest_spending_category",
            "description": "Find the category with the highest total spending.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_monthly_summary",
            "description": "Get total spending for every category.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]


# Function that executes the selected tool
def run_tool(function_name, arguments):

    if function_name == "calculate_category_total":

        return calculate_category_total(
            arguments["category"]
        )

    elif function_name == "get_highest_spending_category":

        return get_highest_spending_category()

    elif function_name == "get_monthly_summary":

        return get_monthly_summary()

    else:
        return "Unknown tool"


# Ask user
question = input("Ask the expense agent a question: ")


# Conversation messages
messages = [
    {
        "role": "system",
        "content": """
You are an expense analysis AI agent.

You have access to tools that can analyze private expense data.

Decide which tools are necessary to answer the user's question.

You may call one or more tools.

After receiving the tool results, provide a clear final answer.
"""
    },
    {
        "role": "user",
        "content": question
    }
]


# Agent loop
for step in range(5):

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    assistant_message = response.choices[0].message

    messages.append(assistant_message)

    # If no tool is required, give final answer
    if not assistant_message.tool_calls:

        print("\n================================")
        print("AI AGENT ANSWER")
        print("================================")

        print(assistant_message.content)

        break


    # Execute requested tools
    for tool_call in assistant_message.tool_calls:

        function_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )

        print(
            f"\nAgent selected tool: {function_name}"
        )

        result = run_tool(
            function_name,
            arguments
        )

        # Send tool result back to the LLM
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            }
        )