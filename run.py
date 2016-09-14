from app import app
from flask import render_template
from models import WorkshopDay


lessons = ['This', 'is', 'just', 'testing', 'you']

@app.route('/')
def hello_world():
    days = WorkshopDay.query.all()
    return render_template('index.html', days=days, lessons=lessons)


if __name__ == '__main__':
    app.run(debug=True)

