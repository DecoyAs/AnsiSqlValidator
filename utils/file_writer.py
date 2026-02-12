def write_report(filename, report_lines):

    with open(filename, "w", encoding="utf-8") as file:
        for line in report_lines:
            file.write(line + "\n")
