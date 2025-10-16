# print("hello desktop")
# name = input("Enter your name: ")
# print("Hello,", name)
# calculating
# num1=30
# num2=4
# print(f"{num1%num2} is the remainder")
# using f string
age=20
age_to_str=str(age)
# print("i am "+ age_to_str + "years old")
# print(f"i am {age}")
name="john"
# greeting=print(f"hello {name}")
name="sami"
welcome_template="welcome, {}!"
greet_sami=welcome_template.format(name)
# print(greet_sami)
name="josef"
greet_josef=welcome_template.format(name)
# print(greet_josef)

message="welcome!😊"
# welcome_user=print("{message}")
# userName=input("please enter your name: ")
# userPhone=input("please enter your phone number: ")
# confirm_userInfo=print(f"thank you for giving us the informations your name is {userName} and your phone is {userPhone} 😊")


# magic number game
# magic_number=13

# user_guess=int(input("🎮please enter your guess 😊: "))
# guess=magic_number==user_guess
# print(f"you give a {guess} guess")

# and and or
# user_age=int(input("enter your age: "))
# check_Age=user_age>18 or user_age <65
# print(f" you are in {check_Age} category")

# default_country="ETHIOPIA"
# Entered_country=input("Enter your country:(optional)")
# User_country=Entered_country or default_country
# print(User_country)


broker_service=["Car", "Home" ,"Apartments"]
# append and remove
broker_service.append("machinary")
# print(broker_service)
broker_service.remove("Home")
# print(broker_service)

Foods=[ 
        ["Apple", "🍎"] ,
         ["Banana" ,"🍌"] ,  
         ["Burger" ,"🍔"] ,
         [ "grapes" ,"🍇"]

     ]

accsess_food=Foods[0][0]
Foods.append(["Bread" ,"🍞"])
# print(accsess_food)
# print(Foods)

# Tuples
Departments=("Computer" ,"Marketing" ,"Bussiness")
# print(Departments)
Departments=Departments + ("Nursing",)
# print(Departments)

# Sets
# no order
# no duplicates


Cake_Lover= {"Jhon", "Mateos","peter" ,"Kidi"}
Fruit_Lover= {"Lucy" , "Kidi" ,"Anna"}
Add_element_Cake=Cake_Lover.add("Jorge")
# print(Cake_Lover)
remove_element= Cake_Lover.remove("Mateos")
# print(Cake_Lover)
Lover_Intersect=Cake_Lover.intersection(Fruit_Lover)
# print(Lover_Intersect)
Mixed=Cake_Lover.union(Fruit_Lover)
# print(Mixed)
only_Cake=Cake_Lover.difference(Fruit_Lover)
# print(only_Cake)

only_Fruit=Fruit_Lover.difference(Cake_Lover)
# print(only_Fruit)

not_in__both=Cake_Lover.symmetric_difference(Fruit_Lover)
# print(not_in__both)



#python dictionaries

drink_price={"pepsi 🥤" : "20$", "sprite 🍹" : "15$" ,"cola 🍾" : "21$"}
price=drink_price["Mirinda"]="23$"
# print(drink_price)
# print(price)

Drink_price=(
    
    {"name":"pepsi" ,"price" : 20},
    {"name":"sprite" ,"price" : 15},
    {"name":"cola" ,"price" : 21},
    {"name":"merinda" ,"price" : 23}

)
Drink=Drink_price[0]
show_data=Drink["price"]
# print(f"{show_data}$")

Hot_Drink=[("Tea ☕", 5) , ("Coffee 🍵" , 7) , ("Milk 🥛" , "4")]
hot_price=dict(Hot_Drink)
# print(hot_price)



prices_pen={"Bic" : 25 , "Lexi" : 30 , "Buna" : 35}
add_pen= prices_pen['Nano']=15
price_pen= prices_pen['Bic']
# print(price_pen)
# print(prices_pen)


pen_Data=(
    

{"Name" : "Bic" ,"Price": 25 },
{"Name" : "Lexi" ,"Price": 15 },
{"Name" : "Buna" ,"Price": 30 },
{"Name" : "Nano" ,"Price": 35 }

)

pen=pen_Data[0]
accsess_price=pen["Name"]
# print(accsess_price)


PC_data=[("Hp" , 200),("Dell" , 245),("Mac" , 470)]
dicted_Pc=dict(PC_data)
# print(dicted_Pc)

# length and SUM functions

grades=[60 , 70,80]
length=len(grades)
# print(length)
sumof_Grades=sum(grades)
# print(sumof_Grades)
averageOf_Grades=int(
sumof_Grades/length
)
# print(averageOf_Grades)

# join
course=["python" ,"Java" ,"CPP"]
useJoin=", ".join(course)
# print(f"my favorite languages are {useJoin}.")





# lottery_wining={1, 4, 5}
# user_ticket=set() 
# user_input=input("Enter your lottry numbers: ")
# user_ticket.add(user_input)

# print(user_ticket)

# ...existing code...

lottery_wining = {1, 4, 5}
# user_ticket = set()
user_input = input("Enter your lottery numbers (e.g. 234): ")
user_ticket = {int(digit) for digit in user_input if digit.isdigit()}
intersections=user_ticket.intersection(lottery_wining)
print("Your ticket:", user_ticket)
print(f"Intersection with winning numbers:{intersections}")
print(f"wining numbers {lottery_wining}")
if user_ticket == lottery_wining:
    print("you win the lottery! 🎉🎉😊")