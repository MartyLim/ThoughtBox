from flask import Flask, render_template
app = Flask(__name__)

notes = [
	{
		'name':'Martin Lim',
		'title':'project ideas',
		'content':'quick note taking web application',
		'date':'12-20-2018'
	},
	{
		'name':'John Doe',
		'title':"grocery list",
		'content':'apples, tuna, chocolate',
		'date':'12-21-2018'
	}

]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', notes=notes)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
	app.run(debug=True)