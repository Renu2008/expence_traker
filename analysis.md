# Day 1 - Agentic AI Foundations

## Scenario

This project uses a fictional personal expense management scenario.

The private data is stored in:

`data/expenses.csv`

The same expense-analysis problem is implemented using three different
approaches:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

Example user question:

> How much did I spend on food and which category had the highest spending?

---

# 1. Plain Chatbot

The plain chatbot uses an LLM to answer questions about the private
expense data.

The Python program reads the CSV file and sends the expense information
as context to the LLM.

The LLM generates the answer based on that context.

## Data / Private Data Access

The chatbot reads the local `expenses.csv` file.

The data is included in the prompt sent to the LLM.

## Tools / Rules

The plain chatbot does not use external tools.

It mainly depends on the LLM and the information supplied in its
context.

## Request Handling

The user enters a natural-language question.

The application sends the question and expense data to the LLM.

The LLM generates an answer.

## Limitations

The chatbot does not independently select tools.

It does not have an iterative tool-calling loop.

Complex multi-step tasks require additional application logic.

---

# 2. Rule-Based Workflow

The rule-based workflow uses normal Python code.

It does not use an LLM.

The program follows predefined rules to process the expense data.

## Data / Private Data Access

The Python program directly reads the local CSV file.

## Tools / Rules

The workflow contains predefined Python functions.

These functions:

- Load the expense data
- Calculate Food spending
- Calculate totals for categories
- Find the highest spending category

## Request Handling

The workflow follows a predefined sequence.

The calculations are performed using the rules written in Python.

## Limitations

The workflow works well for tasks that have already been defined.

However, it is less flexible when users ask new types of questions.

Additional Python rules may need to be written for new requirements.

---

# 3. AI Agent

The AI agent combines:

**LLM + Tools + Loop**

The LLM receives the user's question and decides which tools are
required.

The tools access and analyze the private expense data.

The results are then returned to the LLM.

The LLM can continue the process and finally generate an answer.

## Data / Private Data Access

The tools directly access the local `expenses.csv` file.

The agent can request specific operations through the available tools.

## Tools

The agent has the following tools:

- `calculate_category_total`
- `get_highest_spending_category`
- `get_monthly_summary`

## Loop

The agent follows an iterative process:

1. Receive the user's question.
2. Analyze the question.
3. Decide whether a tool is required.
4. Call the required tool.
5. Receive the tool result.
6. Continue if another tool is required.
7. Generate the final answer.

## Advantages

The agent can handle more flexible natural-language requests.

It can select different tools depending on the question.

It can perform multiple operations for one request.

## Limitations

The agent is more complex than the chatbot and rule-based workflow.

It requires an LLM API.

Tool definitions and the agent loop need to be designed and tested
carefully.

---

# Comparison

| Criteria | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | Medium | Low | High |
| Decision-making | LLM response generation | Predefined rules | LLM can select tools |
| Tool usage | No tools | Python functions | LLM-selected tools |
| Private-data access | Prompt context | Direct Python access | Tools provide access |
| Multi-step task handling | Limited | Predefined sequence | Iterative tool calls |
| Automation | Basic | High for fixed tasks | High for dynamic tasks |
| Reliability | Depends on LLM response | Predictable for defined rules | Depends on LLM and tools |
| Suitable for | Simple questions | Fixed processes | Flexible multi-step tasks |

---

# Suitability Analysis

## Plain Chatbot

A plain chatbot is suitable for simple conversational questions where
the required information can be provided as context.

It is relatively simple to implement.

Its main limitation is that it does not independently perform structured
tool-based operations.

---

## Rule-Based Workflow

A rule-based workflow is suitable for predictable tasks with clearly
defined steps.

For example, calculating predefined expense totals can be implemented
with normal Python functions.

Its main limitation is flexibility.

New types of questions may require additional rules and code.

---

## AI Agent

An AI agent is suitable for tasks requiring flexible decision-making,
tool usage, and multiple steps.

For example, the expense agent can decide whether it needs a category
calculation, a monthly summary, or the highest-spending-category tool.

This provides more flexible task handling.

The tradeoff is additional complexity and dependence on the LLM.

---

# General Conclusion

The three approaches solve related problems using different designs.

A plain chatbot primarily uses an LLM to understand a question and
generate an answer.

A rule-based workflow uses predefined program logic to perform known
operations.

An AI agent combines an LLM with tools and an iterative loop so that it
can dynamically select actions needed to complete a task.

A chatbot can be used for straightforward conversational tasks.

A rule-based workflow can be used when the process is predictable and
the steps are already known.

An AI agent can be used when a task requires flexible tool usage and
multiple steps.