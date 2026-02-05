from .constants import ANSI_RESERVED_WORDS, ANSI_DATA_TYPES
import re

# --- Helper Logic ---
def is_valid_identifier(name):
    if not name: return False
    if name.startswith('"') and name.endswith('"'): return True
    pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"
    return bool(re.match(pattern, name)) and name.upper() not in ANSI_RESERVED_WORDS

def check_clause_order(tokens, sequence):
    """Ensures keywords like SELECT, FROM, WHERE appear in order."""
    indices = [tokens.index(s) if s in tokens else None for s in sequence]
    present_indices = [i for i in indices if i is not None]
    return present_indices == sorted(present_indices)

# --- DDL Validators ---

def alter_validator(tokens):
    errors = []
    # ALTER TABLE <name> ADD/DROP/MODIFY <col>
    if len(tokens) < 4 or tokens[1] != "TABLE":
        errors.append("Malformed ALTER statement. Expected: ALTER TABLE <name>...")
    
    if len(tokens) >= 3 and not is_valid_identifier(tokens[2]):
        errors.append(f"Invalid Table Identifier: {tokens[2]}")
        
    actions = {"ADD", "DROP", "MODIFY", "RENAME"}
    if len(tokens) >= 4 and tokens[3] not in actions:
        errors.append(f"Invalid ALTER action: {tokens[3]}. Expected {actions}")
        
    return {"status": "PASS" if not errors else "FAIL", "errors": errors}

# --- DML Validators ---

def select_validator(tokens):
    errors = []
    # Sequence: SELECT -> FROM -> WHERE -> GROUP BY -> ORDER BY
    sequence = ["SELECT", "FROM", "WHERE", "GROUP", "ORDER"]
    if not check_clause_order(tokens, sequence):
        errors.append("Clause Order Violation: Standard is SELECT..FROM..WHERE..GROUP BY..ORDER BY")
    
    if "FROM" not in tokens:
        errors.append("Missing mandatory FROM clause")
        
    # Check for empty SELECT (e.g., "SELECT FROM table")
    if tokens.index("FROM") == 1:
        errors.append("No columns specified after SELECT")

    # Handle Subqueries Recursively
    if "(" in tokens:
        start = tokens.index("(") + 1
        # Find matching end )
        end = len(tokens) - 1 - tokens[::-1].index(")")
        sub_query = " ".join(tokens[start:end])
        if "SELECT" in sub_query.upper():
            from .validators import router # Local import to avoid circularity
            sub_res = router(sub_query)
            if sub_res["status"] == "FAIL":
                errors.extend([f"Subquery Error: {e}" for e in sub_res["errors"]])

    return {"status": "PASS" if not errors else "FAIL", "errors": errors}

def update_validator(tokens):
    errors = []
    # UPDATE <table> SET <col>=<val> WHERE ...
    if len(tokens) < 4 or tokens[2] != "SET":
        errors.append("Malformed UPDATE. Expected: UPDATE <table> SET <column> = <value>")
    
    if not is_valid_identifier(tokens[1]):
        errors.append(f"Invalid Table Name: {tokens[1]}")
        
    return {"status": "PASS" if not errors else "FAIL", "errors": errors}

def delete_validator(tokens):
    errors = []
    # DELETE FROM <table> WHERE ...
    if "FROM" not in tokens or tokens.index("FROM") != 1:
        errors.append("Malformed DELETE. Expected: DELETE FROM <table>")
        
    if len(tokens) > 2 and not is_valid_identifier(tokens[2]):
        errors.append(f"Invalid Table Name: {tokens[2]}")
        
    return {"status": "PASS" if not errors else "FAIL", "errors": errors}

# --- The Router (Main Entry Point) ---
def router(query_string):
    from .tokenizer import tokenizer
    tokens, balance = tokenizer(query_string)
    
    if balance != 0:
        return {"status": "FAIL", "errors": [f"Unbalanced Parentheses: {balance}"]}
    if not tokens:
        return {"status": "FAIL", "errors": ["Empty Query"]}

    cmd = tokens[0].upper()
    if cmd == "SELECT": return select_validator(tokens)
    if cmd == "CREATE": 
        # You can use your existing create logic here, just ensure it returns the dict
        from .validators import create_validator 
        return create_validator(tokens)
    if cmd == "UPDATE": return update_validator(tokens)
    if cmd == "DELETE": return delete_validator(tokens)
    if cmd == "ALTER":  return alter_validator(tokens)
    
    return {"status": "FAIL", "errors": [f"Unknown Command: {cmd}"]}
