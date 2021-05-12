from flask import Flask, render_template

app = Flask("FlaskApp")
app.config['SECRET_KEY'] = 'thisisathirtytwocharacterstring!'

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)