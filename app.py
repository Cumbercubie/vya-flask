from flask import Flask, request, render_template
import os

#Init app
app = Flask(__name__)


#onfig routes:

@app.route('/',methods=['GET'])
def get():
    return render_template('index.html')

@app.route('/reddit',methods=['GET'])
def extract():
    sub_id = "3g1jfi"
    from Extractor import RedditExtractor
    red = RedditExtractor()
    cmts = red.getComments(sub_id)
    # return render_template('reddit.html',cmts)
    return cmts
#Run server

if __name__ == '__main__':
    app.run(debug=True)