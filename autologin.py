import requests
from bs4 import BeautifulSoup
import os
import platform
import time
import argparse

def is_connected():
    cmd = ''
    sysstr = platform.system()
    if sysstr == 'Windows':
        print("windows系统")
        cmd = 'ping baidu.com -n 4'
    elif sysstr == "Linux":
        print("Linux系统")
        cmd = 'ping baidu.com -c 4'
    result = os.system(cmd)
    if result == 0:
        return True;
    else:
        print("网络连接异常！")
        return False


def login(username, password, type, provider):
    post_addr="https://u.njtech.edu.cn/cas/login?service=https%3A%2F%2Fu.njtech.edu.cn%2Foauth2%2Fauthorize%3Fclient_id%3DOe7wtp9CAMW0FVygUasZ%26response_type%3Dcode%26state%3Dnjtech"
    get_addr="https://u.njtech.edu.cn/cas/login?service=https://u.njtech.edu.cn/oauth2/authorize?client_id=Oe7wtp9CAMW0FVygUasZ&response_type=code&state=njtech"

    response_gw = requests.get(get_addr)
    response_cookie = response_gw.cookies
    soup = BeautifulSoup(response_gw.content,"html.parser")
    lt0 = soup.find('input',attrs={'name':'lt'})['value']
    execution0 = soup.find('input',attrs={'name':'execution'})['value']

    post_header={
        'Accept': '*/*',
        'Accept-Language': 'zh-cn',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    }

    if type == 'njtech-home':
        supported_provider = {'cmcc':'中国移动','telecom':'中国电信'}
        if provider not in supported_provider.keys():
            print("运营商仅支持cmcc(中国移动)和telecom(中国电信)!")
            exit(0)
        else:
            channelshow = supported_provider[provider]

        post_data={
            'username': username,#学号
            'password': password,#密码
            'channelshow': channelshow,#中国移动，中国电信
            'channel': '@'+provider,#@cmcc,@telecom
            'lt': lt0,
            'execution': execution0,
            '_eventId': 'submit',
            'login': '登录',
        }

        requests.post(post_addr, data=post_data, headers=post_header, cookies=response_cookie)
        print("校园网登录成功！")
    elif type == 'njtech':
        post_data={
            'username': username,#学号
            'password': password,#密码
            'lt': lt0,
            'execution': execution0,
            '_eventId': 'submit',
            'login': '登录',
        }
        requests.post(post_addr, data=post_data, headers=post_header, cookies=response_cookie)
        print("校园网登录成功！")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Njtech-Home auto login')
    parser.add_argument('-username',dest='username',type=str,required=True,help='学号(必填参数)')
    parser.add_argument('-password',dest='password',type=str,required=True,help='密码(必填参数)')
    parser.add_argument('-type',dest='type',type=str,required=True,choices=['njtech','njtech-home'],help='上网方式选择(njtech, njecth-home)')
    parser.add_argument('-provider',dest='provider',type=str,default='cmcc',help='运营商(\'cmcc\',\'telecom\'默认为cmcc)')
    args = parser.parse_args()

    while True:
        if not is_connected():
            login(args.username,args.password,args.type,args.provider)
        time.sleep(0.1)
        