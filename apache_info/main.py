from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from urllib import request
import config

def send_email(subject, body):

    msg = MIMEMultipart()
    msg['From'] = config.EMAIL_ADDRESS
    msg['To'] = config.RECIPIENT_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
    server.starttls()
    server.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(config.EMAIL_ADDRESS, config.RECIPIENT_EMAIL, text)
    server.quit()

def check_web_server(url):    
    try:
        response = request.get(url)
        if response.status_code == 200:
            print("웹 서버가 정상적으로 동작 중입니다.")
        else:
            print(f"서버 응답 상태 코드: {response.status_code}")
            print("웹 서버에 문제가 있을 수 있습니다.")
            send_email("웹 서버 오류 발생", "웹 서버에 문제가 있습니다. 조치가 필요합니다.")
    except Exception as e:
        print(f"에러 발생: {e}")

def main():
    apache_url = "http://your-apache-server/"
    check_web_server(apache_url)

if __name__ == "__main__":
    main()