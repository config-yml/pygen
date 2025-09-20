import sys
import random

first_arg = sys.argv[1]
#second_arg = sys.argv[2]


list_all_symbols = [0,1,2,3,4,5,6,7,8,9,'~','!','@','#','$','%','^','&','*','(',')','-','+','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l']

print(first_arg)                            #Вывод введённых аргументов для откладки


match first_arg:
    case '-h':
        print("Welcome to pygen 1.0.0!\nUsage: pygen -P")
    case '-p':
        password = []
        for i in range(8):
                symbol_to_append = random.choice(list_all_symbols)
                password.append(symbol_to_append)
        print(*password[ :8 ], sep='')
    case _:
        print('Unknown command :(')