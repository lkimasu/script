# 인프라 관리 스크립트 모음

이 저장소는 인프라를 효율적으로 관리하기 위한 스크립트를 포함하고 있습니다.

## cpu_memory_use

이 스크립트는 파이썬 환경에서 CPU와 메모리 사용량을 확인합니다.<br> 
사용량이 80% 이상인 경우 관리자에게 이메일을 보냅니다.<br>
로컬 환경에는 Python과 pip가 설치되어 있어야 합니다.<br>
이메일 설정은 `config.py` 파일에서 수정할 수 있습니다.<br>
저는 구글 SMTP 서버를 사용했습니다. <br>

예시:

```python
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'test@gmail.com'
EMAIL_PASSWORD = 'password'
RECIPIENT_EMAIL = 'test@gmail.com' 
```

CPU와 Memory를 확인하여 80% 이상인 경우 메일을 보냅니다.
HostName, CPU Percent, Memory Percent, Top 5 CPU process, Top 5 memory process를 확인할 수 있습니다.
