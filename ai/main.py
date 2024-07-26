from doubao.finddoubaomoney import find_doubao_money
from kimi.findkimimoney import find_kimi_money
from kimi.qqemail import send_email

def main(email_list):
    print("开始查询")
    doubao = find_doubao_money()
    kimi = find_kimi_money()
    for item in email_list:
        result = send_email(doubao, kimi, item)
        print('给'+item + '邮件'+result)
    print("查询结束了")
if __name__ == "__main__":
    email_list = ['707884802@qq.com']
    main(email_list)

