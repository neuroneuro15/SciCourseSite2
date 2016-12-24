from app import app, flatpages, LESSON_DIR, DAY_DIR, pygments_style_defs, LINKS_ACTIVE, freezer
from flask import render_template, make_response
from itertools import groupby


@app.route('/')
def index():
    return render_template('freelancer.html')

@app.route('/workshop')
def workshop():
    """Homepage"""
    lesson_pages = [p for p in flatpages if LESSON_DIR in p.path]
    lesson_pages = sorted(lesson_pages, key=lambda p: p.meta['num'])  # sort pages by filename
    days = groupby(lesson_pages,
                   lambda p: p.meta['day'])  # group pages into days [(0, [Page1, Page2]), (1, [Page3, Page4]),...]

    day_pages = [p for p in flatpages if DAY_DIR in p.path]
    day_pages = sorted(day_pages, key=lambda p: p.meta['num'])


    return render_template('landing.html', days=days, daydata=day_pages, links_active=LINKS_ACTIVE)



@app.route('/resources')
def further_resources():
    page = flatpages.get_or_404('online_resources')
    return render_template('learning_resources.html', page=page)


@app.route('/pygments.css')
def pygments_css():
    """colors python code blocks in markdown text"""
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}


@app.route('/file/<filename>')
def get_file(filename):

    with app.open_resource('content/exercises/{}'.format(filename)) as f:
        contents = f.read()

    response = make_response(contents)
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename)
    return response

if __name__ == '__main__':

    app.run(debug=True)
