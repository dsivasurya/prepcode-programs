low_temp=10
high_temp=40
temp=int(input("enter temperature:"))
if(temp<low_temp and temp>high_temp):
   print("warning")
else:
    print("weather is good")