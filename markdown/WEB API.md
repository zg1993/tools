### 一、使用app_key和app_secret获取accesstoken
http请求方式：post
- 测试服url： http://topenapi.mgm-iot.com/v1
- 生产服url： https://openapi.mgm-iot.com/v1

request url: http://topenapi.mgm-iot.com/v1/token

request headers: {Content-Type: application/json}

request body:
```js
{"func": "get_access_token",
 "data":{
    "app_key": "app_key",
    "app_secret": "app_secret"
}}
```

返回
```js
{code: 200,
 data:{
    "access_token": "ACCESS_TOKEN",
    "expires_in": 7200
    "refresh_token": REFRESH_TOKEN
    }
}
```

- 参数说明
    + access_token接口调用凭证
    + expires_inaccess_token接口调用凭证超时时间，单位（秒）
    + refresh_token用户刷新access_token

错误返回样例：
```javascript
{
"message": "app key disabled",
"code": 3002,
"data": {}
}
```



### 二、通过access_token调用接口
http请求方式：post

request url: http://topenapi.mgm-iot.com/v1/resource

request headers: {Content-Type: application/json}

request body:
```javascript
{"func": "func_name",
"access_token":"access_token",
"data":{
  "key": "value"
}}
```
返回：
```js
{
  "code": CODE,
  "data"：DATA,
  "message": MESSAGE}
```
- code 200 数据请求成功 data 返回的数据

- code不等于200时候 message 错误消息



#### 1、刷新access_token有效期
access_token是调用授权关系接口的调用凭证，由于access_token有效期（目前为2个小时）较短，当access_token超时后，可以使用refresh_token进行刷新，access_token刷新结果有两种：

- 若access_token已超时，那么进行refresh_token会获取一个新的access_token，新的超时时间；
- 若access_token未超时，那么进行refresh_token不会改变access_token，但超时时间会刷新，相当于续期access_token。

request url: http://topenapi.mgm-iot.com/v1/token
```js
{"func": "refresh_token",
"data":{
"app_key": "APP_KEY"
    "refresh_token": "REFRESH_TOKEN"
}}
```
返回
```js
{
  "code": 200,
  "data":
    {
      "access_token": "ACCESS_TOKEN",
      "expires_in": 7200
      "refresh_token": REFRESH_TOKEN
    }
}
```

#### 2、获取工厂组织架构body
```js
{
  "func": "get_organization",
  "access_token":"0011",
  "data":{
}}
```
返回：

    工厂组织架构：产区，车间，生产线，机床存在于生产线下面，改架构只返回相应权限下的组织架构。
    （权限的分配在moses设置中心-云端API授权里查看）
```js
{
    "code": 200,
    "data": {
        "factory_id": "8wCx",
        "members": {
            "0": {
                "id": "8wCxAAA=",
                "name": "厂区",
                "members": {
                    "0": {
                        "id": "8wCxAAAAAA==",
                        "name": "车间1",
                        "members": {
                            "1": {
                                "name": "生产线",
                                "members": {
                                    "0": {
                                        "name": "盒子未配置",
                                        "machine_id": "8wCxAAAAAAABAAA="
                                    }
                                },
                                "id": "8wCxAAAAAAAB"
                            }
                        }
                    }
                }
            }
        },
        "id": "8wCx"
    }
}
```
#### 3、获取机床的元数据
```js
{"func": "get_sys_info",
"access_token":"0011",
"data":{
    "machine_list": ["8wCxAAAAAAAAABg="]
}}
```
返回：
```js
{
    "code": 200,
    "data": {
        "8wCxAAAAAAAAABg=": {
            "cnc_system": "",
            "cnc_class": "",
            "cnc_model": "789"
        }
    }
}
```
- cnc_system: cnc系统型号（系列）
- cnc_class: cnc系统类型
- cnc_model: 机床型号


#### 4、websocket推送，实时推送一台机床的状态
js示例代码
```js
<script src="https://cdn.jsdelivr.net/npm/sockjs-client@1/dist/sockjs.min.js"></script>
<script>
    var sock = new SockJS('http://topenapi.mgm-iot.com/v1/real_time?session_id=access_token');
    sock.onopen = function() {
      console.log('open');
    };
    sock.onmessage = function(obj) {
      console.log(obj);
    };
    sock.onclose = function() {
      console.log('close');
    };
</script>
```
##### 4.1获取机床的实时状态：
url：http://topenapi.mgm-iot.com/v1/real_time?session_id=access_toke
```js
var msg = JSON.stringify({'machine_id': 'GADIAAAAAAAAAA8=', 'page': 'a'})
sock.send(msg)
```

服务器返回消息：
```js
// 机床的状态信息，如果有报警则带上报警相关信息
{status: 5, status_time: "2018-09-17T01:52:52.894000Z", machine_id: "GADIAAAAAgABAAA="}
// 主轴转速、倍率、负载，进给、进给倍率，各轴单位、坐标和负载数据等信息
{
"Fovr": "300.000"
"S1load": "0.000"
"S1speed": "0.000"
"S1speedOvr": "100.000"
"Xact": "259.212"
"Xload": "1.000"
"Yact": "352.546"
"Yload": "0.000"
"Zact": "-6273.725"
"Zload": "0.000"
"block": "T1 "
"id": "GADIAAAAAgABAAA="
"line": "0"
"path_feedrate": "150.000"
"program": "1004.1004"
"time": "2018-09-17T06:30:30.156Z"
"tool_id": "1"}
// 主轴转速、倍率、负载，进给、进给倍率，各轴单位、坐标和负载数据的实时变化
{"Xact": "260.306", "id": "GADIAAAAAgABAAA=", "Yact": "353.640"}
```
##### 4.2文件传输：
ws://topenapi.mgm-iot.com/v1/real_time/websocket?session_id=
wss://openapi.mgm-iot.com/v1/real_time/websocket?session_id=

url ： 'http://topenapi.mgm-iot.com/v1/trans_file?session_id=' + this.session_id + '&cloud_path=' + this.cloud_path + '&file_size=' + this.file_size + '&file_name=' + this.file_name + '&storage_type=' + this.storage_type + '&machine_id=' + this.machine_id

- session_id: access_token
- file_size: 文件大小
- cloud_path: 目的文件路径
- file_name: 文件名
- storage_type: 文件传输类型 (0：本地到机床外部存储 1：本地到机床内部存储)
- machine_id: 机床id

```js
var conn = new SockJS(url, this.transports)
var msg = JSON.stringify({'content': content, 'file_md5': file_md5})
conn.send(msg)
// 建立链接后收到服务器返回的
{code: 200, file_seek: 0, file_id: "ff973dd6ba4111e8852800163e026f57"}
// 传输成功后返回
{code: 200, request_id: "1537136569199e442dba4211e8853000163e026f57"}
```
- content：文件内容对应的base64编码
- file_md5: content经过md5散列后的值
- 文件传输限制文件大小: 50M
- 建议每次content大小：64KB





[测试服demo](http://tmoses.mgm-iot.com/openapi_demo/#)

### 补：
#### Access_token 补充：
  - 过期时间2h
  - 只有获取的access_token有效
  - 通过access_token调用api的频率：200次/分钟

#### websocket推送相关：
- websocket连接上以后，当access_token过期后服务器发送过期提示并会断开连接，客户端需要自己重新去连接
- 文件传输限制文件大小: 50M
- 建议每次content大小：64KB

##### 报错
```python
class OauthCode(object):
    ACCESS_TOKEN_EXPIRES_IN = 7200
    REFRESH_TOKEN_EXPIRES_IN = 3600 * 24 * 30
    KEY_ERROR = 3000
    SECRET_ERROR = 3001
    KEY_DISABLE = 3002
    ACCESS_TOKEN_ERROR = 3003
    REFRESH_TOKEN_ERROR = 3004
    ACCESS_TOKEN_EXPIRED = 3005
    REFRESH_TOKEN_EXPIRED = 3006
    INVALID_TOKEN = 3007
    NOT_LASTED_TOKEN = 3008
    CALL_FREQUENTLY = 3009
    NO_PERMISSION = 3011
    NO_MACHINE = 3012
    FORBID_APP_KEY = 3013


class OauthMessage(object):
    KEY_ERROR = 'invalid app_key'
    SECRET_ERROR = 'invalid app_secret'
    KEY_DISABLE = 'app key disabled'
    ACCESS_TOKEN_ERROR = 'invalid access_token'
    REFRESH_TOKEN_ERROR = 'invalid refresh_token'
    ACCESS_TOKEN_EXPIRED = 'access_token expired'
    REFRESH_TOKEN_EXPIRED = 'refresh_token expired'
    INVALID_TOKEN = 'invalid token'
    NOT_LASTED_TOKEN = 'not lasted token'
    CALL_FREQUENTLY = 'api call too frequently'
    NO_PERMISSION = 'no permission'
    NO_MACHINE = 'the machine does not exist'
    FORBID_APP_KEY = 'app key disable'


class ContentError(object):
    CODE = 3010
    APP_SECRET = 'app_secret must be str'
    APP_KEY = 'app_key must be str'
    MACHINE_LIST = 'machine_list must be list'

    class VfsMessage(object):
        TRANS_ERROR_TOOL = {"-2": [711, "系统出错"], "-1": [712, "没有足够的存储空间"],
                            "1": [713, "内部存储已有该文件或路径"],
                            "2": [714, "外部存储已有该文件或路径"],
                            "3": [715, "内部存储无该文件或路径"],
                            "4": [716, "外部存储无该文件或路径"],
                            "5": [717, "内部存储无该路径"],
                            "6": [718, "外部存储无该路径"],
                            "7": [719, "文件名不合法"],
                            "8": [723, "系统出错"],
                            "9": [730, "盒子与机床断开连接"],
                            "10": [731, "文件过大"],
                            "11": [732, "文件内容格式不合法"],
                            "12": [733, "文件已经存在"],
                            "13": [734, "未获取到存储"],
                            "404": [720, "响应超时"],
                            "-3": [721, "该系统型号暂不支持创建文件夹"]
                            }
        LOCK_ERROR_TOOL = {"-1": [722, "该机床暂不支持"],
                           "1": [723, "加锁文件不符合要求"],
                           "2": [724, "盒子与机床连接异常"]}
        FILE_NOT_EXIST = '文件不存在或已删除，请刷新页面后重试'
        FAIL_CODE = '操作失败'
        FILE_TYPE_WRONG = '文件类型错误'
        FILE_EXIST = '文件已存在'
        PATH_NOT_EXIST = '路径不存在'
        DELETE_CNC_FILE_FAIL = "删除内部存储文件失败"
        DELETE_BOX_FILE_FAIL = "删除外部存储失败"
        FILE_IN_CNC_NOT_EXIST = "内部存储无此文件"
        FILE_IN_BOX_NOT_EXIST = "外部存储无此文件"
        FILE_IN_CNC_EXIST = "内部存储该文件已存在"
        FILE_IN_BOX_EXIST = "外部存储该文件已存在"
        FILE_TO_CNC_FAIL = "传输到内部存储失败"
        FILE_TO_BOX_FAIL = "传输到外部存储失败"
        CNC_TO_BOX_FAIL = "内部存储到外部存储失败"
        GET_FILE_INFO_FAIL = "获取文件内容失败"
        CANT_ALTER_LARGE_FILE = "文件过大暂不支持编辑"
        ADD_FILE_DUPLICATION = "此次添加有重复文件"
        FLOW_NOT_ENOUGH = "贵公司剩余可下载流量不足"
        START_DNC_FILE = "在线加工失败"
        IS_MODIFY = "下列文件正在被操作"
        TIME_OUT = "盒子响应超时"
        NO_CONNECT = "请检查网络连接"
        STORAGE_TYPE_NOT_SUPPORT = "不支持的存储类型"
        NO_RPC_REQUEST = "rpc request 参数错误"
        GET_LOG_FILE_FAIL = "获取Log文件失败"
        MAX_OPERATOR = "重试次数超出上限"
        TRANS_CANCEL = "传输中断"
        CREATE_DIR_FAILED = "创建云端文件夹失败"
        EMPTY_NAME = "文件或文件夹名不能为空"
        TRANS_TIMEOUT = "传输超时"
        FILE_IS_TOO_LARGE = "文件大于50M，不支持传输"
        FILE_NAME_TOO_LONG = "全英文文件名不得大于180个字符，全中文文件名不得大于60个字符"
        FILE_EDIT_ERROR = "文件类型不支持编辑"
```

##### 示例代码(测试服demo源码)

###### api.js
```js
var test = new Vue({
    el: '#example',
    data: {
        select: 'machine',
        session_id: 'c2915ea819acac55f12a1519c75abff1',
        cloud_path: '/',
        file_size: 1400,
        file_name: '1.txt',
        storage_type: 0,
        machine_id: 'ewCdAAEAAAAAACE=',
        content: '',
        file_md5: '',
        conn: null,
        transports: ["websocket"],
        slist: [],
        status: null,
        alarm_str: '',
        status_dict: {0: '停机', 1: '加工', 2: '下线', 3: 'deploy', 4: '报警', 5: '盒子断开'}
    },

    methods: {
        log: function(msg) {
            var control = $('#log')
            control.html(control.html() + msg + '<br/>');
            control.scrollTop(control.scrollTop() + 100);
        },
        // 文件传输
        trans_file: function() {
            /*
            - session_id: access_token
            - file_size: 文件大小
            - cloud_path: 目的文件路径, 可以填 '/'
            - file_name: 文件名
            - storage_type: 文件传输类型 (0：本地到机床外部存储 1：本地到机床内部存储)
            - machine_id: 机床id
            */
            url = 'http://topenapi.mgm-iot.com/v1/trans_file?session_id=' + this.session_id + '&cloud_path=' + this.cloud_path + '&file_size=' + this.file_size + '&file_name=' + this.file_name + '&storage_type=' + this.storage_type + '&machine_id=' + this.machine_id
            // url = 'http://localhost:8200/trans_file?session_id=' + this.session_id + '&cloud_path=' + this.cloud_path + '&file_size=' + this.file_size + '&file_name=' + this.file_name + '&storage_type=' + this.storage_type + '&machine_id=' + this.machine_id
            var conn = new SockJS(url, this.transports)
            this.conn = conn
            conn.onopen = function() {
                console.log('trans_file on open')
            }
            var file_md5 = this.file_md5
            var content = this.content
            conn.onmessage = function(e) {
                console.log(e.data)
                var data = e.data
                var file_id = data.file_id
                var file_seek = data.file_seek
                var code = data.code
                var request_id = data.request_id
                if (code != 200) {
                    log('RECEIVE: ' + data.code + ' ' + data.message)
                } else if (file_id){
                    // 服务器返回file_id后使用下面msg格式进行传输文件,传输成功返回{code: 200, file_seek: 0, file_id: "ff973dd6ba4111e8852800163e026f57"}
                    var msg = JSON.stringify({'content': content, 'file_md5': file_md5})
                    console.log(msg)
                    conn.send(msg)
                } else if (request_id) {
                    var control = $('#log')
                    control.html(control.html() + 'Transport File success' + '<br/>');
                    control.scrollTop(control.scrollTop() + 100);
                }
            }
            conn.onclose = function() {
                console.log('Colsed')
                conn = null
            }
        },


    },

    computed: {
        is_file: function() {
            return this.select == 'transport_file'
        }
    },
})
```

###### index.html
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8"/>
  <script src="https://cdn.bootcss.com/jquery/1.4.2/jquery.js"></script>
  <!-- <script src="https://cdn.jsdelivr.net/npm/sockjs-client@1/dist/sockjs.min.js"></script> -->
  <script src="https://cdn.jsdelivr.net/sockjs/1/sockjs.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <!-- <script src="https://cdn.jsdelivr.net/npm/vue"></script> -->
  <script src="http://cdn.bootcss.com/blueimp-md5/1.1.0/js/md5.js"></script>
  <link rel="stylesheet" type="text/css" href="./api.css">
    <script>

        $(function(){
           var conn = null;
           // 连接建立后发送该消息可以获取机床的实时状态, machine_id: get_organization接口里获取的machine_id, page: a(actual实时)
           var msg = JSON.stringify({'machine_id': 'GADIAAAAAAAAAA8=', 'page': 'a'})
           var second = 50000;
           log = test.log
           // 建立websocket连接
           function connect() {
            disconnect();
            // test.session_id get_access_token接口获取的access_token
            url = 'http://topenapi.mgm-iot.com/v1/real_time?session_id=' + test.session_id
            // url = 'http://localhost:8200/real_time?session_id=' + test.session_id
            conn = new SockJS(url, test.transports);
            // 建立连接的回调函数
            conn.onopen = function() {
              log('Connect');
              update_ui();
            };

            // 接受消息回调函数，处理机床实时消息
            conn.onmessage = function(e) {
              // log('Received: ' + e.data);
              var data = e.data
              if (data.code) {
                log('Error: ' + data.message);
              } else{
              init_table(data)
            }
            };

            // 连接关闭回调函数
            conn.onclose = function() {
              log('Disconnected.');
              conn = null;
              update_ui();
            };
           }
           // 断开连接
           function disconnect() {
            if (conn != null) {
              conn.close();
              conn = null;
              update_ui();
            }
           }

           function update_ui() {
            var msg = '';

            if (conn == null || conn.readyState != SockJS.OPEN) {
              $('#status').text('disconnected');
              $('#connect').text('Connect');
            } else {
              $('#status').text('connected');
              $('#connect').text('Disconnect');
            }
          }

           $('#connect').click(function() {
            if (conn == null) {
              connect();
            } else {
              disconnect();
            }
           })

           $('#send').click(function() {
            console.log('send')
            if (conn == null) {
              log('not connected ...')
            } else {
              var machine_id = $('#machine_id').val()
              if (!machine_id) {
                machine_id = 'GADIAAAAAAAAAA8='
              }
              var msg = JSON.stringify({'machine_id': test.machine_id, 'page': 'a'})
              conn.send(msg)
              log('send: ' +  msg)
            }
           })

           function init_table(data) {
            var tbody = $('#table1')
            tool_id = data['tool_id']
            status = data['status']
            if (data['status'] != undefined) {
              test.status = status
              if (status == 4) {
                test.alarm_str = JSON.stringify({'alarm_code': data['alarm_code'],
                            'alarm_info': data['alarm_info'], 'alarm_level': data['alarm_level'],
                            'alarm_type': data['alarm_type']})
              }
            }
            if (tool_id && test.slist.length == 0) {
              for (var k in data) {
                test.slist.push({'key': k, 'value': data[k]})
              }

            } else {
              for (var k in data)
                $('#'+k).text(data[k])
            }
           }

           var fileSelect = $(':file')
           $('.btn').click(function () {
            console.log('select file')
            if (fileSelect) {
              fileSelect.click()
            }
           })
        })
      console.log(FileReader)

      // 文件传输
     function handleFiles(files) {
            var file = files[0]
            console.log(files[0].name)
            test.file_name = files[0].name
            test.file_size = files[0].size
            var reader = new FileReader()
            // reader.readAsText(file)
            reader.readAsDataURL(file)
            reader.onload = function(f) {
              console.log('onload start ...')
              console.log(f.target.result)
              var content = f.target.result
              test.content = f.target.result.split(',')[1]
              test.file_md5 = md5(test.content) // 发送base64编码后的内容
              console.log('onload.....')
              test.trans_file()
            }
           }

    </script>
    <title>Machine Status</title>
</head>
<body>
<div id='example'>

<h3> {{ select }} </h3>
<div id="main" class="a">
<div class="select_type">
  <input type="radio" id="transport_file" value="transport_file" v-model="select">
  <label for="transport_file">transport_file</label>
  <br>
  <input type="radio" id="machine" value="machine" v-model="select">
  <label for="machine">machine</label>
  <br>
</div>
<div id="storage_type" v-show="is_file">
  <input type="radio" id="local_box" value="0" v-model="storage_type">
  <label for="local_box">本地到机床外部存储</label>
  <br>
  <input type="radio" id="local_cnc" value="1" v-model="storage_type">
  <label for="local_cnc">本地到机床内部存储</label>
  <br>
  <br>
 </div>
 </div>
<fieldset>
  <label for="session_id">session_id: </label>
  <input v-model="session_id" id="session_id" placeholder="session_id" type="text" style="width: 350px" /> <br>
  <label for="machine_id">machine_id: </label>
  <input v-model="machine_id" id="machine_id" placeholder="machine_id" type="text" style="width: 350px" /> <br>
  <label for="cloud_path" v-if="is_file">path: </label>
  <input v-model="cloud_path" v-if="is_file" id="cloud_path" placeholder="path" type="text" style="width: 350px" /> <br>
</fieldset>
<input type="file" name="" style="display:none" onchange="handleFiles(this.files)">
<a class="btn" href="#" v-show="is_file">Select File</a>
<!-- <a v-if="select=='Transport File'" class="btn" href="#">Select File</a> -->
<br>
<div v-show="!is_file">
<a id="connect" href="#">Connect</a> | Status: <span id="status">disconnected</span>

<p v-if="machine_id">send_msg: {'machine_id': '{{machine_id}}', 'page': 'a'} <a id="send" href="#">Send</a> </p>
</div>


<div id="log" style="width: 60em; height: 20em; overflow:auto; border: 1px solid black"></div>

<div>
  <p v-show="!is_file">Status: {{status_dict[status]}} </p> <p v-if="status=='4'"> {{alarm_str}} </p>

</div>

<table border="1">
  <tr v-cloak v-for="(item, index) of slist">
    <td> {{index}} </td>
    <td> {{item.key}} </td>
    <td v-bind:id="item.key"> {{item.value}} </td>
  </tr>
</table>


<table id="table1" border="1">

</table>

</div>
<script src="./api.js"></script>

</body>
</html>
```
