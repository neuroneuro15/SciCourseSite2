from app import db
from models import WorkshopDay

# Delete the Database, so we can completely start anew.
db.drop_all()

# Create Database
db.create_all()

# Fill with data
day_titles = [
    'Introduction to Python',
    'Numpy and Matplotlib: Collecting Data and Making Charts',
    'Pandas DataFrames',
    '...And More!',
]

for title in day_titles:
    day = WorkshopDay(title=title)
    db.session.add(day)

# Save all changes to the database file
db.session.commit()


# Confirm that the data is there!
days = WorkshopDay.query.all()
print(days)