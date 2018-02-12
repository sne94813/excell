import random
r=random.randint(1,6)
print(r)
count=int(input("enter the values of the dice"))
count=0
count=count+r
if(count==100):
    print("winner")
else:
    print("contiue playing")
if(count==8):
    count=37
    print("go up  to 37")
else:
    print("contiue playing")
if(count==13):
    count=34
    print("go up  to 34")
else:
    print("contiue playing")
if(count==40):
    count=68
    print("go up  to 68")
else:
    print("contiue playing")
if(count==52):
    count=81
    print("go up to 81")
else:
    print("contiue playing")
if(count==11):
    count=2
    print("oops snake bite go to 2")
else:
    print("contiue playing")
if(count==25):
    count=4
    print("oops snake bite go to 4")
else:
    print("contiue playing")
if(count==38):
    count=9
    print("oops snake bite go go to 9")
else:
    print("contiue playing")
if(count==65):
    count=46
    print("oops snake bite go to 46")
else:
    print("contiue playing ")
if(count==89):
    count=70
    print("oops snake bite go to 70")
if(count==93):
    count=64
    print("oops snake bite go to 64")
else:
    print("contiue playing")
