from app import app, flatpages, LESSON_DIR
from flask import render_template
from itertools import groupby


@app.route('/')
def hello_world():

    pages = sorted(flatpages, key=lambda p: p.path)
    print(pages)
    days = groupby(pages, lambda p: p.meta['day'])

    return render_template('index.html', days=days)



if __name__ == '__main__':
    app.run(debug=True)

