from flask import Flask, render_template, request
import json

app = Flask(__name__)





qwer=["b","c","d","e","f","g"]
@app.route('/')
def index():
	return render_template('index.html', qwe=qwer)

if __name__ == '__main__':
    app.run()