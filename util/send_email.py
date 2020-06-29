import smtplib
from email.mime.text import MIMEText
from email.header import Header


host = "smtp.126.com"
from_server = "wyu0430@126.com"
password = "****"

def send_email(sub, to_list, content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = sub
    msg['From'] = "username" + "<" + from_server + ">"
    msg['To'] = ";".join(to_list)
    smtp = smtplib.SMTP()
    smtp.connect(host)
    smtp.login(from_server, password)
    smtp.sendmail(from_server, to_list, msg.as_string())
    smtp.quit()

def send_report_email(sub, to_list, reportpath):
    with open(reportpath,"rb") as file:
        content = file.read()
        msg = MIMEText(content,_subtype='html',_charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = "testcenter" + "<" + from_server + ">"
        msg['To'] = ";".join(to_list)
        smtp = smtplib.SMTP()
        smtp.connect(host)
        smtp.login(from_server, password)
        smtp.sendmail(from_server, to_list, msg.as_string())
        print('邮件发送成功')
        smtp.quit()

if __name__ == '__main__':
    sub = "测试summary"
    to_list = ["wyu0430@126.com","224138170@qq.com"]
    # content = "请查看测试结果"
    # send_email(sub, to_list, content)
    send_report_email(sub,to_list,"D:\\report\\201912191615_result.html")
