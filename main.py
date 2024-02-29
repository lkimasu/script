import socket
import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

# HostName, CPU 및 메모리 사용량 체크 함수
def check_usage():
    hostname = socket.gethostname()
    cpu_usage = round(psutil.cpu_percent(interval=1), 2)
    memory_usage = round(psutil.virtual_memory().percent, 2)
    return hostname, cpu_usage, memory_usage

# CPU 사용량 높은 상위 5가지
def top_cpu_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        processes.append((proc.info['pid'], proc.info['name'], round(proc.info['cpu_percent'], 2)))
    top_cpu = sorted(processes, key=lambda x: x[2], reverse=True)[:5]
    return top_cpu

# 메모리 사용량 높은 상위 5가지
def top_memory_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        processes.append((proc.info['pid'], proc.info['name'], round(proc.info['memory_percent'], 2)))
    top_memory = sorted(processes, key=lambda x: x[2], reverse=True)[:5]
    return top_memory

# 이메일 보내는 함수
def send_email(hostname, cpu_usage, memory_usage, top_cpu, top_memory):

    msg = MIMEMultipart()
    msg['From'] = config.EMAIL_ADDRESS
    msg['To'] = config.RECIPIENT_EMAIL
    msg['Subject'] = 'Warning: High CPU/Memory Usage'

    body = f'Host Name: {hostname}\n CPU Usage: {cpu_usage}%\n Memory Usage: {memory_usage}%\n\nTop CPU Processes:\n'
    for pid, name, cpu_percent in top_cpu:
        body += f'PID: {pid}, Name: {name}, CPU Percent: {cpu_percent}\n'

    body += '\nTop Memory Processes:\n'
    for pid, name, memory_percent in top_memory:
        body += f'PID: {pid}, Name: {name}, Memory Percent: {memory_percent}\n'

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
    server.starttls()
    server.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(config.EMAIL_ADDRESS, config.RECIPIENT_EMAIL, text)
    server.quit()

# 메인 함수
def main():
    hostname, cpu_usage, memory_usage = check_usage()
    if cpu_usage > 10 or memory_usage > 10:
        top_cpu = top_cpu_processes()
        top_memory = top_memory_processes()
        send_email(hostname, cpu_usage, memory_usage, top_cpu, top_memory)

if __name__ == "__main__":
    main()
