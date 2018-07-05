import re
import random
responses ={
    "about (.*)": "121",
    "Hi":["Hey","Hello","Hello, how could i help you"],
    "Hii":["Hey","Hello","Hello, how could i help you"],
    "hi":["Hey","Hello","Hello, how could i help you"],
    "hii":["Hey","Hello","Hello, how could i help you"],
    "Hello":["Hey","Hello","Hello, how could i help you"],
    "hello":["Hey","Hello","Hello, how could i help you"],
    "Hey":["Hey","Hello","Hello, how could i help you"],
    "hey":["Hey","Hello","Hello, how could i help you"],
    "admission procedure" :["(i) First you need to get yourself registered for the online entrance test of GLA University i.e. GLAET. Then you need to appear in the test at the APTECH Attest centers. Verify with the office the availability of the attest center in your city. Alternatively, the exam could be conducted in the office of GLA. You would be given your  result (qualified or not) soon after completing the exam.After qualifying the test one can deposit the fees at GLA University, Mathura or at city office in    form of DD/Cheque/Cash. The Demand draft can be issue from any nationalized bank in the favour of GLA University, Mathura payable at Vrindavan."],
   

    "default": [" try 'admission procedure'",
                "try 'about deepak mangal' "],
                
    "dehaii":[ "retry i can't understand ","i am here to solve your problems related to admission procedure ,show you the details of faculty,and basic qweries about placements and other ",
               "i can tell you about admission procedure","i can tell you about faculties if you ask"]
    }
patt_res={
    "about (.*)":[ "121","121"],
    "admission procedure (.*)" :["(i) First you need to get yourself registered for the online entrance test of GLA University i.e. GLAET. Then you need to appear in the test at the APTECH Attest centers. Verify with the office the availability of the attest center in your city. Alternatively, the exam could be conducted in the office of GLA. You would be given your  result (qualified or not) soon after completing the exam.After qualifying the test one can deposit the fees at GLA University, Mathura or at city office in    form of DD/Cheque/Cash. The Demand draft can be issue from any nationalized bank in the favour of GLA University, Mathura payable at Vrindavan."]
    }
bot_template = "BOT : {0}"
user_template = "USER : "#"USER : {0}"
def sql_responce(message):
    #responce by kshitij after searching in sql data base
    return "about the faculty"
def match_rule(message):
    response, phrase = None, None
    
    # Iterate over the rules dictionary
    for pattern, responses in patt_res.items():
        # Create a match object
       
        match = re.search(pattern, message)
        if match is not None:
          
            # Choose a random response
            response = random.choice(responses)
        else:
            
            responce = None
    # Return the response and phrase
    return response

f=0
def respond(message):
    # Check if the message is in the responses
    global f
    resp = match_rule(message)
    if resp=="121":
        bot_message = sql_responce(message)
    elif resp is not None:
        return resp    
    elif message in responses:
        f=0
        # Return the matching message
        bot_message = random.choice(responses[message])
    else:
        # Return the "default" message
        if f<=4:
            bot_message = random.choice(responses["dehaii"])
            f=f+1
        else:
            bot_message = random.choice(responses["default"])
        
    return bot_message

def send_message(message):
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


message =""

while message != "byy":
    # Print user_template including the user_message
    print(user_template,end="")
    message=input()
    send_message(message)
    
