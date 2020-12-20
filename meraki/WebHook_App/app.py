from flask import Flask,request
import json

app = Flask(__name__)


@app.route('/webhook', methods=['GET','POST'])
def MerakiWebhook():
    if request.method== 'POST':
        req_body=request.data
        string_body= req_body.decode('utf-8')
        data= json.loads(string_body)
        if data['sharedSecret'] == 'foo':
            return data, 201
        else:
            return "Please check Shared Secret", 401
    elif request.method== 'GET':
        return 'c8b77133f4bd2218df387186212a6e946d5b4207', 200
    else:
        return "Bad Request", 400

app.run(debug=True, port=9999)
