from flask import Flask, render_template
# from flask import escape, request,

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')
    # name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'

@app.route('/about')
def harry():
	name="harry rohan das"
	return render_template('about.html',name2=name)
    # name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'

app.run(debug=True)