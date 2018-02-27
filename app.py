from flask import Flask, render_template, request
import json, pymongo
from utils import pop

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('form.html')

@app.route('/output/', methods=['POST'])
def output():
    data = pop.findByAge(int(request.form['age']))
    total = data['total']
    females = data['females']
    males = data['males']
    return render_template('output.html', data=data, total=total, females=females, males=males)

if __name__ == '__main__':
    app.debug = True
    app.run()

    
