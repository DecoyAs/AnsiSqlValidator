def show_file_format_help():

    print("\n========== INPUT FILE FORMAT HELP ==========\n")

    print("Your SQL input file must follow these rules:\n")

    print("DO's ✅")
    print("1. Each query must end with a semicolon ';'")
    print("   Example: SELECT * FROM users;")

    print("2. Write one query per line (recommended)")
    print("   Example:")
    print("   SELECT * FROM users;")
    print("   DELETE FROM users WHERE id = 5;")

    print("3. Use only supported ANSI keywords in CAPITAL form")
    print("   Example: ALTER TABLE, CREATE TABLE")

    print("\nDON'Ts ❌")
    print("1. Do not forget semicolon ';' at the end")
    print("   Wrong: SELECT * FROM users")

    print("2. Do not write unsupported queries like INSERT")
    print("   Wrong: INSERT INTO users VALUES (1);")

    print("3. Do not write multiple queries in one line without semicolon")
    print("   Wrong: SELECT * FROM users DELETE FROM users;")

    print("\nExample File: queries.sql\n")
    print("SELECT * FROM users;")
    print("ALTER TABLE users ADD age INT;")
    print("DELETE FROM users WHERE id = 5;")

    print("\n============================================\n")


def show_supported_queries():

    print("\n========== SUPPORTED SQL QUERIES ==========\n")

    print("This validator currently supports the following ANSI SQL queries:\n")

    print("1. SELECT Query")
    print("   Syntax:")
    print("   SELECT * FROM table;")
    print("   SELECT col1, col2 FROM table WHERE col = value;")

    print("\n2. CREATE TABLE Query")
    print("   Syntax:")
    print("   CREATE TABLE table_name (")
    print("       col1 INT,")
    print("       col2 VARCHAR,")
    print("       col3 INT PRIMARY KEY")
    print("   );")

    print("\n3. ALTER TABLE Query")
    print("   Supported Operations:")
    print("   ALTER TABLE table_name ADD col datatype;")
    print("   ALTER TABLE table_name DROP COLUMN col;")
    print("   ALTER TABLE table_name ALTER COLUMN col SET DATA TYPE datatype;")
    print("   ALTER TABLE table_name RENAME COLUMN old TO new;")

    print("\n4. UPDATE Query")
    print("   Syntax:")
    print("   UPDATE table_name SET col = value;")
    print("   UPDATE table_name SET col = value WHERE col2 = value2;")

    print("\n5. DELETE Query")
    print("   Syntax:")
    print("   DELETE FROM table_name;")
    print("   DELETE FROM table_name WHERE col = value;")

    print("\n==========================================\n")
