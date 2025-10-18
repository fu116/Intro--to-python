# if else statments
# my_dict =(

#     {"phone" : "Samsung " , "price" : 230},
#     {"phone" : "Iteal " , "price" : 130 },
#     {"phone" : "Nokia " , "price" : 180 }
# )
# phone_name=my_dict[0]
# # print(phone_name["phone"])

# phones_for_sell=["Samsung" , "Iteal", "Nokia"]
# phones_on_discount=["Samsung" ,"Itel"]
# user_choice=input("please enter the phone 📱 you wanted to buy😊:  ")
# if user_choice in phones_for_sell and user_choice in phones_on_discount:
    # print("your choice is on sell and on discount 😉☺️")
# elif user_choice in phones_for_sell:
    # print("this phone is on sell ☺️")
# else:
    # print("we run out of this phone😔")
# # while loop
# user_input= input("do you still want to continue using this app?(yes/no)")
# while user_input == "yes":
#    print("it seems you like this App 😍")
#    user_input= input("do you still want to continue using this app?(yes/no)")

#  for loop #########################################################
List_Phones = [
    {"name" : "Samsung " , "price" : 230},
    {"name" : "Iteal "   , "price" : 130},
    {"name" : "Nokia "   , "price" : 180}
]

# for phone in List_Phones:
#     name_of_phone=phone["name"]
#     price_of_phone=phone["price"]

    # print(f"for this month {name_of_phone} have a price of {price_of_phone}$")

# Cars={"Honda": 2000 , "Tesla" : 3000 , "Mercedes":4500}
# for car in Cars:
    # print(car)

# counters=[0,1,2,3,4,5,6,7,8,9]
# for nums in range(10,20,3):
    # print(nums)
# ////////////////////////////////////////
    # destructuring of lists of tuples
Sweets=[("cake" , 8),("Ice_cream" , 10),("Candy" , 5)]   
dicted_sweets=dict(Sweets)
# print(dicted_sweets)
# disp_sweet=Sweets[0]
# print(disp_sweet)
# for name, price in Sweets:
    # name , price=sweet
    # name=sweet[0]
    # price=sweet[1]
    # print(name)
    # print(f"{name} have price of  {price}$")
# /////////////////////////////////////////////////////////////////
# exercise
# user_choice=input("do u want to coninue to the app ?(press q to continue or p to stop) :" )
# while user_choice !="q":
    # print("the App is still running")
    # if user_choice=="p":
        #  print("Hello")

    # user_choice=input("do u want to coninue to the app ?(press q to continue or p to stop) :" )
# ////////////////////////////////////////////////////////////////
# iterating over dictioneries
Cars={"Honda": 2000 , "Tesla" : 3000 , "Mercedes":4500}
# for name , price in Cars.items():
    #    print(f"{name} have price of  {price}$")
#/////////////////////////////////////////////////////////////

# break and continue
product_status=["ok" , "ok" , "ok" , "faulty", "ok" , "ok"]

# for Status in product_status:
#     if Status=="faulty":
#       print(f"{Status} computer 🖥️ found !")
#       continue
#     print(f"this PC is {Status} 👌🏼") 
#     print(f"shipping🚚 new computer to the customer") 
    

# challange FizzBBUZZ multiples of 3 and 5

# for index in range(1, 100):
    # if index%3==0:     
    #  Fizz=index="Fizz"
    #  print(Fizz)
    #  continue
    # if index%5==0:
    #  Buzz=index="Buzz"
    #  print(Buzz)
    #  continue
    # if index%3==0 and index%5==0 :   
    #  FizzBuzz=index="FizzBuzz"
    #  print(FizzBuzz)
    #  continue
    # print(index)


# for index in range(1, 101):
#     if index%3==0 and index%5==0 :   
#      print(f"FizzBuzz, since {index}  is a multiple of BOTH 3 AND 5")
#      continue
#     if index%5==0:
#      print(f"Buzz, since {index} is a multiple of 5")
#      continue
#     if index%3==0:     
#      print(f"Fizz, since {index} is a multiple of 3")
#      continue
#     print(index)

