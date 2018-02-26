from flask import Flask, render_template, request, json, pymongo
from utils import pop

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('form.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
