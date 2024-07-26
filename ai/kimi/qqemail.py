import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser

def send_email(doubao, kimi, receiver):
    config = configparser.ConfigParser()
    config.read('config.ini')
    # 设置SMTP服务器和账户信息
    smtp_server = 'smtp.qq.com'  # QQ SMTP服务器地址
    port = 465
    username = config.get('email', 'sender_email') # 您的QQ邮箱地址
    password = config.get('email', 'password') 
    # 设置发件人、收件人和邮件内容
    sender = username

    # 邮件内容
    message = f"""
    <html>
    <body>
    <h1>温馨提示</h1>
    <h2>账户余额通知</h2>
    <p>豆包余额：<span style="color: #ee1010; ">{doubao.available_balance}</span>元</p>
    <p>kimi余额：<span style="color: #ee1010; ">{kimi['data']['available_balance']}</span>元</p>
    </body>
    </html>
    """

    # 创建一个带附件的实例
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = "账户余额通知"

    # 设置邮件内容
    msg.attach(MIMEText(message, 'html'))

    # 连接到SMTP服务器并发送邮件
    try:
        server = smtplib.SMTP_SSL(smtp_server, port)  # 使用SSL加密连接
        server.login(username, password)  # 登录到SMTP服务器
        server.sendmail(sender, receiver, msg.as_string())  # 发送邮件
        server.quit()  # 断开连接
        return "发送成功"
    except Exception as e:
        return f"发送出错: {e}"