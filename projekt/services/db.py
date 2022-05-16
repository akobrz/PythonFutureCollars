from datetime import datetime

def db_log(msg):
    dt = datetime.now()
    print(dt, msg)

if __name__ == "__main__":
    print("db")