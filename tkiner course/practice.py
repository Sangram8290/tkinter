# age=int(input("Type your age ="))
# birth_date=int(input("Type your DOB ="))
# a=birth_date + 100 - age
# if birth_date > 2022 :
#     print("You are not born yet")
# elif  birth_date < 1922 :
#     x=birth_date - age + 100
#     print (f"you have  alredy become  100 year old in ",x) 
      
# else:  
#     print (f"you wiil be 100 year old in ",a)

# print("harry got 68 aplles from his frnd ")
# n=68
# mx = int(input("what is the maximum number =  "))
# mn = int(input("what is the minuimum number =  "))

# for i in range(mn, mx+1):
#         if n % i == 0 :
#             print(f"{i} is a divisor of {n}")
#         else :
#             print(f"{i} is not a divisor of {n}")

# list1=[2,7,8,5,9]
# # list1.sort(reverse=True)
# revers1=list1[:]
# revers1.reverse()
# print(revers1)

# revers2=list1[:]

# print(revers2[::-1])

# revers3 =list1[:]
# for i in range(len(revers3)//2):
#     revers3[i],revers3[len(revers3) -i -1] = revers3[len(revers3) -i ,-1],revers3[i]
#     print(revers3)


# a=int(input("Enter the number of string : "))
# for i in range(a):
  
#     x=input("Enter input : ")
#     y=x
#     while(x!=x[::-1]):
#         x=int(x)+1
#         print(x)
#         x=str(x)

#     print(f"Next Palindrome of {y} is {x} ")




import pyttsx3
import datetime
import speech_recognition as sr

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print (voices[0].id)

engine.setProperty('vocie',voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning sonu singh')
    elif hour>=12 and hour<18:
        speak('good afternoon sonu singh')

    else :
       speak('good evening sonu singh')   


    speak("Hey Mr. singh i am jarvis how can i help you ")
def takeCommand():
    #  It takes microwphone input from user and return string output 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
        audio = r.listen(source)

        print ("again")
        

    try:
        print("Rcognizing.....")   
        query = r.recognize_google(audio, Language='en-in') 
        print(f"user saud {query}\n")

    except Exception as e:
        print(" Voice is not clear try again")
        return "none"    


    return query
if __name__== "__main__" :

    wishMe()    
    takeCommand()
    

