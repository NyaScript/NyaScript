from lexer import lexer

lexer('owo stay name = (nya? "What\'s your name?")\nmeow "Hello"..name.."!"')
# program:
"""
owo stay name = (nya? "What's your name?")          name = input("What's your name?")
meow "Hello "..name.."!"                            print(f'Hello {name}!')
"""
