s=input("do you want play this computer quies game : ")
mark=0
if s=="yes":
    print("lets go !")
    q1=input("what is mean by SBI : ")
    if q1.lower()=="state bank of india":
        print("correct")
        mark+=1
    else:
        print("incorrect")
      

    q1=input("what is mean by GPU : ")
    if q1.lower()=="graphics process unit":
        print("correct")
        mark+=1
    else:
        print("incorrect")
     

    q1=input("what is mean by SAAS : ")
    if q1.lower()=="software as a service":
        print("correct")
        mark+=1
    else:
        print("incorrect")
    

    q1=input("what is mean by DS : ")
    if q1.lower()=="data science":
        print("correct")
        mark+=1
    else:
        print("incorrect")
       

    q1=input("what is mean by SF : ")
    if q1.lower()=="soulfull":
        print("correct")
        mark+=1
    else:
        print("incorrect")
       
else:
   print("thank you")
print("your score :",mark)
print("thank you")


