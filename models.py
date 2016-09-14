from app import db


class Day(db.Model):
    __tablename__ = 'day'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False)
    lessons = db.relationship('Lesson', backref='day', lazy='dynamic')

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<WorkshopDay %r>' % self.title


class Lesson(db.Model):
    __tablename__ = 'lesson'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'))

    def __init__(self, day, title):
        self.title = title
        self.day = day


    def __repr__(self):
        return '<Lesson %r' % self.title

