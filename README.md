### 南京工业大学校园网自动登录脚本

## 简介

- 支持Windows, Linux
- 实时监测网络连通状态，如果断开自动登录校园网
- 支持Njtech, Njtech-Home 

## 运行环境

#### 源码运行

- Windows, Linux
- Python 3+
- 外部依赖库：requests, beautifulsoup, argparse 

#### 可执行文件运行

- Windows, Linux

  

## 使用方法

#### 可执行文件运行

```powershell
.\autologin -username USERNAME -password PASSWORD -type TYPE -provider PROVIDER
```

其中username(学号), password(密码)为必填参数，type为必填参数只能是njtech或njtech-home，provider(运营商), 可填项cmcc, telecom, 默认为cmcc.

## 代码如有bug请提交issue
