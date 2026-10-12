pref_rating=3
years=2
user_performance_rating=int(input("enter user performance rating:"))
user_experience=int(input("enter user experience:"))
if(user_performance_rating>pref_rating and user_experience>years):
   print("eligible")
else:
    print("not eligible")