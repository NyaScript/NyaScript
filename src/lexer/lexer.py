from lexer.token import Token

def determine_token(token: str):
    return "test"

def main(program: str) -> list:
    tokenized_program = []
    program.split("\n")

    for line_number, line in enumerate(program):
        saved_colnum = 0
        for col_number, char in enumerate(line):
            if char == ' ':
                tokenized_program.append(Token(determine_token(line[saved_colnum:col_number]), line[saved_colnum:col_number], (line_number, col_number)))
                saved_colnum = col_number
        tokenized_program.append(Token(determine_token(line[saved_colnum:col_number]), line[saved_colnum:col_number], (line_number, col_number)
                    ))
        # TODO: fix this
    
    for i in tokenized_program:
        print(i.value)