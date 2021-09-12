import re
import csv
from collections import Counter

# date and time


def reader(logfile):
    myregex = r'[0-9]..\\*.[a-zA-z].\\*.[0-9].[0-9]..[0-9]..[0-9]..[0-9].'

    with open(logfile) as f:
        log = f.read()
        my_datelist = re.findall(myregex, log)
        datecount = Counter(my_datelist)
        for k, v in datecount.items():
            print("Date and Time " + "=> " + str(k) +
                  " " + "Count " + "=> " + str(v))
        with open('datetime.csv', 'w') as f:
            for k, v in datecount.items():
                f.write(str(k) + "\n")


if __name__ == '__main__':
    reader("access.log")

    # Operating System


def reader(logfile):
    myregex1 = r'Windows'
    myregex2 = r'Ubuntu'
# count windows
    with open(logfile) as f:
        log = f.read()
        my_windows = re.findall(myregex1, log)
        windows_count = Counter(my_windows)
        for k, v in windows_count.items():
            print("IP Address " + "=> " + str(k) +
                  " " + "Count " + "=> " + str(v))
        with open('os.csv', 'w') as f:
            for k, v in windows_count.items():
                f.write(str(k) + ","+str(v)+",")
# count ubuntu
    with open(logfile) as f:
        log = f.read()
        my_ubuntu = re.findall(myregex2, log)
        ubuntu_count = Counter(my_ubuntu)
        for k, v in ubuntu_count.items():
            print("IP Address " + "=> " + str(k) +
                  " " + "Count " + "=> " + str(v))
        with open('os.csv', 'a') as f:
            for k, v in ubuntu_count.items():
                f.write(str(k) + ","+str(v))


if __name__ == '__main__':
    reader("access.log")

    # IP address


def access_log_reader(logfile):
    myregex4 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(logfile) as f:
        log = f.read()
        my_iplist = re.findall(myregex4, log)
        ipcount = Counter(my_iplist)
        for k, v in ipcount.items():
            print("IP Address " + "=> " + str(k) +
                  " " + "Count " + "=> " + str(v))
        with open('ipaddress.csv', 'w') as f:
            for k, v in ipcount.items():
                f.write(str(k) + "\n")

        # Create entry point of our code
if __name__ == '__main__':
    reader("access.log")
