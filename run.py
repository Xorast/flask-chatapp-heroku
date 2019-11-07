import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "randomstring123")
messages = []


def add_message(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append({"timestamp": now, "from": username, "message": message})
    
    """ messages.append("({}) {}: {}".format(now, username, message)) """
 
"""
def get_all_messages():
    # Get all of the messages and separate them with a `br`#
    return "<br>".join(messages)    
"""

@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session: 
        return redirect(url_for("user", username=session["username"]))
        
    """ to check if username exists in session and if so we redirect to contents of username session, which takes us to the .route("/<username>") underneath """
   
    return render_template("index.html")


@app.route("/chat/<username>", methods=["GET", "POST"])
def user(username):
    """Add and display chat messages using post method"""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"]))
        # redirect unless code reload and sends each 5 seconds
    
    return render_template("chat.html", username=username,
                           chat_messages=messages) 
                           
    """ return "<h1>Welcome, {0}</h1>{1}".format(username, messages) """
    """ removed get all messages replaced with messages list """

""" 
@app.route("/<username>/<message>")
def send_message(username, message):
    #Create a new message and redirect back to the chat page
    add_messages(username, message)
    return redirect("/" + username)
""" 

app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")), debug=False)