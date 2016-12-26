from app import app, flatpages, pygments_style_defs
from flask import render_template, make_response


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/workshop/<name>')
def workshop_page(name):
    page = flatpages.get('workshops')
    workshop = page.meta[name]
    day_pages = [[flatpages.get('lessons/{}'.format(lesson)) for lesson in day['lessons']] for day in workshop['plan']]
    return render_template('workshop_summary.html', workshop=workshop, daydata=day_pages)


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
