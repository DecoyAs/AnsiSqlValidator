import engine.constants as const


def create(token):

    const.result_list.clear()

    # ---------------- BASIC LENGTH CHECK ----------------
    if len(token) < 6:
        const.result_list.append(
            "INVALID LENGTH. CREATE TABLE must be at least: CREATE TABLE name (col datatype);"
        )
        return False

    # ---------------- CREATE KEYWORD ----------------
    if token[0] != "CREATE":
        const.result_list.append("ERROR AT INDEX 0. QUERY DOES NOT START WITH CREATE.")
        return False

    # ---------------- TABLE KEYWORD ----------------
    if token[1] != "TABLE":
        const.result_list.append(
            f"ERROR AT INDEX 1. CREATE MUST BE FOLLOWED BY TABLE. USED {token[1]}"
        )
        return False

    # ---------------- TABLE NAME ----------------
    table_name = token[2]

    if not const.is_valid_identifier(table_name):
        const.result_list.append(
            f"ERROR AT INDEX 2. INVALID TABLE NAME IDENTIFIER USED: {table_name}"
        )

    # ---------------- PARENTHESIS CHECK ----------------
    if "(" not in token:
        const.result_list.append("MISSING '(' FOR COLUMN DEFINITIONS.")
        return False

    if ")" not in token:
        const.result_list.append("MISSING ')' FOR COLUMN DEFINITIONS.")
        return False

    open_index = token.index("(")
    close_index = token.index(")")

    if close_index < open_index:
        const.result_list.append("INVALID SYNTAX. ')' COMES BEFORE '('.")
        return False

    # ---------------- COLUMN DEFINITIONS ----------------
    column_tokens = token[open_index + 1:close_index]

    if len(column_tokens) == 0:
        const.result_list.append("NO COLUMNS PROVIDED INSIDE CREATE TABLE.")
        return False

    # Columns should come in pairs: name datatype
    i = 0
    while i < len(column_tokens):

        col_name = column_tokens[i]

        # Skip commas
        if col_name == ",":
            i += 1
            continue

        # Must have datatype after column name
        if i + 1 >= len(column_tokens):
            const.result_list.append(
                f"ERROR. COLUMN {col_name} HAS NO DATATYPE."
            )
            break

        datatype = column_tokens[i + 1]

        # ---------------- COLUMN NAME CHECK ----------------
        if col_name in const.ANSI_RESERVED_WORDS:
            const.result_list.append(
                f"INVALID COLUMN NAME. RESERVED WORD USED: {col_name}"
            )

        if not const.is_valid_identifier(col_name):
            const.result_list.append(
                f"INVALID COLUMN IDENTIFIER USED: {col_name}"
            )

        # ---------------- DATATYPE CHECK ----------------
        if datatype not in const.ANSI_DATA_TYPES:
            const.result_list.append(
                f"INVALID DATATYPE USED FOR COLUMN {col_name}. USED {datatype}"
            )

        # ---------------- OPTIONAL CONSTRAINTS ----------------
        # Example: id INT PRIMARY KEY
        if i + 2 < len(column_tokens):

            next_tok = column_tokens[i + 2]

            if next_tok == "PRIMARY":
                if i + 3 < len(column_tokens) and column_tokens[i + 3] == "KEY":
                    i += 2  # skip PRIMARY KEY tokens
                else:
                    const.result_list.append(
                        f"INVALID PRIMARY KEY SYNTAX AFTER COLUMN {col_name}"
                    )

            elif next_tok == "NOT":
                if i + 3 < len(column_tokens) and column_tokens[i + 3] == "NULL":
                    i += 2  # skip NOT NULL tokens
                else:
                    const.result_list.append(
                        f"INVALID NOT NULL SYNTAX AFTER COLUMN {col_name}"
                    )

            elif next_tok == "UNIQUE":
                i += 1  # skip UNIQUE

        # Move forward (col + datatype)
        i += 2

    # ---------------- FINAL RESULT ----------------
    if len(const.result_list) == 0:
        return True
    else:
        return False
