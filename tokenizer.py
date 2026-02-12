import engine.constants as const

def tokenize(query):

    query = query.upper()

    query = query.replace("(", " ( ")
    query = query.replace(")", " ) ")
    query = query.replace(",", " , ")
    query = query.replace(";", " ")

    token = query.split()
    val = parenthesis_checker(token)

    if val:
        return token
    else:
        return False


def parenthesis_checker(token):

    count = 0
    for tok in token:
        if tok == "(":
            count += 1
        elif tok == ")":
            count -= 1

    if count != 0:
        const.result_list.append("Error !!! : INVALID QUERY, PARENTHESIS CHECKER FAILED")
        return False

    return True
