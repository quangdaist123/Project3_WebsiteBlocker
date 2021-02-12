import time
from datetime import datetime as dt
# TODO: create necessaries
host_file = r"C:\Windows\System32\drivers\etc\hosts"
loopback_ip_addr = '127.0.0.1'
website_to_block = ['facebook.com', 'youtube.com', 'google.com']

# TODO: INFINITE LOOP
#       - Block
#       - Unblock
start_hr = 8
start_min = 0
end_hr = 17
end_min = 0
while True:
    dt_start_time = dt(dt.now().year, dt.now().month, dt.now().day, start_hr, start_min)
    dt_end_time = dt(dt.now().year, dt.now().month, dt.now().day, end_hr, end_min)
    if dt_start_time < dt.now() < dt_end_time:
        print('Blocking websites')
        with open(host_file, 'a+') as f:
            for website in website_to_block:
                f.write(loopback_ip_addr + ' ' + website + '\n')
                f.write(loopback_ip_addr + ' www.' + website + '\n')
            f.close()
    else:
        with open(host_file, 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if not any(website in line for website in website_to_block):
                    f.write(line)
            f.truncate()

        print("Oke hay lam Dai")
    time.sleep(5)

# TODO: GUI

