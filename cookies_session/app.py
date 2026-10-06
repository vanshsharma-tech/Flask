from flask import Flask, make_response, request, session

app = Flask(__name__)

secret_key = "my_secret_key"
# Please don't share this secret key with anyone.
app.secret_key = secret_key

@app.route('/')
def home():
    return "Cookies and Sessions"

@app.route('/set-cookie')
def setCookie():
    response = make_response("Cookie Set")
    response.set_cookie('full_name', 'Vansh Sharma')
    return response

@app.route('/get-cookie')
def getCookie():
    username = request.cookies.get('full_name')
    if username:
        return f'Welcome {username}'
    else:
        return 'No cookie found'

@app.route('/delete-cookie')
def deleteCookie():
    response = make_response("Cookie Deleted")
    response.delete_cookie('full_name')
    return response

@app.route('/set-session')
def setSession():
    session["username"] = "VanshSharma"
    session["email"] = "vanshvats.tech@gmail.com"
    session["role"] = "Admin"
    return "Session Created"

@app.route("/get-session")
def getSession():
    username = session.get("username")
    email = session.get("email")
    if username:
        return f"Welcome {username} , Email : {email}"
    else:
        return f"Session not found"

if __name__ == '__main__':
    app.run(debug=True)