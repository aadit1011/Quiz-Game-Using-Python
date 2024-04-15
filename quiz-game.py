# Welcome to the quiz game by Aadit Sharma 
score=0;answer="";user="";
def question(q,o1,o2,o3,o4):
            global user;
            print(f"{q}");
            print(f"1.{o1}");
            print(f"2.{o2}");
            print(f"3.{o3}");
            print(f"4.{o4}");
            user=str(input("Your answer="));
            if user not in['1','2','3','4']:
                        recursion(q,o1,o2,o3,o4);
def recursion(q,o1,o2,o3,o4):
            print("You have chosen wrong option😥😥....Please kindly choose a 1,2,3,4 as option😊😊");
            question(q,o1,o2,o3,o4);  
# To check the answer 
def correct(ans,expected):
            global score,user;
            ans=user;
            if(ans==expected):
                print("Correct!!😍😍");
                score=score+1;
            else:
                print(f"Sorry!!😥😥Next time.The correct answer is {answer}");
# To display the result....
def resultDisplay(sc):
            global score;
            sc=score;
            if(score<=4):
                  print(f"Your score is {score}/7......Better Luck next time.💪😊😊");
            if(score>4):
                  print(f"Your score is {score}/7......Great Job!!😍😻🙀");


def main():
      global user,answer;
      questionCount=1;
      print("Welcome to the quiz game by Aadit Sharma");
      print("Let's start the game........");
      while(questionCount<=7):
            print(f"{questionCount}/7");
            answer="Liver";
            question(f"{questionCount}.What is the largest internal organ in the human body?","Lungs","Heart","Kidneys","Liver");
        
            correct(user,"4");
            questionCount=questionCount+1;
            print(f"{questionCount}/7");
            answer="71%";
            question(f"{questionCount}.What is the percentage of the Earth covered by water?","51%","61%","71%","81%",);
          
            correct(user,"3");
            questionCount=questionCount+1;
            print(f"{questionCount}/7");
            answer="Elephants";
            question(f"{questionCount}.Which is the largest animal on the Earth?","Lions","Tigers","Bears","Elephants");
         
            correct(user,"4");
            questionCount=questionCount+1;
            print(f"{questionCount}/7");
            answer="For all the dogs";
            question(f"{questionCount}.What was the name of Drake’s 2023 album?","Take Care","Views","Scorpion","For All the Dogs");
         
            correct(user,"4");
            questionCount=questionCount+1;
            print(f"{questionCount}/7");
            answer="Australia";
            question(f"{questionCount}.Which country is the band AC/DC from?","Australia","New Zealand","UK","USA");
         
            correct(user,"1");
            questionCount=questionCount+1;
            print(f"{questionCount}/7");
            answer="Babi guling";
            question(f"{questionCount}.Which of the following is not a Japanese dish?","Sushi","Ramen","Babi guling","Udon");
          
            correct(user,"3");
            questionCount=questionCount+1;
            print(f"{questionCount}/7");
            answer="1";
            question(f"{questionCount}.What is the atomic number of Hydrogen?","1","2","3","4");
          
            correct(user,"1");
            questionCount=questionCount+1;
            print("Quiz is now over........");
            resultDisplay(score);
main();    
