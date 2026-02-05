Project Name: Simple SQL ANSI Validator

1\. What is this project?

This project is a Python tool that checks if a SQL query is written correctly. It follows the ANSI standard. The goal is to find mistakes in the query and tell the user exactly what went wrong and how many errors there are.

2\. What queries will it check?

We are focusing on two main types of SQL:

 	A. DDL (Structure)

        **CREATE TABLE**: Checks if the table name is okay, if parentheses are used, and if column types (like INT or VARCHAR) are valid.

        **ALTER TABLE**: Checks if you are adding or dropping columns correctly.

        **DROP TABLE**: Makes sure you didn't forget the table name.

        B. DML (Data)

        **SELECT**: This is the most important. It checks the order of words: SELECT first, then FROM, then WHERE.

        **Subqueries**: It can check a query inside another query (nested queries) by using the same rules again.

        **UPDATE/DELETE**: Checks for the SET and WHERE clauses so you don't accidentally change or delete everything.



3\. How will it work? (The Steps)

Input: The user gives a SQL query as a string.

Cleaning: We make everything uppercase and add spaces around commas and brackets to make it easy to read.

Tokenizing: We split the string into a list of words (tokens).

Checking Rules:

Balanced Brackets: Every ( must have a ).

Reserved Words: You cannot name your table SELECT or FROM.

Order: You cannot put WHERE before FROM.

Output: If it's good, it says "Valid." If it's bad, it prints "Error," tells you why, and shows the total error count.



5\. Current system architecture diagram 



User Query → Tokenizer → Router → Validator → Output Errors

&nbsp;                    ↘ Subquery Extractor ↗





5\. Input and Output Format

Input: A string like "CREATE TABLE users (id INT)".

Output: If the input is valid , that is not incorrect syntactically, then the output will say 'Valid' else, Invalid.

 	Also, an error message will be displayed.

Error Message: e.g., "Error: Missing comma after column name."

Error Count: The total number of mistakes found.





The system is designed with a modular architecture that validates core ANSI SQL syntax rules and can be extended in the future to support additional grammar constructs and more advanced query structures.

