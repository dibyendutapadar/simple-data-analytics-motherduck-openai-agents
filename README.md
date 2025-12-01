## Simple Data Analytics with MotherDuck and OpenAI Agents SDK

This repository contains a minimal end to end example that connects the OpenAI Agents SDK with a MotherDuck database. The goal is to enable natural language questions that are converted into SQL, executed on MotherDuck, and returned as structured results.

The project uses a sample database that is already available in MotherDuck after login. You can also create and load your own database from CSV, Parquet, or any other source supported by DuckDB and MotherDuck.

### Features

- Natural language query to SQL generation using OpenAI Agents SDK
- Secure SQL execution using MotherDuck through DuckDB
- Example Python tool for running SQL inside an agent
- Simple and extensible codebase to connect structured data with agent workflows

---

### Getting Started with MotherDuck

- Sign up or log in at https://motherduck.com
- Install DuckDB CLI if needed
- Create a MotherDuck token from the MotherDuck UI
- Store it securely as an environment variable

### Getting Started with OpenAI Agents SDK

- Obtain an OpenAI API key from https://platform.openai.com
- Install the official Python package:
```python
pip install openai-agents
```

---
### Installation
Clone this repository and install dependencies.

``` python
git clone https://github.com/<your-user>/simple-data-analytics-motherduck-openai-agents.git
cd simple-data-analytics-motherduck-openai-agents

python -m venv env
source env/bin/activate
pip install -r requirements.txt

```

create .env file in the following format
```
OPENAI_API_KEY=""
MOTHER_DUCK_TOKEN=""
```

### How it works

The agent uses a Python function decorated as a tool. This tool connects to MotherDuck through DuckDB and executes SQL queries. When the agent receives a user query, it generates SQL, calls the tool, and returns the result.

### Running the Agent

Change the user_input to your question in the main function

```python
if __name__ == "__main__":
    user_input ="""
        How long do riders wait between request_datetime and pickup_datetime for each hvfhs_license_num?
        """
    asyncio.run(main(user_input))
```

and run from terminal

```
python motherDuck_openai_agentssdk.py
```


#### Custom Databases

The included example uses a sample MotherDuck database that is available after login. You can replace it with your own database using DuckDB or MotherDuck SQL commands: