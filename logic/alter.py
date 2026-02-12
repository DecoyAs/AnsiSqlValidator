import engine.constants as const

res = ['ADD', 'DROP', 'RENAME', 'ALTER']

def alter(token) :

    const.result_list.clear()

    if len(token) < 4 :
        const.result_list.append("THE LENGTH OF THE QUERY IS LESS THAN 4 WHICH IS INVALID. ALTER TABLE table_name <operation>;")
        return False

    if token[1] != "TABLE" :
        const.result_list.append(f"ERROR AT INDEX 1. ALTER KEYWORD ISNT FOLLOWED BY A TABLE KEYWORD!!!. IT IS FOLLOWED BY {token[1]}")

    valid_identifier = const.is_valid_identifier(token[2])

    if valid_identifier == False :
        const.result_list.append(f"ERROR AT INDEX 2. TABLE NAME IS NOT A VALID IDENTIFIER. USED {token[2]}")

    if token[3] not in res :
        const.result_list.append(f"ERROR AT INDEX 3. INVALID OPERATION USED. USED {token[3]}")


    #FOR ADD CONSTRAINT
    if token[3] == "ADD" :

        if len(token) > 6 :
            const.result_list.append("ERROR!!!. ADD NEEDS COLUMN NAME PLUS DATATYPES.")
        col_name = token[4]
        datatype = token[5]

        if col_name in const.ANSI_RESERVED_WORDS :
            const.result_list.append(f"ERROR AT INDEX 4. COLUMN NAME IS NOT A VALID IDENTIFIER. USED {col_name}")
        if datatype not in const.ANSI_DATA_TYPES :
            const.result_list.append(f"ERROR AT INDEX 5. INAVLID DATA TYPE USED FOR COLUMN DEFINITION. {datatype}")


    #FOR DROP CONSTARINT
    if token[3] == "DROP" :

        if len(token) <5 :
            const.result_list.append("INVALID LENGHT OF QUERY FOR A DROP OPERATIN!!!")
            return False

        if token[4] != "COLUMN" :
            const.result_list.append(f"ERROR AT INDEX 4. DROP TABLE ISNT FOLLOWED BY A COLUMN KEYWORD. IT IS FOLLOWED BY {token[4]}")

        col_name = token[5]

        if col_name in const.ANSI_RESERVED_WORDS :
            const.result_list.append(f"ERROR AT INDEX 5. COLUMN NAME IS NOT A VALID IDENTIFIER. USED {col_name}")


    #FOR ALTER COLUMN
    if token[3] == "ALTER" :

        if len(token) <9 :
            const.result_list.append(f"INVALID LENGHT OF QUERY FOR A (SECOND) ALTER COLUMN OPERATIN!!!. LENGHT IS {len(token)}")
            return False

        if token[4] != "COLUMN":
            const.result_list.append(f"ERROR AT INDEX 4. SECOND ALTER ISNT FOLLOWED BY A COLUMN KEYWORD. IT IS FOLLOWED BY {token[4]}")

        col_name = token[5]
        if col_name in const.ANSI_RESERVED_WORDS :
            const.result_list.append(f"ERROR AT INDEX 5. COLUMN NAME IS NOT A VALID IDENTIFIER. USED {col_name}")

        if token[6] != "SET" or token[7] != "DATA" or token[8] != "TYPE" :
            const.result_list.append(f"ERROR AT INDEX 6. INVALID SYNTAX. NEED 'SET DATA TYPE' KEYWORDS. USED {token[6]} {token[7]} {token[8]}")

        if token[9] not in const.ANSI_DATA_TYPES :
            const.result_list.append(f"ERROR AT INDEX 9. INVALID DATA TYPE USED FOR COLUMN ALTER. USED {token[9]}")


    #FOR RENAME
    if token[3] == "RENAME" :

        if len(token) < 7 :
            const.result_list.append("INVALID LENGTH OF THE QUERY FOR A RENAME OPERATIN!!!.")
            return False

        if token[4] != "COLUMN" :
            const.result_list.append(f"ERROR AT INDEX 4. RENAME KEYWORD SHOULD ALWAYS BE FOLLOWED BY COLUMN KEYWORD. USED {token[4]}")

        if not const.is_valid_identifier(token[5]) :
            const.result_list.append(f"ERROR AT INDEX 5. TABLE NAME IS NOT A VALID IDENTIFIER. USED {token[5]}")

        if token[6] != "TO" :
            const.result_list.append(f"ERROR AT INDEX 6. MISSING TO. USED {token[6]}")

        if not const.is_valid_identifier(token[7]) :
            const.result_list.append(f"ERROR AT INDEX 7. TABLE NAME IS NOT A VALID IDENTIFIER. USED {token[7]}")


    # FINAL VALIDATION RESULT
    if len(const.result_list) == 0:
        return True
    else :
        return False
