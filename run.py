from app import app, flatpages, pygments_style_defs
from flask import render_template, make_response


@app.route('/')
def index():
    page = flatpages.get_or_404('workshops')
    workshops = page.meta
    return render_template('index.html', workshops=workshops)

@app.route('/workshop/<name>')
def workshop_page(name):
    page = flatpages.get_or_404('workshops')
    workshop = page.meta[name]
    for day in workshop['plan']:
        day['lessons'] = [flatpages.get('lessons/{}'.format(lesson)) for lesson in day['lessons']]

    return render_template('workshop_summary.html', workshop=workshop)#, daydata=day_pages)


@app.route('/resources')
def further_resources():
    page = flatpages.get_or_404('online_resources')
    return render_template('learning_resources.html', page=page)


@app.route('/pygments.css')
def pygments_css():
    """colors python code blocks in markdown text"""
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}


if __name__ == '__main__':
    app.run(debug=True)
