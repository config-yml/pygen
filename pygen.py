import argparse
import random


parser = argparse.ArgumentParser(description='Password generator software(pygen 1.0.1)', usage='pygen [password] [-d <difficulty level>] [-c <count>]\nusage: pygen [wordlist]')

parser.add_argument('mode',type=str,help='for generate password(s): password / for generate wordlist: wordlist')
parser.add_argument('-l','--length',type=int,help='If difficulty custom type the count of symbols')
parser.add_argument('-c','--count',type=int,help='count of passwords')
parser.add_argument('-d','--difficulty',type=str,help='easy/medium/hard/custom')
args = parser.parse_args()
lenght = 10

if args.length:                                             # Блок кода для определения необязательных аргументов
    lenght = args.length                                    
else:
     lenght = 10

if args.difficulty:
    difficulty = args.difficulty
else:
    difficulty = 'medium'

if args.count:
    count = args.count
else:
    count = 1                                               # А также их приравнивание к необходимым переменным

list_all_symbols = [0,1,2,3,4,5,6,7,8,9,'[',']','{','}',';',':','"',"'",'<','>','?','/','|','~','!','@','#','$','%','^','&','*','(',')','-','+','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


match args.mode:
    case 'password':
        if difficulty == 'hard':
            for i in range(count):
                password = []
                for i in range(12):
                    symbol_to_append = random.choice(list_all_symbols)
                    password.append(symbol_to_append)
                print(*password[ :12 ], sep='')


        if difficulty == 'medium':
                for i in range(count):
                    password = []
                    for i in range(8):
                        symbol_to_append = random.choice(list_all_symbols)
                        password.append(symbol_to_append)
                    print(*password[ :8 ], sep='')


        if difficulty == 'easy':
                for i in range(count):
                    password = []
                    for i in range(5):
                        symbol_to_append = random.choice(list_all_symbols)
                        password.append(symbol_to_append)
                    print(*password[ :5 ], sep='')


        if difficulty == 'custom':
                for i in range(count):
                    password = []
                    for i in range(lenght):   
                        symbol_to_append = random.choice(list_all_symbols)
                        password.append(symbol_to_append)
                    print(*password[ :lenght ], sep='')      
                        
    case 'wordlist':
        print('making function...')

    
    case _:
        print('Unknown command :(')
