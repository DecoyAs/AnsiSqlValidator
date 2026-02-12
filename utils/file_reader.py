def read_queries_from_file(filename):

    with open(filename, "r") as file:
        content = file.read()

    queries = content.split(";")
    queries = [q.strip() for q in queries if q.strip() != ""]

    return queries
