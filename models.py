from app import db

class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<WorkshopDay %r>' % self.title


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)

    def __init__(self, title):
        self.title = title


    def __repr__(self):
        return '<Lesson %r' % self.title



# class CalendarEvent(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     day = db.Column(db.Integer, primary_key=)
#     lesson = db.Column(db.Integer)

#     id = db.Column(db.Integer, primary_key=True)
#     day = db.Column(db.Integer, primary_key=)
#     lesson = db.Column(db.Integer)
