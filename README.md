###开始

安装依赖
pip install -r requirements.txt

配置环境变量
OPENAI_API_KEY，输入你自己的秘钥

启动
python main.py

###请求示例


请求类型：post
http://0.0.0.0:7866/example-service/v1/user/request

{
    "system":"hi",
    "user":"hi"
}

正确返回

{
    "code": 0,
    "msg": "ok",
    "data": "Hello! How can I assist you today?"
}

TODO

mysql 入库gpt的请求信息