from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    UnexpectedAlertPresentException,
    JavascriptException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    ElementNotVisibleException,
    ElementNotSelectableException,
    InvalidElementStateException,
    NoSuchWindowException,
    MoveTargetOutOfBoundsException)
from projekt.services import db, ex, variables, win

# decorator function in case xpath exception
def xpath_exception_handler(timeout=120):
    def checker(func):
        def wrapper(*args):
            counter = True
            fn = f"{func.__name__}, {args}"
            start_time = datetime.now().timestamp()
            while datetime.now().timestamp() - start_time < timeout:
                try:
                    return func(*args)
                except TimeoutException:
                    if counter:
                        db.db_log("WARNING, timeout exception for " + fn)
                except NoSuchElementException:
                    if counter:
                        db.db_log("WARNING, no element exception for " + fn)
                except UnexpectedAlertPresentException as alert:
                    if counter:
                        db.db_log("WARNING, unexpected alert exception for " + fn)
                        db.db_log(f"WARNING, alert: {alert.alert_text}")
                except JavascriptException:
                    if counter:
                        db.db_log("WARNING, JavaScript exception for " + fn)
                except StaleElementReferenceException:
                    if counter:
                        db.db_log("WARNING, stale element exception for " + fn)
                except ElementNotInteractableException:
                    if counter:
                        db.db_log("WARNING, not interactable element exception for " + fn)
                except ElementNotVisibleException:
                    if counter:
                        db.db_log("WARNING, element not visible exception for " + fn)
                except ElementNotSelectableException:
                    if counter:
                        db.db_log("WARNING, element not selectable exception for " + fn)
                except InvalidElementStateException:
                    if counter:
                        db.db_log("WARNING, invalid element state exception for " + fn)
                except NoSuchWindowException:
                    if counter:
                        db.db_log("WARNING, no such window exception for " + fn)
                except MoveTargetOutOfBoundsException:
                    if counter:
                        db.db_log("WARNING, target out of bounds exception for " + fn)
                if counter:
                    counter = False
            if timeout > 1:
                db.db_log("WARNING, process timeout for " + fn)
                raise xpathException(ex.EXCEPT_TIMEOUT)
        return wrapper
    return checker

def display_func_name(fun):
    def wrapper(*args):
        db.db_log(f"INFO, {fun.__name__}, {args[1:]}")
        return fun(*args)
    return wrapper

class xpathException(Exception):
    id: int

    def __init__(self, id=0):
        super().__init__()
        self.id = id
        db.db_log(ex.getWarning(self.id))

class Sel(win.Win):

    def __init__(self):
        pass

    def open(self, page):
        self.driver = webdriver.Firefox()
        self.driver.get(page)

    def close(self):
        self.driver.quit()

    @display_func_name
    def locate_and_count_repeater(self, xpath, id=0):

        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True

        @xpath_exception_handler(1)
        def step2(xpath):
            return len(self.driver.find_elements(By.XPATH, xpath))

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step1(xpath):
                return step2(xpath)
        raise xpathException(id)

    @display_func_name
    def locate_and_click_xpath_repeater(self, xpath, id=0):
        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return True

        @xpath_exception_handler(1)
        def step2(xpath):
            self.driver.find_element(By.XPATH, xpath).click()
            return True

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step1(xpath):
                if step2(xpath):
                    return True
        raise xpathException(id)

    @display_func_name
    def locate_and_get_xpaths_repeater(self, xpath, id=0):
        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return True
        @xpath_exception_handler(1)
        def step2(element):
            return self.driver.find_elements(By.XPATH, xpath)

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step1(xpath):
                return step2(xpath)
        raise xpathException(id)

    @xpath_exception_handler(1)
    @display_func_name
    def locate_xpath(self, xpath):
        WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
        WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return True

if __name__ == "__main__":
    print("sel library")
    a = ()
    for i in a:
        print(i)