# ✅ ANSI SQL Query Validator (Mini Project)

## 📌 Project Overview

This project is a **menu-driven ANSI SQL Query Validator** built using
**Python**.
It validates basic SQL queries by checking their syntax and structure
according to ANSI SQL rules.

The validator supports both:

-   **Single query validation (CLI input)**
-   **Multiple query validation (SQL/Text file input)**

It also provides detailed error messages for invalid queries.

------------------------------------------------------------------------

## 🎯 Objectives

-   Validate SQL queries without using any database engine
-   Implement syntax checking using token-based parsing
-   Provide clear error reporting for invalid SQL queries
-   Support file-based validation and report generation
-   Build a simple CLI menu-driven application

------------------------------------------------------------------------

## ✅ Supported SQL Queries

This validator currently supports the following query types:

### 1. SELECT


SELECT * FROM table;
SELECT col1, col2 FROM table WHERE col = value;


### 2. CREATE TABLE


CREATE TABLE table_name (
    col1 INT,
    col2 VARCHAR,
    col3 INT PRIMARY KEY
);


### 3. ALTER TABLE

Supported operations:


ALTER TABLE table_name ADD col datatype;
ALTER TABLE table_name DROP COLUMN col;
ALTER TABLE table_name RENAME COLUMN old TO new;
ALTER TABLE table_name ALTER COLUMN col SET DATA TYPE datatype;


### 4. UPDATE

UPDATE table_name SET col = value;
UPDATE table_name SET col = value WHERE col2 = value2;

### 5. DELETE

DELETE FROM table_name;
DELETE FROM table_name WHERE col = value;

------------------------------------------------------------------------

## ⚙️ Features Implemented

-   Token-based SQL parsing
-   Reserved keyword validation
-   Identifier validation (table names, column names)
-   Datatype validation
-   Detailed error reporting using `result_list`
-   File input support (`.sql` / `.txt`)
-   Report generation in output text file
-   Help menu showing Do's and Don'ts
-   Supported query syntax display

------------------------------------------------------------------------

## 📂 Project Structure

    SQLPARSER/
    |
    |-- main.py                # Menu-driven CLI program
    |-- validator.py           # Router / Query dispatcher
    |-- tokenizer.py           # Tokenizer + parenthesis checker
    |-- constants.py           # Reserved words, datatypes, error list
    |
    |-- logic/
    |   |-- select.py          # SELECT query validator
    |   |-- create.py          # CREATE TABLE validator
    |   |-- alter.py           # ALTER TABLE validator
    |   |-- update.py          # UPDATE validator
    |   |-- delete.py          # DELETE validator
    |
    |-- utils/
        |-- file_reader.py     # Reads SQL queries from file
        |-- file_writer.py     # Writes validation report to file
        |-- help_menu.py       # Help + Supported query display
------------------------------------------------------------------------

## ▶️ How to Run the Project

### Step 1: Run the program

python main.py

### Step 2: Menu Options

    1. Validate Single SQL Query
    2. Validate SQL Queries from File
    3. Validate Single Query + Save Report
    4. Validate Multiple Queries + Save Report
    5. File Format Help
    6. Show Supported SQL Queries
    7. Exit

------------------------------------------------------------------------

## 📄 Input File Format Rules

When validating from a file:

✅ Each query must end with a semicolon `;`\
✅ One query per line is recommended\
✅ Only supported query types should be used

Example file (`queries.sql`):

------------------------------------------------------------------------

## 📝 Output Report

The program can generate a report file containing:

-   Query number
-   Query text
-   SUCCESS / FAILED status
-   List of errors (if any)

Example:

    QUERY 3: ALTER TABLE users ADD age WRONGTYPE;
    STATUS: FAILED
    ERRORS:
    1. INVALID DATA TYPE USED FOR COLUMN DEFINITION. WRONGTYPE

------------------------------------------------------------------------

## 🧪 Testing

The project has been tested using:

-   Valid and invalid queries for each supported type
-   File-based validation with mixed queries
-   Report generation and Unicode-safe output writing

------------------------------------------------------------------------

## 🚀 Conclusion

This project demonstrates the implementation of a simple SQL syntax
validator using Python.
It provides a structured approach to parsing, validating, and reporting
errors for ANSI SQL queries in a menu-driven CLI environment.

------------------------------------------------------------------------

## 👤 Developer

**RAVENCLAW GROUP 2**
ANSI SQL Validator using Python
