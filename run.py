from app import app, flatpages, LESSON_DIR, pygments_style_defs
from flask import render_template
from itertools import groupby


@app.route('/')
@app.route('/index')
def index():
    """Homepage"""
    pages = sorted(flatpages, key=lambda p: p.path)  # sort pages by filename
    days = groupby(pages, lambda p: p.meta['day'])  # group pages into days [(0, [Page1, Page2]), (1, [Page3, Page4]),...]

    return render_template('index.html', days=days)

@app.route('/lessons/<title>')
def lesson(title):
    """Lesson pages"""
    page = [p for p in flatpages if title in p.meta['title']][0]  # match title in FlatPages title tag list
    return render_template('lesson.html', page=page)


@app.route('/pygments.css')
def pygments_css():
    """colors python code blocks in markdown text"""
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}



if __name__ == '__main__':
    app.run(debug=True)

