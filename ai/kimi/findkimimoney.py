import requests
import configparser
import json

def find_kimi_money():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('config.ini')

    default_url = config.get('kimi', 'url')
    default_apikey = config.get('kimi', 'apikey')

    # 定义要设置的HTTP头部
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+default_apikey
    }

    #发送GET请求并带上自定义的HTTP头部
    response = requests.get(default_url, headers=headers)
    # 检查响应状态码
    if (response.status_code == 200):
        return json.loads(response.text)
    
    return