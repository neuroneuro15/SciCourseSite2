from app import app
from flask import render_template
from models import Day


lessons = ['This', 'is', 'just', 'testing', 'you']

@app.route('/')
def hello_world():
    days = Day.query.all()
    return render_template('index.html', days=days)


if __name__ == '__main__':
    app.run(debug=True)

