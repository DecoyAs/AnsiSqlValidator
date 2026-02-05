def tokenizer(query):
    query = query.upper().strip()
    query = query.replace("(", " ( ").replace(")", " ) ").replace(",", " , ")
    tokens = query.split()
    
    # Parentheses check logic
    balance = 0
    for tok in tokens:
        if tok == "(": balance += 1
        elif tok == ")": balance -= 1
        
    return tokens, balance
