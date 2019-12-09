
"""Chat_Bot.ipynb

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"(.*)@(.*).(.*)",
        ["Thanks for the details. May i know your latest Qualification. So that I can Provide you the Details.",]
    ],
    
     [
        r"en(.*)r(.*)ing",
        ["You want to about engineering course. Our enengineering course have fee 35000 INR and the scholarship will be as follow"]],
     [
        r"what (.*) name ?",
        ["My name is Enlight and I'm a chatbot ?",]
    ],
    [
        r"10|ten|x|xth|tenth|matric(.*)",
        ["According to your latest Qualification We have following course.\n1. Diploma in Engineering ( Fee:- 38000) \n2. Diploma in Management( Fee:- 58000) \n3. Diploma in Architecture( Fee:- 38000)\n4. Diploma in Hotel Management( Fee:- 68000)\n5. Diploma in Fashion Design( Fee:- 58000)\n6. Diploma in Medical Science( Fee:- 58000)\n\nScholarship Criteria \n95 and above OR LPUNest Criteria-1 50 of fee\n90-95 OR LPUNest Criteria-2 40 of fee\n80-90 and above OR LPUNest Criteria-3 30 of fee\n70-80 OR LPUNest Criteria- 20 of fee",]
    ],
    [
        r"12|12th|xii|xiith|twelveth|inter(.*)",
        ["According to your latest Qualification We have following course.\n1.Engineering ( Fee:- 98000) \n2.Management( Fee:- 68000) \n3.Medical( Fee:- 98000)\n4.Law( Fee:- 98000)\n5. BioTechnology( Fee:- 68000)\n6.Fashion Technlogy( Fee:- 98000)\n7.Journalism( Fee:- 98000)\n8.Agriculture( Fee:- 98000)\n9.Fashion Technlogy( Fee:- 78000)\n\nScholarship Criteria \n95 and above OR LPUNest Criteria-1 50 of fee\n90-95 OR LPUNest Criteria-2 40 of fee\n80-90 and above OR LPUNest Criteria-3 30 of fee\n70-80 OR LPUNest Criteria- 20 of fee",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello\nPlease enter your email and phone so we can contact you later", "Hey there\nPlease enter your email and phone so we can contact you later",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
       
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
       
    ],
    [
        r"(.*) created ?",
        ["Sunny created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Phagwara, Punjab',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) package (.*)",
        ["Highest Package from our University 42lpa.\nAverage pacakge is 4lpa.\nHope you like it:)"]
],
[
        r"(.*) placements (.*)",
        ["We have an excellent record of 100 percent Placements:)"]
],

    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]
def chatty():
        print("Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
        chat = Chat(pairs, reflections)
        chat.converse()
if __name__ == "__main__":
        chatty()