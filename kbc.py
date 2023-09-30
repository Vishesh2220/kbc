print("welcom to Kaun Banega Crorepati ")
print("your first question of 10000 rupees is\n  Which god is also known as 'Gauri Nandan'?\n1).Hanuman\n2).Ganesha\n3).Agni\n4).Indra")
a1=eval(input("enter your answer your options are (1,2,3,4):"))
if(a1==2):
    print("*******your answer is correct you win 10000 rupees*******")
    print("your next question of 20000 rupees is")
    print("What does not grow on tree according to a popular Hindi saying\n1),Money\n2).Flowers\n3).Fruits\n4).Leaves")
    a2=eval(input("enter your answer your options are (1,2,3,4):"))
    if(a2==1):
      print("******your answer is correct you win 20000 rupees********")
      print("your next question of 50000 rupees is")
      print("Which city is known as Pink City in India?\n1).jaipur\n2)patna\n3).pune\n4).noida")
      a3=eval(input("enter your answer your options are (1,2,3,4):"))
      if(a3==1):
       print("******your answer is correct you win 50000 rupees********")
       print("your next question of 100000 rupees is")
       print("Who wrote India's National Anthem?\n1).Chetan Bhagat\n2).RK Narayan\n3).Lal Bahadur Shastri\n4).Rabindranath Tagore")
       a4=eval(input("enter your answer your options are (1,2,3,4):"))
       if(a4==4):
        print("******your answer is correct you win 100000 rupees********")
       else:
        print("sorry! your ans is wrong! you win only 50000 rupees")
      else:
       print("sorry! your ans is wrong! you win only 20000 rupees")
    else:
      print("sorry! your ans is wrong! you win only 10000 rupees")
else:
    print("sorry! your ans is wrong!")
