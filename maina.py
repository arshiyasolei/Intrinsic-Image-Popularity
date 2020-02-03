#!/usr/bin/env python

from flask import *  
app = Flask(__name__)  
import good
from PIL import Image
@app.route('/')  
def upload():  
    return render_template("index.html")  
 
@app.route('/calculate/', methods = ['POST'])  
def calculate():  
    if request.method == 'POST':  
        f = request.files['file'] 
        f = Image.open(f)
        print(type(f)) 
        f = good.doit(f)
        #f.save(f.filename)  
        resp = jsonify({"rsvp":f} )
        return resp
  
if __name__ == '__main__':  

    app.run(host = '0.0.0.0',port=5000,debug=True, threaded=True)