import engine.constants as const

def select(token):

    const.result_list.clear()

    # ---------------- BASIC LENGTH CHECK ----------------
    if len(token) < 4:
        const.result_list.append(
            "INVALID LENGTH. SELECT query must be at least: SELECT * FROM table;"
        )
        return False

    # ---------------- SELECT KEYWORD ----------------
    if token[0] != "SELECT":
        const.result_list.append("ERROR AT INDEX 0. QUERY DOES NOT START WITH SELECT.")
        return False

    # ---------------- DISTINCT OPTIONAL ----------------
    start_index = 1
    if token[1] == "DISTINCT":
        start_index = 2

        if len(token) < 5:
            const.result_list.append(
                "INVALID LENGTH. SELECT DISTINCT needs column list and FROM clause."
            )
            return False

    # ---------------- FROM MUST EXIST ----------------
    if "FROM" not in token:
        const.result_list.append("MISSING FROM KEYWORD IN SELECT QUERY.")
        return False

    from_index = token.index("FROM")

    # ---------------- COLUMN LIST VALIDATION ----------------
    if from_index <= start_index:
        const.result_list.append("NO COLUMNS PROVIDED AFTER SELECT.")
        return False

    columns = token[start_index:from_index]

    # Case: SELECT * FROM table
    if len(columns) == 1 and columns[0] == "*":
        pass

    else:
        # Validate column names separated by commas
        for col in columns:

            if col == ",":
                continue

            # AS keyword allowed
            if col == "AS":
                continue

            # Reserved words not allowed as column names
            if col in const.ANSI_RESERVED_WORDS:
                const.result_list.append(
                    f"INVALID COLUMN NAME. RESERVED WORD USED: {col}"
                )

            # Identifier check
            if col not in ["AS"] and col != ",":
                if not const.is_valid_identifier(col):
                    const.result_list.append(
                        f"INVALID COLUMN IDENTIFIER USED: {col}"
                    )

    # ---------------- TABLE NAME VALIDATION ----------------
    if from_index + 1 >= len(token):
        const.result_list.append("MISSING TABLE NAME AFTER FROM.")
        return False

    table_name = token[from_index + 1]

    if not const.is_valid_identifier(table_name):
        const.result_list.append(f"INVALID TABLE NAME USED: {table_name}")

    # ---------------- OPTIONAL WHERE CLAUSE ----------------
    if "WHERE" in token:

        where_index = token.index("WHERE")

        # WHERE must come after FROM table
        if where_index < from_index:
            const.result_list.append("WHERE CLAUSE PLACED BEFORE FROM.")
            return False

        # Must have condition after WHERE
        if where_index + 3 >= len(token):
            const.result_list.append(
                "INVALID WHERE CLAUSE. FORMAT: WHERE column operator value"
            )
            return False

        where_col = token[where_index + 1]
        operator = token[where_index + 2]
        value = token[where_index + 3]

        # Column name check
        if where_col in const.ANSI_RESERVED_WORDS:
            const.result_list.append(
                f"INVALID WHERE COLUMN NAME. RESERVED WORD USED: {where_col}"
            )

        if not const.is_valid_identifier(where_col):
            const.result_list.append(
                f"INVALID WHERE COLUMN IDENTIFIER USED: {where_col}"
            )

        # Operator check
        valid_ops = ["=", ">", "<", ">=", "<=", "<>", "!="]

        if operator not in valid_ops:
            const.result_list.append(
                f"INVALID OPERATOR IN WHERE CLAUSE. USED {operator}"
            )

        # Value check (basic)
        if value in const.ANSI_RESERVED_WORDS:
            const.result_list.append(
                f"INVALID VALUE IN WHERE CLAUSE. RESERVED WORD USED: {value}"
            )

    # ---------------- FINAL RESULT ----------------
    if len(const.result_list) == 0:
        return True
    else:
        return False
