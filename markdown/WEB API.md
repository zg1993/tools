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
js例子
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
