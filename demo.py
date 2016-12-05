from flask import Flask
from flask import render_template
from flask import request
from algorithm import *

import yaml

app = Flask(__name__)

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

@app.route('/compute', methods=['GET', 'POST'])
def compute():
    if request.method == 'GET':
        return render_template('compute.html')
    else:
        input1 = request.form['input1']
        app.logger.debug(input1)
        print 'input1: ' + input1

        input2 = request.form['input2']
        app.logger.debug(input2)
        print 'input2: ' + input2

        input3 = request.form['input3']
        app.logger.debug(input3)
        print 'input3: ' + input3

        yamlInput1 = yaml.safe_load(input1)
        app.logger.debug(yamlInput1)
        print 'yamlInput1: ' + str(yamlInput1)
        print yamlInput1

        result = isDistinct(yamlInput1, input2, input3)
        print result
        return render_template('compute.html', result=result)
