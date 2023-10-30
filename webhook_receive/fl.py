from flask import Flask, request
import requests
import json
 
app = Flask(__name__)
 
@app.route('/webhook', methods=['post'])
def post_http():
    dbackup_head = {k:v for k, v in request.headers.items()}
    dbackup_body = json.loads(request.data.decode('unicode_escape'))
    print("*" * 100)
    print(dbackup_head)
    print("*" * 100)
    print(dbackup_body)
    WeCom_forward(dbackup_head, dbackup_body)
    return {"code": 200, 'msg': 'success'}

# json.dumps(ensure_ascii=False) 设置中文字符不自动转义
def WeCom_forward(head, body):
    tpObj = {"head": head, "body": body}
    WeCom_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ae2acf74-3a20-449c-9ec8-6cc79aeac712'
    data = {
      'msgtype': 'text',
      'text': {
          'content': json.dumps(tpObj, ensure_ascii=False),
      }
    }
    r = requests.post(WeCom_url, json=data)
    print(r.text)

if __name__ == '__main__':
    app.run(host='192.168.3.118', port=8080)
