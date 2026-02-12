from logic.select import select
from logic.alter import alter
from logic.update import update
from logic.delete import delete
from logic.create import create

from engine.tokenizer import tokenize
import engine.constants as const


def router(query, show_output=True):

    const.result_list.clear()

    token = tokenize(query)

    if token == False:
        if show_output:
            count = 0
            for i in const.result_list:
                count += 1
                print(f"ERROR NO. {count} : {i}")
        return False

    if not token:
        return False

    if token[0] == "SELECT":

        val = select(token)

        if val == True:
            if show_output:
                print("SUCCESS")
            return True
        else:
            if show_output:
                print("ERRORS FOUND")
                count = 0
                for i in const.result_list:
                    count += 1
                    print(f"ERROR NO. {count} : {i}")
            return False

    elif token[0] == "CREATE":

        val = create(token)

        if val == True:
            if show_output:
                print("SUCCESS")
            return True
        else:
            if show_output:
                print("ERRORS FOUND")
                count = 0
                for i in const.result_list:
                    count += 1
                    print(f"ERROR NO. {count} : {i}")
            return False

    elif token[0] == "ALTER":

        val = alter(token)

        if val == True:
            if show_output:
                print("SUCCESS")
            return True
        else:
            if show_output:
                print("ERRORS FOUND")
                count = 0
                for i in const.result_list:
                    count += 1
                    print(f"ERROR NO. {count} : {i}")
            return False

    elif token[0] == "UPDATE":

        val = update(token)

        if val == True:
            if show_output:
                print("SUCCESS")
            return True
        else:
            if show_output:
                print("ERRORS FOUND")
                count = 0
                for i in const.result_list:
                    count += 1
                    print(f"ERROR NO. {count} : {i}")
            return False

    elif token[0] == "DELETE":

        val = delete(token)

        if val == True:
            if show_output:
                print("SUCCESS")
            return True
        else:
            if show_output:
                print("ERRORS FOUND")
                count = 0
                for i in const.result_list:
                    count += 1
                    print(f"ERROR NO. {count} : {i}")
            return False

    else:
        if show_output:
            print("INVALID QUERY !!!")
        return False
