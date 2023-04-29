import random

print("Dice Roller Simulator")

x='y'
while x.lower()=='y' or x.lower()=='yes':
    i = random.randint(1,6)
    if i==1:
        print('Its one')
        print("--------")
        print("|      |")
        print("|  0   |")
        print("|      |")
        print("--------")
    elif i==2:
        print('Its two')
        print("--------")
        print("|  0   |")
        print("|      |")
        print("|    0 |")
        print("--------")
    elif i==3:
        print('Its three')
        print("--------")
        print("|  0   |")
        print("|  0   |")
        print("|  0   |")
        print("--------")
    elif i==4:
        print('Its four')
        print("--------")
        print("|0    0|")
        print("|      |")
        print("|0    0|")
        print("--------")
    elif i==5:
        print('Its five')
        print("--------")
        print("|0    0|")
        print("|  0   |")
        print("|0    0|")
        print("--------")
    elif i==6:
        print('Its six')
        print("--------")
        print("|0    0|")
        print("|0    0|")
        print("|0    0|")
        print("--------")

    print('Do you want to continue rolling the dice?')
    x = input()