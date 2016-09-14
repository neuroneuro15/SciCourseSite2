from app import db

class WorkshopDay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<WorkshopDay %r>' % self.title
