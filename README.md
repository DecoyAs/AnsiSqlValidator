# AnsiSqlValidator
A simple ansi sql validator for ddl and dll commands made AS A BEGINEER PROJECT in python for learning the basics of python and learning how parsers and validators work. 



## 1. The Global Execution Flow

Before writing any specific query logic, memorize this 4-step sequence:

1. **Clean & Tokenize:** Normalize to uppercase, add spaces around `(`, `)`, and `,`, then `.split()`.
2. **Pre-Validation:** Check for balanced parentheses and empty strings.
3. **Command Routing:** Look at `tokens[0]` to decide which function to call (`SELECT`, `CREATE`, etc.).
4. **Reporting:** Collect errors in a list. If the list is empty, return **PASS**; otherwise, return **FAIL** with the list.

---

## 2. Query Specific Logic (The "Checklist")

### **SELECT (The "Order" Query)**

**Logic:** Must follow the **S-F-W-G-H-O** sequence.

* **Mandatory:** Must have `SELECT` and `FROM`.
* **Order Check:** `FROM` index must be  `SELECT` index. `WHERE` index must be  `FROM` index.
* **Recursive Check:** If you see `(SELECT ...)`, pass that inner string back to your `router`.
* **Example Error:** `SELECT name WHERE id = 1 FROM users;` (WHERE before FROM).

### **CREATE (The "Blueprint" Query)**

**Logic:** `CREATE` + `TABLE` + `Name` + `(Columns)`.

* **Structure:** `tokens[1]` must be `TABLE`.
* **Table Name:** `is_valid_identifier(tokens[2])`.
* **Columns:** Inside the `()`, tokens should ideally follow a triplet: `Name -> Type -> Constraint`.
* **Comma Check:** No comma should exist just before the closing `)`.
* **Example Error:** `CREATE TABLE 123_data (id INT);` (Numeric start).

### **ALTER (The "Modification" Query)**

**Logic:** `ALTER` + `TABLE` + `Name` + `Action`.

* **Structure:** `tokens[1]` must be `TABLE`.
* **Action Check:** `tokens[3]` must be in `['ADD', 'DROP', 'MODIFY', 'RENAME']`.
* **Example Error:** `ALTER TABLE users salary INT;` (Missing the word `ADD` or `MODIFY`).

### **UPDATE (The "Assignment" Query)**

**Logic:** `UPDATE` + `Table` + `SET` + `Assignments`.

* **Structure:** `tokens[2]` must be `SET`.
* **Table Name:** `is_valid_identifier(tokens[1])`.
* **Example Error:** `UPDATE SET users id=1;` (Table name in wrong place).

### **DELETE (The "Removal" Query)**

**Logic:** `DELETE` + `FROM` + `Table`.

* **Mandatory:** ANSI requires the word `FROM`.
* **Table Name:** `tokens[2]` must be a valid identifier.
* **Example Error:** `DELETE users;` (Missing `FROM`).

---

## 3. The "Main Logic" Functions (Your Tools)

| Function Name | Logic |
| --- | --- |
| **`is_valid_identifier(t)`** | Returns `False` if `t` is in `RESERVED_WORDS` or starts with a number. |
| **`check_balance(tokens)`** | Uses a counter (+1 for `(`, -1 for `)`). If final sum != 0, error. |
| **`check_order(tokens, a, b)`** | If both words exist, `tokens.index(a)` must be `< tokens.index(b)`. |

---

## 4. Tomorrow's Implementation Strategy

1. **Define your Constants:** Start by pasting your `ANSI_RESERVED_WORDS`. It shows you know the standard.
2. **Write the Tokenizer:** Keep it simple. Just `replace` and `split`.
3. **The "Guard" Clauses:** At the start of every validator function, check if the query is long enough.
* *Example:* `if len(tokens) < 4: return "Incomplete Query"`


4. **Recursive Subqueries:** If you see a subquery, say: *"I am treating the content inside parentheses as a new query and routing it back to the start."*

### Quick Cheat-Sheet Table

| Keyword | Required Neighbors | Common Error to Print |
| --- | --- | --- |
| **SELECT** | `FROM` | "Missing FROM clause" |
| **INSERT** | `INTO`, `VALUES` | "Missing INTO or VALUES keyword" |
| **CREATE** | `TABLE`, `( )` | "Table name is a reserved keyword" |
| **DROP** | `TABLE` | "Missing TABLE keyword in DROP statement" |

**Would you like me to write a "Mock Test" list of 5 bad SQL queries and the specific error messages your logic should catch for them?**
