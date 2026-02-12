import engine.constants as const


def update(token):

    const.result_list.clear()

    # ---------------- BASIC LENGTH CHECK ----------------
    if len(token) < 6:
        const.result_list.append(
            "INVALID LENGTH. UPDATE must be at least: UPDATE table SET col = value;"
        )
        return False

    # ---------------- UPDATE KEYWORD ----------------
    if token[0] != "UPDATE":
        const.result_list.append("ERROR AT INDEX 0. QUERY DOES NOT START WITH UPDATE.")
        return False

    # ---------------- TABLE NAME ----------------
    table_name = token[1]

    if not const.is_valid_identifier(table_name):
        const.result_list.append(
            f"ERROR AT INDEX 1. INVALID TABLE NAME USED: {table_name}"
        )

    # ---------------- SET KEYWORD ----------------
    if token[2] != "SET":
        const.result_list.append(
            f"ERROR AT INDEX 2. UPDATE MUST CONTAIN SET KEYWORD. USED {token[2]}"
        )
        return False

    # ---------------- SET CLAUSE VALIDATION ----------------
    # Example: SET col = value , col2 = value2
    i = 3

    if i >= len(token):
        const.result_list.append("MISSING COLUMN ASSIGNMENT AFTER SET.")
        return False

    while i < len(token):

        # Stop if WHERE begins
        if token[i] == "WHERE":
            break

        col_name = token[i]

        # Skip commas
        if col_name == ",":
            i += 1
            continue

        # Must have "=" after column name
        if i + 1 >= len(token):
            const.result_list.append(
                f"ERROR. COLUMN {col_name} HAS NO '=' ASSIGNMENT."
            )
            break

        if token[i + 1] != "=":
            const.result_list.append(
                f"ERROR. MISSING '=' AFTER COLUMN {col_name}. USED {token[i+1]}"
            )
            break

        # Must have value after "="
        if i + 2 >= len(token):
            const.result_list.append(
                f"ERROR. COLUMN {col_name} HAS NO VALUE AFTER '='."
            )
            break

        value = token[i + 2]

        # Column name validation
        if col_name in const.ANSI_RESERVED_WORDS:
            const.result_list.append(
                f"INVALID COLUMN NAME IN SET CLAUSE. RESERVED WORD USED: {col_name}"
            )

        if not const.is_valid_identifier(col_name):
            const.result_list.append(
                f"INVALID COLUMN IDENTIFIER USED IN SET CLAUSE: {col_name}"
            )

        # Value check (basic)
        if value in const.ANSI_RESERVED_WORDS:
            const.result_list.append(
                f"INVALID VALUE IN SET CLAUSE. RESERVED WORD USED: {value}"
            )

        # Move forward by 3 tokens: col = value
        i += 3

    # ---------------- OPTIONAL WHERE CLAUSE ----------------
    if "WHERE" in token:

        where_index = token.index("WHERE")

        # Must have condition after WHERE
        if where_index + 3 >= len(token):
            const.result_list.append(
                "INVALID WHERE CLAUSE. FORMAT: WHERE column operator value"
            )
            return False

        where_col = token[where_index + 1]
        operator = token[where_index + 2]
        where_value = token[where_index + 3]

        # Column validation
        if where_col in const.ANSI_RESERVED_WORDS:
            const.result_list.append(
                f"INVALID WHERE COLUMN NAME. RESERVED WORD USED: {where_col}"
            )

        if not const.is_valid_identifier(where_col):
            const.result_list.append(
                f"INVALID WHERE COLUMN IDENTIFIER USED: {where_col}"
            )

        # Operator validation
        valid_ops = ["=", ">", "<", ">=", "<=", "<>", "!="]

        if operator not in valid_ops:
            const.result_list.append(
                f"INVALID OPERATOR USED IN WHERE CLAUSE: {operator}"
            )

        # Value validation (basic)
        if where_value in const.ANSI_RESERVED_WORDS:
            const.result_list.append(
                f"INVALID VALUE IN WHERE CLAUSE. RESERVED WORD USED: {where_value}"
            )

    # ---------------- FINAL RESULT ----------------
    if len(const.result_list) == 0:
        return True
    else:
        return False
