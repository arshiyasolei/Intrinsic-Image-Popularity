#!/usr/bin/env python

from flask import *  
app = Flask(__name__)  
import popmodel
from PIL import Image
@app.route('/')  
def upload():  
    return render_template("index.html")  
 
@app.route('/calculate/', methods = ['POST'])  
def calculate():  
    if request.method == 'POST':  
        f = request.files['file']
        if '.png' not in f.filename and '.jpg' not in f.filename:
            resp = jsonify({"rsvp":'Wrong file type!'} )
            return resp
        else:
            f = Image.open(f)
            print(type(f))
            f = popmodel.doit(f)
            #f.save(f.filename)
            resp = jsonify({"rsvp":f} )
            return resp
  
if __name__ == '__main__':  

    app.run(host = '0.0.0.0',port=4000,debug=True, threaded=True)