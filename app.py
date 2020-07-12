"""
Created on Sat May  9 22:59:57 2020

@author: Madhan Kumar Selvaraj
"""

from flask import Flask, render_template, request
from chatbot_run import chatbot_response

from scrape import scrape_data


check_wikipedia1 = ['what', 'is']
check_wikipedia2 = ['who', 'is']
check_wikihow = ['how', 'to']
    




app = Flask(__name__)
@app.route("/login")
def login():
    return render_template("login.html")
    
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/")
def mainpage():
    return render_template("home.html")

@app.route("/homepage")
def homepage():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    user_request = request.args.get('msg')  # Fetching input from the user
    user_request = user_request.lower()
    if len(user_request.split(" ")) > 1:
        check_search = user_request.split(" ")[0]
        if check_search == 'google':
            user_request = user_request.replace("google","")
            user_request = user_request.translate ({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
            check_query = user_request.split(" ")[1]
            check_text = user_request.split(" ")[1:3]
            if check_text == check_wikipedia1 or check_text == check_wikipedia2:
                response = scrape_data(user_request, "wikipedia")
            elif check_text == check_wikihow:
                response = scrape_data(user_request, "wikihow")
            elif check_query == "nearby":
                response = scrape_data(user_request, "nearby")
            else:
                response = scrape_data(user_request, "")
        else:
            if user_request == 'how are you?' or user_request == 'how are you':
                response= 'Fine , Good to see you again'
            elif user_request == 'what is your name' or user_request == 'Who are you':
                response = ' I am farmbot, I help in agriculture related problems'
            elif user_request == 'what is agriculture' or user_request == 'define agriculture':
                response = 'Agriculture is the science or practice of farming, including cultivation of the soil for the growing of crops and the rearing of animals to provide food, wool, and other products.'
            elif user_request == 'What Is Organic Gardening' or user_request == 'What Is Organic farming':
                response = 'Organic gardening is more than simply avoiding synthetic pesticides and fertilizers. It is about observing nature’s processes, and emulating them in your garden as best you can. And the most important way to do that is to understand the makeup of your soil and to give it what it needs. If anything could be called a ‘rule’ in organic gardening, it’s this: feed the soil, not the plant'
            elif user_request == 'what is the reason behind the tomatoes leaves having spots ' or user_request == 'what to do if my tomato leaves have spots ':
                response = 'Tiny spots may be due to spider mites, which tend to gather on the undersides of leaves, as do tiny pale aphids. A good spray from the hose (including both sides of the leaves) often will take care of such an infestation. If that doesnt work, try an insecticidal soap (avoid home-grown soap solutions, which can strip the protective coating from leaves). Sometimes brown spots indicate a minor fungus infection. To deter fungus problems, avoid overwatering and stake plants so they get good air circulation'
            elif user_request == 'what are all the watering methods for onion' or user_request == 'proper watering technique for onion':
                response = 'Watering once a week usually is enough in the spring. But you may need to water more often during dry, windy weather. Water onions slowly and deeply to help grow strong, healthy roots.'
            elif user_request == 'Why is jasmine plant not flowering' or user_request == 'why is my plant not flowering':
                response = 'Though your plant looks healthy with lustrous green foliage, it may not bloom flowers. It is due to the lack of feeding the plants with water and fertilizers rich in nitrogen and phosphorus. So apply the fertilizers that jasmine plants love to absorb nutrients from them and bloom flowers quickly. Prune the jasmine plant when it stops blooming fragrant flowers'
            elif user_request == 'How to cultivate crop faster' or user_request == 'how can crop yields be increased':
                response = '1.Plant Early, Plant Effectively 2.Practice Seasonal Soil Rotation 3. Know The Yield Potential 4. Always Scout Your Fields 5. Ensure Proper Water Drainage 6. Utilize Fertilizers 7. Test Your Soil 8. Weed Early and Often.'
            else:
                user_request = user_request.translate ({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
                check_query = user_request.split(" ")[1]
                check_text = user_request.split(" ")[1:3]
                if check_text == check_wikipedia1 or check_text == check_wikipedia2:
                    response = scrape_data(user_request, "wikipedia")
                elif check_text == check_wikihow:
                    response = scrape_data(user_request, "wikihow")
                elif check_query == "nearby":
                    response = scrape_data(user_request, "nearby")
                else:
                    response = scrape_data(user_request, "")                

    else:
        if user_request == 'hi':
            response = 'Hello , Thanks for your greeting'
        elif user_request == 'bye' or  user_request == 'thank you':
            response = 'bye, Thank you'
        elif user_request == 'hello':
            response = 'Good to see you again'
        else:
            response = '...'
    
   
    return response

if __name__ == "__main__":
    app.run(threaded=False)
