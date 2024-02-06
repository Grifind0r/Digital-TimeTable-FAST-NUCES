from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import json

app = Flask(__name__, static_url_path='/static')

# Load data
with open('classesDat.json', 'r') as f:
    classes_info = json.load(f)
with open('labsDat.json', 'r') as f:
    labs_info = json.load(f)

def func(subject, type):
    to_return=[]
    if (type == 'class'):
        for i in range(len(classes_info)):
            if(classes_info[i][-1] == subject):
                to_return.append('Day: '+str(classes_info[i][0])+'   Room: '+str(classes_info[i][1])+ '   Time: '+str(classes_info[i][2]))
    elif(type == 'lab'):
        for i in range(len(labs_info)):
            if(labs_info[i][-1] == subject):
                to_return.append('Day: '+str(labs_info[i][0])+'   Room: '+str(labs_info[i][1])+ '   Time: '+str(labs_info[i][2]))

    return to_return


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form['subject']
        subject_type = request.form['type']
        output = func(subject, subject_type)
        return render_template('index.html', output=output)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
