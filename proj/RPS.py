import random
import string

a = 'ROCK = r\n','PAPER = p\n', 'SCISSOR = s'
# rock = 'r'
# paper = 'p'
# scissor = 's'
print(*a, sep = '\n')
print('\n')

ranges = list(map(chr, range(97, 112)))
ranges1 = list(map(chr, range(113, 114)))
ranges2 = list(map(chr, range(116, 123)))
list1 = ranges, ranges1, ranges2

rounds = eval(input('Play Rounds: '))

cw = count_wins = 0
cl = count_losses = 0
ct = count_ties = 0



for i in range(rounds):   
      
    user_select = input('Enter a your R-P-S: ')

    act_possi = ["r", "p", "s"]
    comp_act = random.choice(act_possi)

    b = (f"\nYou choose {user_select}, computer choose {comp_act}.")
    print(b)
    print('\n')
    
    if user_select == list1:
        print('Please Enter The Correct R-P-S Again!')

    if user_select == comp_act:
        # print(f"Both players selected {user_select}. It's a tie!\n")
        ct += 1        
        
    elif user_select == "r":        
        if comp_act == "s":
            # print("Rock smashes scissors! You win!\n")
            cw += 1           
        else:
            # print("Paper covers rock! You lose.\n")
            cl += 1            
    elif user_select == "p":       
        if comp_act == "r":
            # print("Paper covers rock! You win!\n")
            cw += 1            
        else:
            # print("Scissors cuts paper! You lose.\n")
            cl += 1           
    elif user_select == "s":        
        if comp_act == "p":
            # print("Scissors cuts paper! You win!\n")
            cw += 1           
        else:
            # print("Rock smashes scissors! You lose.\n")
            cl += 1   

if cw >= cl or ct:
    print('It is a TIE')
elif cl <= cw or ct:
    print('You Loose')
else:
    print('You are the WINNER')                         

    
        
     

print(cw)
print(ct)
print(cl)