from flask import Flask, make_response, request

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)