var express = require('express');
var request = require('request');
var app = express();

// express.json()默认解析application/json，输出为对象类型，自动转字符集，但是遇到body为空会报错
// app.use(express.json())

// 指定type类型，解析application/json类型请求，输出字符串
app.use(express.text({type:'application/json'}))

app.post('/webhook', function(req, res){
    let msg = '';
    let headmsg = '';
    res.header('Access-Control-Allow-Origin', '*');
    res.send('accept post');
    headmsg = req.headers
    msg = req.body;
    let objBody = JSON.parse(unescape(msg.replace(/\\u/g, "%u")))
    console.log('---------------------HEAD-----------------------------');
    console.log(headmsg);
    console.log('---------------------BODY-----------------------------');
    // 解码中文
    console.log(objBody);
    WeCom_transfrom(headmsg, objBody)
})

//将迪备的请求格式转换成 企业微信-机器人推送消息的规定格式 (仅仅将body转化成字符串)
function WeCom_transfrom(head_json, body_json) {
    let newObj = {"headers":head_json, "body":body_json}
    let tpStr = JSON.stringify(newObj)
    console.log(tpStr);
    let sendUrl = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ae2acf74-3a20-449c-9ec8-6cc79aeac712'
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


