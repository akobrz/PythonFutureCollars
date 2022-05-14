from datetime import datetime
from time import sleep
from datetime import date, timedelta
import psutil


def stop():
    while True:
        print("sleeping")
        sleep(60)

def next_workday():
    dt = date.today()
    if dt.isoweekday() == 5:
        return dt + timedelta(days=3)
    if dt.isoweekday() == 6:
        return dt + timedelta(days=2)
    return dt + timedelta(days=1)

def wait(time):
    sleep(time)

def node_wait(node):
    # db.db_update_ping(node)
    now_hour = int(datetime.now().strftime("%H"))
    now_min = int(datetime.now().strftime("%M"))
    if now_hour >= 22 or now_hour <= 5:
        print("INFO, waiting for 300 sec.")
        sleep(150)
        return False
    elif now_hour == 21 and now_min >= 50:
        print("INFO, waiting for 300 sec.")
        sleep(150)
        return False
    else:
        print("INFO, waiting for 10 sec.")
        sleep(10)

        return True

def kill_browser():
    try:
        for proc in psutil.process_iter():
            if proc.name() in ('iexplore.exe', 'IEDriverServer.exe'):
                p = psutil.Process(proc.pid)
                if not 'SYSTEM' in p.username():
                    proc.kill()
                    print(f"WARNING, {proc.name()} with id = {proc.pid} killed")
    except:
        print("WARNING, problem with killing processes")
    try:
        for proc in psutil.process_iter():
            if proc.name() in ('iexplore.exe', 'IEDriverServer.exe', 'WerFault.exe'):
                p = psutil.Process(proc.pid)
                if not 'SYSTEM' in p.username():
                    proc.kill()
                    print(f"WARNING, {proc.name()} with id = {proc.pid} killed")
    except:
        print("WARNING, problem with killing processes")

if __name__ == "__main__":
    print("test")