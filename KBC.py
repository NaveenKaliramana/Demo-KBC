#####           KBC Function         #####

def Call():
    global prize
    for i in range(r):
        print("Question Number ",i+1 ,"on your Screen\n")
        q = ques[i]
        print("Question for ", amount[i] ,"Rupees\n")
        print("Q.", q[0])
        print(q[1],"\t\t",q[2],"\n",q[3],"\t\t",q[4])
        res = input("Enter Your Answer(A,B,C,D,0(To Quit)) : ")
        if(res.upper() == ans[i]):
            print("Correct Answer\n")
            prize = amount[i]
            if(i==3):
                print("Congrats , Level 1 Cleared,\nYou will take Home atleast 10K\n")
            elif(i==8):
                print("Congrats , Level 2 Cleared,\nYou will take Home atleast 320K\n")
            elif(i==11):
                print("Congrats , Level 3 Cleared,\n 0You will take Home atleast 25 Lakh\n")
        elif(res.upper() == "0"):
            print("You Quit")
            if((i-1)<0):
                prize = 0
            else:
                prize = amount[i-1]
            break
        else:
            print("Oops ! , Wrong Answer")
            if(i<=3):
                prize =0
            elif(i>=4 and i<=8):
                prize = "10K"
            elif(i>=9 and i<=11):
                prize = "320K"
            else:
                prize = "25 Lakh"
            break             
    if(prize!=0):        
        print("You Played Well ,Congrats\n ")
    else:
        print("Good Luck for Next Time\n")
    return prize


#####               Main Program Using Tuple            #####

ques = (
        ("1. What is Capital City of Turkey ?",
         "A. Istanbul","B. Amsterdam","C. Ankara","D. Tehran"),
        ("2. What is Currency of Italy ?",
         "A. Euro","B. Peso","C. Dollar","D. Itlia"),
        ("3. Who lead 1857 Mutiny from Jhansi ?",
         "A. Ram Singh","B. Tatia Tope","C. Rani Laxmibai","D. Mangal Pandey"),
        ("4. Which Article related to Amendment of Constitution ?",
         "A. Article 371","B. Article 368","C. Article 325","D. Article 360"),
        ("5. Which Country won FIFA World Cup 2022 ?",
         "A. Argentina","B. Brazil","C. France","D. Crotcia"),
        ("6. Damdama Lake is situated in which State ?",
         "A. Rajasthan","B. Haryana","C. Delhi","D. Goa"),
        ("7. Which one is Metalloid ?",
         "A. Tellurium","B. Tin","C. Magnesium","D. Titanium"),
        ("8. Mahabharata names Haryana as ?",
         "A. Bahudhanyaka","B. Pramoda","C. Prajapathi","D. Gurusathal"),
        ("9. Leaves of Mimosa are Sensitive for ?",
         "A. Light","B. Heat","C. Smell","D. Touch"),
        ("10. First King of Vardhana Dynasty ?",
         "A. Jaya Vardhana","B. Prabhakar Vardhana","C. Harsha Vardhana","D. Geeta Vardhana"),
        ("11. The Panchayath Raj Bill passed in Parliament ?",
         "A. 2017","B. 1992","C. 1990","D. 1994"),
        ("12. Acid present in Tomato ?",
         "A. Citric Acid","B. Oxalic Acid","C. Lactic Acid","D. Acetic Acid"),
        ("13. Smallest UT of India by Area?",
         "A. Delhi","B. Chandigarh","C. Andaman Nicobar","D. Lakshadweep"),
        ("14. Number of Maha Jyoti Linga ?",
         "A. 16","B. 24","C. 12","D. 52")
        )
ans = ("C","A","C","B","A","B","D","A","C","C","B","A","D","C")
amount = ("1K","2K","5K","10K","20K","40K","80K","160K","320K","640K","12.5 Lakh","25 Lakh","50 Lakh","1 Crore")
r = len(ques)
print("\n\t\t\t\t\t *** Welcome To KBC *** \t\t\t\t\t")
print(" --- LET'S START --- \n")
Call()
print("You Won", prize ,"Rupees")