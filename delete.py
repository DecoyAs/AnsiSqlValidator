import engine.constants as const


def delete(token):

    const.result_list.clear()

    # ---------------- BASIC LENGTH CHECK ----------------
    if len(token) < 3:
        const.result_list.append(
            "INVALID LENGTH. DELETE must be at least: DELETE FROM table;"
        )
        return False

    # ---------------- DELETE KEYWORD ----------------
    if token[0] != "DELETE":
        const.result_list.append("ERROR AT INDEX 0. QUERY DOES NOT START WITH DELETE.")
        return False

    # ---------------- FROM KEYWORD ----------------
    if token[1] != "FROM":
        const.result_list.append(
            f"ERROR AT INDEX 1. DELETE MUST BE FOLLOWED BY FROM. USED {token[1]}"
        )
        return False

    # ---------------- TABLE NAME ----------------
    if len(token) < 3:
        const.result_list.append("MISSING TABLE NAME AFTER FROM.")
        return False

    table_name = token[2]

    if not const.is_valid_identifier(table_name):
        const.result_list.append(
            f"ERROR AT INDEX 2. INVALID TABLE NAME USED: {table_name}"
        )

    # ---------------- OPTIONAL WHERE CLAUSE ----------------
    if "WHERE" in token:

        where_index = token.index("WHERE")

        # WHERE must come after table name
        if where_index < 3:
            const.result_list.append("WHERE CLAUSE PLACED BEFORE TABLE NAME.")
            return False

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
