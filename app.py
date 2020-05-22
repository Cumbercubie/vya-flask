from flask import Flask, request, render_template, json
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
    # getAllComments(sub_id,limit), limit = your desired replies + 2,
    # idk why, it works like that.
    cmts = json.dumps(red.getAllComments(sub_id,7))
    # return render_template('reddit.html',cmts)
    return cmts
#Run server

if __name__ == '__main__':
    app.run(debug=True)