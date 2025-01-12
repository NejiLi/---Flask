from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/achievements')
def achievements():
    return render_template('achievements.html')


if __name__ == '__main__':
    app.run(debug=True)
