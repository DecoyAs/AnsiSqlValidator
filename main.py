from engine.validators import router
import engine.constants as const

from utils.file_reader import read_queries_from_file
from utils.file_writer import write_report
from utils.help_menu import show_file_format_help, show_supported_queries


# ===================== BANNER =====================
def banner():
    print(r"""
╔══════════════════════════════════════════════╗
║                                              ║
║        ⚡ SQL VALIDATOR TOOL ⚡                ║
║      ANSI Syntax + Rules Checker (v1.0)      ║
║                                              ║
╚══════════════════════════════════════════════╝
""")


# ===================== PAUSE =====================
def pause():
    input("\n⏎ Press Enter to return to menu... ")


# ===================== MULTIPLE QUERY MODE =====================
def validate_multiple_queries():

    print("\n╭────────────────────────────────────────╮")
    print("│        MULTI QUERY VALIDATION MODE     │")
    print("╰────────────────────────────────────────╯")

    print("\n📌 Paste or type SQL queries below.")
    print("Type DONE on a new line when finished.\n")

    queries = []
    full_input = ""

    # -------- INPUT UNTIL DONE --------
    while True:
        line = input("SQL> ").strip()

        if line.upper() == "DONE":
            break

        if line == "":
            continue

        full_input += line + "\n"

    # -------- SPLIT QUERIES USING ; --------
    parts = full_input.split(";")

    for q in parts:
        q = q.strip()

        if q == "":
            continue

        queries.append(q + ";")

    if len(queries) == 0:
        print("\n⚠ No queries entered!")
        return

    print(f"\n✅ Detected {len(queries)} queries.\n")

    # -------- OUTPUT FILE --------
    out_file = input("Enter output file name (example: report.txt): ").strip("'").strip('"')
    out_file = out_file.replace("\\", "/")

    report = []
    report.append("========== MULTIPLE QUERY REPORT ==========")

    query_no = 0

    # -------- VALIDATION LOOP --------
    for query in queries:
        query_no += 1

        const.result_list.clear()

        status = router(query, show_output=False)

        report.append("-----------------------------------")
        report.append(f"QUERY {query_no}: {query}")

        if status:
            report.append("STATUS: SUCCESS ✅")
        else:
            report.append("STATUS: FAILED ❌")
            report.append("ERRORS:")

            count = 0
            for err in const.result_list:
                count += 1
                report.append(f"  {count}. {err}")

    # -------- SAVE REPORT --------
    write_report(out_file, report)

    print("\n╭────────────────────────────────────────╮")
    print("│        REPORT SAVED SUCCESSFULLY       │")
    print("╰────────────────────────────────────────╯")
    print(f"📄 Location: {out_file}")


# ===================== SINGLE QUERY + SAVE =====================
def validate_single_query_to_file():

    query = input("\n🟢 Enter SQL Query ➜ ").strip()

    if not query.endswith(";"):
        query += ";"

    const.result_list.clear()

    status = router(query)

    out_file = input("\nEnter output file name (example: report.txt): ").strip("'").strip('"')
    out_file = out_file.replace("\\", "/")

    report = []
    report.append("========== SINGLE QUERY REPORT ==========")
    report.append(f"QUERY: {query}")

    if status:
        report.append("STATUS: SUCCESS ✅")
    else:
        report.append("STATUS: FAILED ❌")
        report.append("ERRORS:")

        count = 0
        for err in const.result_list:
            count += 1
            report.append(f"{count}. {err}")

    write_report(out_file, report)

    print("\n╭────────────────────────────────────────╮")
    print("│        REPORT SAVED SUCCESSFULLY       │")
    print("╰────────────────────────────────────────╯")
    print(f"📄 Location: {out_file}")


# ===================== SINGLE QUERY ONLY =====================
def validate_single_query():

    query = input("\n🟢 Enter SQL Query ➜ ").strip()

    if not query.endswith(";"):
        query += ";"

    const.result_list.clear()

    status = router(query)

    if status:
        print("\n✨ Query Status: VALID ✅")
    else:
        print("\n⚠ Query Status: INVALID ❌")


# ===================== FILE VALIDATION =====================
def validate_sql_file():

    filename = input("\nEnter SQL File Name or Full Path: ").strip('"').strip("'")
    filename = filename.replace("\\", "/")

    try:
        queries = read_queries_from_file(filename)
    except FileNotFoundError:
        print("\n❌ ERROR: File not found!")
        return

    report = []
    query_no = 0

    for q in queries:
        query_no += 1
        full_query = q + ";"

        print("\n" + "─" * 45)
        print(f"Validating Query {query_no}:")
        print(full_query)
        print("─" * 45)

        report.append("===================================")
        report.append(f"QUERY {query_no}: {full_query}")

        const.result_list.clear()
        status = router(full_query, show_output=False)

        if status:
            report.append("STATUS: SUCCESS ✅")
        else:
            report.append("STATUS: FAILED ❌")
            report.append("ERRORS:")

            count = 0
            for err in const.result_list:
                count += 1
                report.append(f"  {count}. {err}")

    print("\n✅ FILE VALIDATION COMPLETED")

    save = input("\nDo you want to save report to a file? (yes/no): ")

    if save.lower() == "yes":
        out_file = input("Enter output file name or path: ").strip('"').strip("'")
        out_file = out_file.replace("\\", "/")

        write_report(out_file, report)

        print("\n╭────────────────────────────────────────╮")
        print("│        REPORT SAVED SUCCESSFULLY       │")
        print("╰────────────────────────────────────────╯")
        print(f"📄 Location: {out_file}")


# ===================== MAIN MENU =====================
def menu():

    while True:

        print("\n╭────────────────────────────────────────╮")
        print("│              MAIN MENU                 │")
        print("╰────────────────────────────────────────╯")

        print("  1  Validate Single SQL Query")
        print("  2  Validate SQL Queries from File")
        print("  3  Single Query + Save Report")
        print("  4  Multiple Queries + Save Report")
        print("  5  File Format Help")
        print("  6  Supported Queries")
        print("  7  Exit")

        print("\n──────────────────────────────────────────")

        choice = input("➜ Select Option: ")

        if choice == "1":
            validate_single_query()
            pause()

        elif choice == "2":
            validate_sql_file()
            pause()

        elif choice == "3":
            validate_single_query_to_file()
            pause()

        elif choice == "4":
            validate_multiple_queries()
            pause()

        elif choice == "5":
            show_file_format_help()
            pause()

        elif choice == "6":
            show_supported_queries()
            pause()

        elif choice == "7":
            print("\nExiting SQL Validator... Goodbye 👋")
            break

        else:
            print("\n⚠ Invalid choice! Please try again.")
            pause()


# ===================== RUN PROGRAM =====================
banner()
menu()
