from app import db
from models import Day, Lesson
from collections import OrderedDict

# Delete the Database, so we can completely start anew.
db.drop_all()

# Create Database
db.create_all()

# Fill with data
day_plan = OrderedDict()

day_plan['Introduction to Python'] = [
    'Working from the Command Line',
    'Running Python Scripts',
    'Variables, Operators, and Functions',
    'Data Collections',
    'Using Classes, Objects, and Methods'
    ]

day_plan['Introduction to the SciPy core: NumPy and Matplotlib'] = [
    'Importing Python Packages',
    "Working with NumPy Arrays",
    "Plotting with MatplotLib"
    ]

day_plan['Organizing Data in Tables'] = [
    'Intro. to Pandas: Series and DataFrames',
    'Loading and Saving your Data',
    'Higher-Level Plotting Libraries: Pandas and Seaborn'
    'Good Data Visualization Practices'
    ]


for day_title, lesson_titles in day_plan.items():
    day = Day(title=day_title)
    db.session.add(day)
    for lesson_title in lesson_titles:
        lesson = Lesson(title=lesson_title)
        db.session.add(lesson)


# Save all changes to the database file
db.session.commit()


# Confirm that the data is there!
days = Day.query.all()
for day in days:
    print(day)