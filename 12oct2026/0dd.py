number=int(input("enter the number:"))
starting=2
is_odd=True
while(starting<number):
    if(number%starting==0):
        is_odd=False
    starting+=1
print(is_odd)