import psutil

mem=psutil.virtual_memory()
print('memory usage :', mem[2] ,'%')

# CPU 부하 출력
cpu=psutil.cpu_percent()
print('cpu usage :',cpu)

# DISK 사용률 퍼센트 출력
disk=psutil.disk_usage('/')
print('disk usage :', disk.percent,'%')

partitions = psutil.disk_partitions()

#C,D 드라이브
for i in partitions:
    print(i.mountpoint)
    try:
        du = psutil.disk_usage(i.mountpoint)
        print('total: %d GB' % round(du.total/1024/1024/1024))
        print('used: %d GB' % round(du.used/1024/1024/1024))
        print('free: %d GB' % round(du.free/1024/1024/1024))
    except:
        pass

