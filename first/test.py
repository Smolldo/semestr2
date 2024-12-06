from flask import Flask, url_for, request, send_file

app = Flask(__name__)

@app.route('/login.html')
def send_login():
    return send_file('templates/login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['name']
        age = request.form['age']
        return f'POST request returned: {user}. {age}'
    else:
        user = request.args.get('name')
        age = request.args.get('age')
        return f'GET request returned {user}. {age}'


@app.route('/')
def greetings():
    return 'Hello User'


@app.route('/menu')
def menu():
    return 'This is menu page'


@app.errorhandler(404)
def page_not_found(error):
    return 'NO PAGE', 404


if __name__ == '__main__':
    with app.test_request_context():
        
        print(url_for('login'))
    app.run(port=7000, host = "0.0.0.0", debug= True)  # host port debug option