# DuckDB SQL Query Syntax and Performance Guide 

## General Knowledge

### Basic Syntax and Features

**Identifiers and Literals:**
- Use double quotes (`"`) for identifiers with spaces/special characters or case-sensitivity
- Use single quotes (`'`) for string literals

**Flexible Query Structure:**
- Queries can start with `FROM`: `FROM my_table WHERE condition;` (equivalent to `SELECT * FROM my_table WHERE condition;`)
- `SELECT` without `FROM` for expressions: `SELECT 1 + 1 AS result;`
- Support for `CREATE TABLE AS` (CTAS): `CREATE TABLE new_table AS SELECT * FROM old_table;`

**Advanced Column Selection:**
- Exclude columns: `SELECT * EXCLUDE (sensitive_data) FROM users;`
- Replace columns: `SELECT * REPLACE (UPPER(name) AS name) FROM users;`
- Pattern matching: `SELECT COLUMNS('sales_.*') FROM sales_data;`
- Transform multiple columns: `SELECT AVG(COLUMNS('sales_.*')) FROM sales_data;`

**Grouping and Ordering Shortcuts:**
- Group by all non-aggregated columns: `SELECT category, SUM(sales) FROM sales_data GROUP BY ALL;`
- Order by all columns: `SELECT * FROM my_table ORDER BY ALL;`

**Complex Data Types:**
- Lists: `SELECT [1, 2, 3] AS my_list;`
- Structs: `SELECT {'a': 1, 'b': 'text'} AS my_struct;`
- Maps: `SELECT MAP([1,2],['one','two']) AS my_map;`
- Access struct fields: `struct_col.field_name` or `struct_col['field_name']`
- Access map values: `map_col[key]`

**Date/Time Operations:**
- String to timestamp: `strptime('2023-07-23', '%Y-%m-%d')::TIMESTAMP`
- Format timestamp: `strftime(NOW(), '%Y-%m-%d')`
- Extract parts: `EXTRACT(YEAR FROM DATE '2023-07-23')`

### Database and Table Qualification

**Fully Qualified Names:**
- Tables are accessed by fully qualified names: `database_name.schema_name.table_name`
- There is always one current database: `SELECT current_database();`
- Tables from the current database don't need database qualification: `schema_name.table_name`
- Tables in the main schema don't need schema qualification: `table_name`
- Shorthand: `my_database.my_table` is equivalent to `my_database.main.my_table`

**Switching Databases:**
- Use `USE my_other_db;` to switch current database
- After switching, tables in that database can be accessed without qualification

### Schema Exploration

**Get database and table information:**
- List all databases: `SELECT alias as database_name, type FROM MD_ALL_DATABASES();`
- List tables in database: `SELECT database_name, schema_name, table_name, comment FROM duckdb_tables() WHERE database_name = 'your_database';`
- List views in database: `SELECT database_name, schema_name, view_name, comment, sql FROM duckdb_views() WHERE database_name = 'your_database';`
- Get column information: `SELECT column_name, data_type, comment, is_nullable FROM duckdb_columns() WHERE database_name = 'your_database' AND table_name = 'your_table';`

**Sample data exploration:**
- Quick preview: `SELECT * FROM table_name LIMIT 5;`
- Column statistics: `SUMMARIZE table_name;`
- Describe table: `DESCRIBE table_name;`

### Performance Tips

**QUALIFY Clause for Window Functions:**
-- Get top 2 products by sales in each category
SELECT category, product_name, sales_amount
FROM products
QUALIFY ROW_NUMBER() OVER (PARTITION BY category ORDER BY sales_amount DESC) <= 2;

**Efficient Patterns:**
- Use `arg_max()` and `arg_min()` for "most recent" queries
- Filter early to reduce data volume
- Use CTEs for complex queries
- Prefer `GROUP BY ALL` for readability
- Use `QUALIFY` instead of subqueries for window function filtering

**Avoid These Patterns:**
- Functions on the left side of WHERE clauses (prevents pushdown)
- Unnecessary ORDER BY on intermediate results
- Cross products and cartesian joins