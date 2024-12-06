from flask import Flask, render_template
app = Flask(__name__, template_folder = 'templates', static_folder = 'static')

@app.route('/')
def index():
    return render_template('base.html', title = 'Hello and welcome to Jinja2')


test_name = 'Python test'
max_score = 100
students = [
    {'name': 'Misha', 'score': 97},
    {'name': 'Vlad', 'score': 75},
    {'name': 'Oksana', 'score': 80},
    {'name': 'Marina', 'score': 89},
    {'name': 'Serhiy', 'score': 45},
]

@app.route('/results')
def results():
    context = {
        'title': 'Results',
        'students': students,
        'test_name': test_name,
        'max_score': max_score,
    }
    return render_template('results.html', **context)


projects = [
    {'name': 'STALKER 2', 'year': 2024},
    {'name': 'Dota 2 ', 'year': 2011},
]

@app.route('/portfolio')
def portfolio():
    context = {
        'title': 'Portfolio',
        'projects': projects
    }
    return render_template('portfolio.html', **context)


if __name__ == '__main__':
    app.run(port = 7050, debug = True)