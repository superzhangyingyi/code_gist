from flask import Flask, request
import json
 
app = Flask(__name__)
 
@app.route('/webhook', methods=['post'])
def post_http():
    # print(json.dumps(request.json))
    print("*" * 100)
    print(request.headers)
    print("*" * 100)
    print(request.data.decode('unicode_escape'))
    return {"code": 200, 'msg': 'success'}
 
if __name__ == '__main__':
    app.run(host='192.168.3.118', port=8080)
