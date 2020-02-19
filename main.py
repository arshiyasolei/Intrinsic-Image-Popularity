#!/usr/bin/env python

from flask import *  
app = Flask(__name__)  
import popmodel
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
@app.route('/')  
def upload():  
    return render_template("index.html")  
 
@app.route('/calculate/', methods = ['POST'])  
def calculate():  
    if request.method == 'POST':  
        f = request.files['file']
        print(f.filename)
        if '.png' not in f.filename and '.jpg' not in f.filename and '.JPG' not in f.filename and '.PNG' not in f.filename:
            resp = jsonify({"rsvp":"Wrong file type!"} )
            return resp
        else:
            f = Image.open(f)
            print(type(f))
            f = popmodel.doit(f)
            #percentiles with graph baby!!
            mu = 3
            variance = 2.3
            sigma = math.sqrt(variance)
            x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
            v = stats.norm(mu, sigma)
            percentile = stats.percentileofscore(x, f)
            #f.save(f.filename)
            resp = jsonify({"rsvp":percentile} )
            return resp

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=4000,debug=True, threaded=True)