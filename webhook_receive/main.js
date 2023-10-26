var express = require('express');
var request = require('request');
var app = express();

app.use(express.urlencoded({ extended: false }))
app.use(express.json())

app.post('/webhook', function(req, res){
    let msg = '';
    let headmsg = '';
    res.header('Access-Control-Allow-Origin', '*');
    res.send('accept post');
    msg = req.body;
    headmsg = req.headers
    console.log('---------------------HEAD-----------------------------');
    console.log(headmsg);
    console.log('---------------------BODY-----------------------------');
    console.log(msg);
    WeCom_transfrom(headmsg, msg)
})

//将迪备的请求格式转换成 企业微信-机器人推送消息的规定格式 (仅仅将body转化成字符串)
function WeCom_transfrom(head_json, body_json) {
    let newObj = {"headers":head_json, "body":body_json}
    let tpStr = JSON.stringify(newObj)
    console.log(tpStr);
    // let sendUrl = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2642c203-abe4-4ab4-a48a-7029390803d7'
    let json_data = {
      'msgtype': 'text',
      'text': {
          'content': tpStr,
      }
    }
    request.post({url:sendUrl, body:json_data, json:true}, function(error, response, body) {
      console.log(body)
    })
}

app.listen(443, function () {
    console.log('dj_webhook nodejs server running');
})


