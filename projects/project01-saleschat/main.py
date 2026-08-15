# this is DEV 108 Programming Project 1: Fake "Sales ChatBot"
# [07/23/2026]
# [Reecha Bharali]

#Greeting 
print("""
                      Hi there!
                🤖🤖🤖I'm Sprouty 🤖🤖🤖

      your friendly plant-loving assistant from 
                  🌱🌱🌱 PlantPal 🌱🌱🌱.
I'm more helpful than a 🌵 cactus 🌵 and less needy than a 🌿 fern 🌿! :)
""")
print()

#Product Prompt
ans=input("🤖🤖🤖 Sprouty 🤖🤖🤖 can help you learn about the 🌱🌱🌱 PlantPal 🌱🌱🌱 product? Do you want to know more Type Y/N : ")
if ans.lower()=="y":
    print("Sure 🌞🌞🌞!!")
 #Sales Pitch 
    print( """
                     🌱🌱🌱 PlantPal 🌱🌱🌱 is the self-watering Smart💧💧Planter
           for people who love plants but keep accidentally sending them to 'Plant Heaven!!' 
    
    It monitors:
          => soil moisture
          => waters your plant exactly when need
          => and even glows softly to remind you it exists.
    
    It is perfect for:
          • busy students 👨‍🎓👨‍🎓👨‍🎓
          • forgetful humans 👤👤👤
          • anyone who's ever whispered 'I'm sorry' to a dead succulent 🌵🌵🌵! 

          """)

#Product Specifications for Sales
    ans1=input("🤖🤖🤖 Sprouty 🤖🤖🤖 can tell how about 🌱🌱🌱 PlantPal 🌱🌱🌱 works. Should I tell you more. Type Y/N : ")
    if ans1.lower()=="y":
        print ("""
               🌱🌱🌱 PlantPal 🌱🌱🌱 featiures
              ✔  Self-watering 2 weeks per refill" 
            ✔ Soil moisture sensor — no more guessing
           ✔ Soft glow reminder light
               
         🤖🤖🤖 Sprouty 🤖🤖🤖 thinks of its huge benefits: 
               💚 Your plants survive 💚 
              💚  You look responsible   💚 
            💚 Everybody in this world wins 💚 
               """)
        print()

#Purchase Offer
        ans2=input("Would you want to go use Smart Planter @29.99. I can place an order for you Y/N : ")
        if ans2.lower()=="y":
            print("All right let me place an order for you. Let's get started with some information to place the order.")
            print()
            od_1=input("Please enter your first name: ")
            od_2=input("Please enter your last name: ")
            od_3=input("Please enter your email address: ")
            od_4=input("Please enter your phone number: ")
            od_5=int(input("Please enter the quantity:"))
            total_price = (od_5*29.99)
            tax=float(.10 * total_price,2)
            total_price_tax= (total_price + tax)
            print("Thank you for your order. Your total is: $",  total_price_tax) 
            print("\n =================" \

#Receipt Formatting
            "\n PLANTPAL RECEIPT" \
            "\n=================")
            print()
            print("Customer:", od_1, od_2)
            print("Email:", od_3)
            print("Phone:", od_4)
            print("==================")
            print("Item: Plant Planter")
            print("Quantity", od_5)
            print("Price: @$29.99 each")
            print("Tax: ", tax)
            print()
            print("================")
            print("Total Price: ", total_price_tax)
            print("\n Thanks for shopping with Sprouty!\
                \n Your plants thank you too 🌿")
            print()
            print("Your PlantPals are on the way! May your thumbs be forever green. 🌱 Goodbye!")

        elif ans2.lower()=="n":
            print("Okay, Thanks for your inquiry and chatting with 🤖🤖🤖 Sprouty 🤖🤖🤖.Come back anytime — I'll be here, photosynthesizing. 🌞 Bye! ") 


 # User declines to know more about Self Planter       
    elif ans1.lower()=="n":
        print("ok let's try something else")
    
#End of Greeting    
elif ans.lower()=="n":
    print("Okay, Thanks for your inquiry and chatting with 🤖🤖🤖 Sprouty 🤖🤖🤖 .Come back anytime — I'll be here, photosynthesizing. 🌞 Bye! ")
else:
    print("Sorry, I think you slipped. Type Y/N")
