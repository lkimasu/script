## 인프라를 효율적으로 관리 하기 위한 스크립트

# cpu_memory_use

파이썬 환경에서 Cpu,Memory를 확인을 해서 80% 이상일 경우 관리자에게 메일을 보내는 스크립트 입니다.<br>
로컬 환경에 Python과 pip가 설치되어 있어야 합니다.<br>
config.py를 열어서 메일 정보를 수정 하세요.<br>
저는 구글 smtp 서버를 이용했습니다.<br>

예시:

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'test@gmail.com'
EMAIL_PASSWORD = 'password'
RECIPIENT_EMAIL = 'test@gmail.com'

프로그램을 실행하면 Cpu,Memory를 확인을 해서 80% 이상일 경우 메일을 보내고 <br>
HostName,Cpu Percent,Memory Percent, Top5 cpu process,Top5 memory process를 확인 할 수 있습니다.<br> 
