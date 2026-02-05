import os
from datetime import datetime

def get_queries(path):
    if os.path.isdir(path):
        queries = []
        for f in os.listdir(path):
            if f.endswith(".sql"):
                with open(os.path.join(path, f), 'r') as file:
                    queries.append((f, file.read()))
        return queries
    elif os.path.isfile(path):
        with open(path, 'r') as file:
            return [(path, file.read())]
    return [("Manual Input", path)]

def save_report(results, output_dir="outputs"):
    if not os.path.exists(output_dir): os.makedirs(output_dir)
    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(os.path.join(output_dir, filename), "w") as f:
        for res in results:
            line = f"Source: {res['source']} | Status: {res['status']} | Errors: {res['errors']}\n"
            f.write(line)
    return filename
