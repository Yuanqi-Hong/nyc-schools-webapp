from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.db'
db = SQLAlchemy(app)

class School(db.Model):
	__tablename__ = 'schools'
	__table_args__ = {
		'autoload': True,
		'autoload_with': db.engine
	}
	dbn = db.Column(db.String, primary_key=True)
	# with this line we're setting the dbn column in our database to be the primary key
	# so when calling school in list.html, we'll be calling the dbn column

@app.route("/")
def hello():
	schools = School.query.all()
	return render_template("list.html", schools=schools)

@app.route("/schools/")
def schools():
	schools = School.query.all()
	return render_template("list.html", schools=schools)

# @app.route("/schools/01M539")
# def school():
# 	# school = School.query.first()
# 	# the above line pulls out the first row
# 	school = School.query.filter_by(dbn="01M539").one()
# 	# .one() or .first() work the same
# 	return render_template("show.html", school=school)

@app.route("/schools/<dbn>/")
def school(dbn):
	school = School.query.filter_by(dbn=dbn).first()
	return render_template("show.html", school=school)

# @app.route("/search")
# def search():
# 	name = request.args.get("query")
# 	schools = School.query.filter(School.school_name.contains(name)).all()
# 	return render_template("list.html", schools=schools)


# If this is running from the command line, do something
if __name__ == '__main__':
	app.run(debug=True)
