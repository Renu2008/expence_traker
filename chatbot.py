import csv
import os

from dotenv import load_dotenv
from groq import Groq


# Load environment variables from .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key or api_key == "YOUR_GROQ_API_KEY_HERE":
    print("Error: Please add your Groq API key to the .env file.")
    exit()


# Create Groq client
client = Groq(api_key=api_key)


def load_expenses():
    expenses = []

    with open("data/expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append(row)

    return expenses


# Load private expense data
expenses = load_expenses()


# Convert expense data into text
expense_data = ""

for expense in expenses:
    expense_data += (
        f"Date: {expense['date']}, "
        f"Category: {expense['category']}, "
        f"Description: {expense['description']}, "
        f"Amount: ₹{expense['amount']}\n"
    )


# Get question from user
question = input("Ask a question about your expenses: ")


# Create prompt
prompt = f"""
You are a personal expense chatbot.

Below is private expense data:

{expense_data}

Answer the user's question using only the provided expense data.

User question:
{question}

Give a simple and clear answer.
"""


# Send request to LLM
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)


# Display answer
print("\nChatbot Answer:")
print(response.choices[0].message.content)