import random
l=["rock","paper","scissor"]
a=input("press m to start a game")
while(a=="m"):
    x=input("choose r:for rock, p:for paper, s:for scissor")
    x.lower()
    y=random.choice(l)
    print("computer choose",y)
    print("your choice is",x)
    if x=="r":
        if y==l[0]:
            print("its a tie")
        elif y==l[1]:
            print("computer wins")
        elif y==l[2]:
            print("you win")
    elif x=="p":
        if y==l[1]:
            print("its a tie")
        elif y==l[2]:
            print("computer wins")
        elif y==l[0]:
            print("you win")
    elif x=="s":
        if y==l[2]:
            print("its a tie")
        elif y==l[0]:
            print("computer wins")
        elif y==l[1]:
            print("you win")
    else:
        print("please choose")
    z=input("press q to quit and p to play")
    if z=="q":
        print("thank you")
        break
    elif z=="p":
        print("continue the game")
            
    
    
