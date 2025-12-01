import duckdb
import json
import asyncio
from dotenv import load_dotenv
import os

import asyncio
from rich import print

load_dotenv() 

token = os.getenv("MOTHER_DUCK_TOKEN")

baseInstructions = """

# Base Instructions

1. You have to query data only from the table sample_data.nyc.rideshare

## OUTPUT FORMAT
### <a suitable Header>
```sql
<sql query executed>
```
#### Data Table
<the extracted Data Table from the sql in Markdown format, only if the number of rows are less than 10, else skip
#### Summary
<a summarized answer related to the user question>

"""

def execute_sql(query: str) -> str:
    """Execute SQL query against MotherDuck"""
    conn = duckdb.connect(f"md:?motherduck_token={token}", read_only=True)
    try:
        result = conn.execute(query).fetchdf()
        return result.to_string()
    except Exception as e:
        return f"Error: {str(e)}"
    
import duckdb
from agents import Agent, Runner, function_tool

conn = duckdb.connect('md:?motherduck_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRpYnllbmR1dGFwYWRhckBnbWFpbC5jb20iLCJtZFJlZ2lvbiI6ImF3cy11cy1lYXN0LTEiLCJzZXNzaW9uIjoiZGlieWVuZHV0YXBhZGFyLmdtYWlsLmNvbSIsInBhdCI6ImRKbnRKRlYtQXlmZHRrMVBMZ2p3bl8xaVhkdDk1YUtHWV92dHZCSnNZU2siLCJ1c2VySWQiOiIzYTYzY2U5OS0wOGFiLTRjY2QtOGI3ZC0yOWY5NDQ3MGVmMzUiLCJpc3MiOiJtZF9wYXQiLCJyZWFkT25seSI6ZmFsc2UsInRva2VuVHlwZSI6InJlYWRfd3JpdGUiLCJpYXQiOjE3NjQ0ODQxMzJ9.wka70v5eVdRMSuBjT3S7jSKZiXh3I0GxaO1aqztWUlc', read_only=True)

@function_tool
def query_motherduck(sql: str) -> str:
    """Execute SQL query against MotherDuck database.
    
    Args:
        sql: The SQL query to execute against the MotherDuck database.
    """
    try:
        result = conn.execute(sql).fetchdf()
        return result.to_string()
    except Exception as e:
        return f"Error executing query: {str(e)}"
    

with open('query_guide.md', 'r') as f:
    query_guide = f.read()
    
with open('ride_share_schema.md', 'r') as f:
    ride_share_schema = f.read()
    
agent = Agent(
    name="MotherDuck Analytics Agent",
    instructions=f"""You are a data analyst helping users query a table in MotherDuck database. 
            Use the query_motherduck tool to execute SQL queries against the database table.
            You will be provided base instructions containing general rules, an overview of the schema, and query_guide on sql queries for Motherduck DB.


            {baseInstructions}

            {ride_share_schema}

            {query_guide}
            """,
    tools=[query_motherduck]
)


async def main(user_input):
    result = await Runner.run(
        starting_agent=agent,
        input=user_input
    )
    print(result.final_output)


if __name__ == "__main__":
    user_input ="""
        How long do riders wait between request_datetime and pickup_datetime for each hvfhs_license_num?
        """
    asyncio.run(main(user_input))