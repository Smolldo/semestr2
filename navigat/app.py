from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/index/")
def index():
    return render_template("base.html", title="All work fine")

@app.route("/results/")
def results():
    # Тестові дані для перевірки роботи
    students = [
        {"name": "Martadelka", "score": 85},
        {"name": "Micromolecula_1100", "score": 70},
        {"name": "Anihilatornaya pushka", "score": 92}
    ]
    return render_template(
        "results.html",
        test_name="Math Test",
        title="Results",
        students=students,
        max_score=100
    )


if __name__ == '__main__':
  app.run(port=7050, debug=True)