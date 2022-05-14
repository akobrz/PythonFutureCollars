import pyodbc
import time
from projekt.hunter import const, rekord
from datetime import datetime, timedelta
from pyodbc import OperationalError, DatabaseError, DataError, InternalError

# custom exception for screen element
class dbException(Exception):
    def __init__(self):
        super().__init__()
        db_log("WARNING, db exception raised")

# decorator function with bool return type
def db_exceptions_handler():
    def checker(func):
        def wrapper(*args):
            fn = f"{func.__name__} with: {args}"
            try:
                return func(*args)
            except DataError as e:
                db_log("INFO, data error exception for: " + fn )
                db_log(f"INFO, {e}")
                db_log("WARNING, raised exception for " + fn )
                raise dbException
            except InternalError as e:
                db_log("INFO, internal error exception for: " + fn )
                db_log(f"INFO, {e}")
                db_log("WARNING, raised exception for " + fn )
                raise dbException
            except OperationalError as e:
                db_log("INFO, operational error exception for: " + fn )
                db_log(f"INFO, {e}")
                db_log("WARNING, raised exception for " + fn )
                raise dbException
            except DatabaseError as e:
                print("INFO, database error exception for: " + fn )
                db_log(f"INFO, {e}")
                print("WARNING, raised exception for " + fn )
                raise dbException
        return wrapper
    return checker

# return cursor and conn to db
@db_exceptions_handler()
def connect():
    counter = 0
    while True:
        counter += 1
        try:
            conn = pyodbc.connect(driver='{SQL Server}', server=const.DB_SERVER, database=const.DB_NAME, UID=const.DB_USER, PWD=const.DB_PASSWORD)
            cursor = conn.cursor()
            return cursor, conn
        except DatabaseError:
            if counter < 4:
                print("WARNING, connection to DB failed")
            time.sleep(10)

@db_exceptions_handler()
def existsPEI(r):
    cursor, conn = connect()
    cursor.execute("SELECT count(*) from dbo.kolejka_1p where pei = ?", r.pei)
    row = cursor.fetchone()
    if row[0] == 1:
        return True
    return False

@db_exceptions_handler()
def deleteRecord(r):
    cursor, conn = connect()
    cursor.execute("delete from dbo.kolejka_1p where pei = ?", r.pei)
    conn.commit()
    return True

@db_exceptions_handler()
def selectRecord(pei, c):
    cursor, conn = connect()
    cursor.execute(f"select top(1) * from dbo.kolejka_1p where pei='{pei}'")
    row = cursor.fetchone()
    r = rekord.Rekord1P(c)
    r.create_from_db(dict(zip([i[0] for i in cursor.description], list(row))))
    db_log(f"INFO, located record in DB: {row[0]}")
    return r

@db_exceptions_handler()
def selectOldestRecord(criteria):
    cursor, conn = connect()
    cursor.execute(f"select top(1) * from dbo.kolejka_1p where status='{criteria.state}' and NazwaPromocji like '%{criteria.promotion}%' and wyborscendlarobota like '%{criteria.robot_scenario}%' and TypKlienta like '%{criteria.client}%' order by data_rejestracji")
    row = cursor.fetchone()
    r = rekord.Rekord1P(criteria)
    r.create_from_db(dict(zip([i[0] for i in cursor.description], list(row))))
    db_log(f"INFO, located record in DB: {row[0]}")
    return r

@db_exceptions_handler()
def db_select_oldest_B_with_criteria(criteria):
    cursor, conn = connect()
    cursor.execute(f"select top(1) * from dbo.kolejka_1p where status='{criteria.state}' and NazwaPromocji like '%{criteria.promotion}%' and wyborscendlarobota like '%{criteria.robot_scenario}%' and TypKlienta like '%{criteria.client}%' and StatusRobota like '%Zatwierdzono%' order by data_rejestracji")
    row = cursor.fetchone()
    r = rekord.Rekord1P(criteria)
    r.create_from_db(dict(zip([i[0] for i in cursor.description], list(row))))
    db_log(f"INFO, located record in DB: {row[0]}")
    return r

@db_exceptions_handler()
def existsOldestRecord(criteria):
    cursor, conn = connect()
    cursor.execute(f"select count(*) from dbo.kolejka_1p where status='{criteria.state}' and NazwaPromocji like '%{criteria.promotion}%' and wyborscendlarobota like '%{criteria.robot_scenario}%' and TypKlienta like '%{criteria.client}%'")
    row = cursor.fetchone()
    if row[0] > 0:
        return True
    return False

@db_exceptions_handler()
def db_check_exists_B_with_criteria(criteria):
    cursor, conn = connect()
    cursor.execute(f"select count(*) from dbo.kolejka_1p where status='{criteria.state}' and NazwaPromocji like '%{criteria.promotion}%' and wyborscendlarobota like '%{criteria.robot_scenario}%' and TypKlienta like '%{criteria.client}%' and StatusRobota like '%Zatwierdzono%'")
    row = cursor.fetchone()
    if row[0] > 0:
        return True
    return False

@db_exceptions_handler()
def db_log(msg):
    dt = datetime.now()
    print(dt, msg)
    # pyautogui.FAILSAFE = False
    # pyautogui.press('scrolllock')
    # cursor, conn = connect()
    # cursor.execute('''insert into dbo.log_1p (entry, date) values(?, ?)''', msg[:200], dt)
    # conn.commit()
    return True

@db_exceptions_handler()
def db_log_delete():
    dt = datetime.now() + timedelta(days=-5)
    cursor, conn = connect()
    cursor.execute('''delete from dbo.log_1p where date < ?''', dt)
    conn.commit()
    return True

if __name__ == "__main__":
    print("db")