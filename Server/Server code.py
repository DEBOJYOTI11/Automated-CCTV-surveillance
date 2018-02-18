from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest
import os
from werkzeug import secure_filename
import json
from flask import send_from_directory
from flask_restplus import abort

import logging
from logging.handlers import RotatingFileHandler
import time
import traceback
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'DatasetGenerated'


@app.route('/')
def index():
     return render_template('index.html')



@app.route('/upload', methods=['GET', 'POST'])
def upload():
       
        if request.method == 'POST':
          print '[Info] In /upload with method=Post'
          for f in request.files.getlist('images'):
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
          return json.dumps({'status':'success'})
        else:
            return "This is for Post request only. Try a POst request"
        


@app.after_request
def after_request(response):
    if response.status_code != 500:
        ts = time.strftime('[%Y-%b-%d %H:%M]')
        logger.error('%s %s %s %s %s %s',
                      ts,
                      request.remote_addr,
                      request.method,
                      request.scheme,
                      request.full_path,
                      response.status)
    return response

@app.errorhandler(Exception)
def exceptions(e):
    ts = time.strftime('[%Y-%b-%d %H:%M]')
    tb = traceback.format_exc()
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                  ts,
                  request.remote_addr,
                  request.method,
                  request.scheme,
                  request.full_path,
                  tb)
    return "Internal Server Error", 500

@app.errorhandler(404)
def Internalerror(e):
    return "page not found. %s"%(e.message)

if __name__ == '__main__':
    handler = RotatingFileHandler('projectapp.log', maxBytes=10000, backupCount=3)
    logger = logging.getLogger('__name__')
    logger = logging.getLogger('werkzeug')
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)
    app.run(host='127.0.0.1', port=3000, debug  = True)  
