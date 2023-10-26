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

})

app.listen(443, function () {
    console.log('dj_webhook nodejs server running');
})
