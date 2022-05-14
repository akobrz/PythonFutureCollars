from datetime import datetime
from time import sleep
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
from selenium.webdriver.support.ui import Select
from projekt.hunter import db, ex, variables, win

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
    def click_and_wait_xpath_repeater(self, xpath_click, xpath_target, id=0):
        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.driver.find_element_by_xpath(xpath).click()
            return True
        @xpath_exception_handler(1)
        def step2(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            step1(xpath_click)
            if step2(xpath_target):
                return
        raise xpathException(id)

    @display_func_name
    def click_and_wait_select_list_repeater(self, xpath_click, xpath_target, text, id=0):
        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.driver.find_element_by_xpath(xpath_click).click()
            return True
        @xpath_exception_handler(1)
        def step2(xpath, text):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            select = Select(self.driver.find_element_by_xpath(xpath))
            if select.first_selected_option.text == text:
                return True
            return False

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if int(datetime.now().timestamp() - start_time) % 2 == 0:
                step1(xpath_click)
            if step2(xpath_target, text):
                return
        raise xpathException(id)

    @display_func_name
    def refresh_and_wait_xpath_repeater(self, xpath_target, id=0):
        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if int(datetime.now().timestamp() - start_time) % 2 == 0:
                self.driver.refresh()
            if step1(xpath_target):
                return
        raise xpathException(id)

    @display_func_name
    def click_and_wait_documents_repeater(self, xpath_click, xpath_target, id=0):
        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.driver.find_element_by_xpath(xpath_click).click()
            return True
        @xpath_exception_handler(1)
        def step2(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            step1(xpath_click)
            if step2(xpath_target):
                return
            sleep(variables.WAIT_SEC_10)
        raise xpathException(id)

    @display_func_name
    def click_and_wait_xpaths_repeater(self, xpath_click, xpath_table, id=0):
        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.driver.find_element_by_xpath(xpath_click).click()
            return True
        @xpath_exception_handler(1)
        def step2(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True
        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if int(datetime.now().timestamp() - start_time) % 2 == 0:
                step1(xpath_click)
            for i, xpath in enumerate(xpath_table):
                if step2(xpath):
                    return xpath
        raise xpathException(id)

    @display_func_name
    def send_text_and_check_repeater(self, xpath, text, id=0):
        @xpath_exception_handler(1)
        def step1(xpath, text):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            if self.driver.find_element_by_xpath(xpath).get_attribute("value") != "":
                self.driver.find_element_by_xpath(xpath).clear()
            self.driver.find_element_by_xpath(xpath).click()
            self.driver.find_element_by_xpath(xpath).send_keys(text)
        @xpath_exception_handler(1)
        def step2(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).get_attribute("value")
        @xpath_exception_handler(1)
        def step3(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).get_attribute("disabled")

        current_time = datetime.now().timestamp()
        while datetime.now().timestamp() - current_time < variables.WAIT_SEC_120:
            if step3(xpath) == "true":
                return True
            if step2(xpath) == text:
                return True
            step1(xpath, text)
            if step2(xpath) == text:
                return True
            sleep(variables.WAIT_SEC_2)
        raise xpathException(id)

    @display_func_name
    def send_pass_and_check_repeater(self, xpath_send, text, id=0):
        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            if self.driver.find_element_by_xpath(xpath).get_attribute("value") != "":
                self.driver.find_element_by_xpath(xpath).clear()
            self.driver.find_element_by_xpath(xpath).click()
            self.driver.find_element_by_xpath(xpath).send_keys(text)
        @xpath_exception_handler(1)
        def step2(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).get_attribute("value")

        current_time = datetime.now().timestamp()
        while datetime.now().timestamp() - current_time < variables.WAIT_SEC_120:
            if step2(xpath_send) == text:
                return True
            step1(xpath_send)
            if step2(xpath_send) == text:
                return True
            sleep(variables.WAIT_SEC_2)
        raise xpathException(id)

    @display_func_name
    def select_list_and_check_repeater(self, xpath, text, id=0):
        @xpath_exception_handler(1)
        def step1(xpath, text):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            select = Select(self.driver.find_element_by_xpath(xpath))
            select.select_by_visible_text(text)
        @xpath_exception_handler(1)
        def step2(xpath, text):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            select = Select(self.driver.find_element_by_xpath(xpath))
            if select.first_selected_option.text == text:
                return True
            return False
        @xpath_exception_handler(1)
        def step3(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).get_attribute("disabled")

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step3(xpath) == "true":
                return True
            if step2(xpath, text):
                return True
            step1(xpath, text)
            if step2(xpath, text):
                return True
            sleep(variables.WAIT_SEC_2)
        raise xpathException(id)

    @display_func_name
    def click_checkbox_and_check_repeater(self, xpath, id=0):
        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.driver.find_element_by_xpath(xpath).click()
            return True
        @xpath_exception_handler(1)
        def step2(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).get_attribute("CHECKED")
        @xpath_exception_handler(1)
        def step3(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).get_attribute("disabled")

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step3(xpath) == "true" and step2(xpath) == "true":
                return True
            if step3(xpath) == "true":
                xpathException(ex.EXCEPT_CHECKBOX_DISABLED)
            if step2(xpath) == "true":
                return True
            step1(xpath)
            if step2(xpath) == "true":
                return True
        raise xpathException(id)

    @display_func_name
    def click_checkbox_and_unclick_other_repeater(self, xpath_to_click, xpath_to_unclick, id=0):
        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.driver.find_element_by_xpath(xpath).click()
            return True
        @xpath_exception_handler(1)
        def step2(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).get_attribute("CHECKED")
        @xpath_exception_handler(1)
        def step3(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).get_attribute("disabled")

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step3(xpath_to_click) == "true":
                if step3(xpath_to_unclick) == "true":
                    xpathException(ex.EXCEPT_CHECKBOX_DISABLED)
                if step2(xpath_to_unclick) == "true":
                    step1(xpath_to_unclick)
            if step2(xpath_to_click) == "true":
                return True
            else:
                step1(xpath_to_click)
            sleep(variables.WAIT_SEC_2)
        raise xpathException(id)

    @display_func_name
    def unclick_checkbox_and_check_repeater(self, xpath, id=0):
        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.driver.find_element_by_xpath(xpath).click()
            return True
        @xpath_exception_handler(1)
        def step2(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).get_attribute("CHECKED")
        @xpath_exception_handler(1)
        def step3(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).get_attribute("disabled")
        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step3(xpath) == "true" and step2(xpath) != "true":
                return True
            if step3(xpath) == "true":
                raise xpathException(ex.EXCEPT_CHECKBOX_DISABLED)
            if step2(xpath) != "true":
                return True
            step1(xpath)
            if step2(xpath) != "true":
                return True
        raise xpathException(id)

    @display_func_name
    def click_and_wait_window_repeater(self, xpath, window, id=0):

        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.driver.find_element_by_xpath(xpath).click()
            return True

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            step1(xpath)
            if self.check_window_exists(window):
                return True
            sleep(variables.WAIT_SEC_2)
        raise xpathException(id)

    @display_func_name
    def click_and_close_alert_repeater(self, xpath_click, alert_action, id=0):

        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.driver.find_element_by_xpath(xpath_click).click()

        @xpath_exception_handler(1)
        def step2(alert_action):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.alert_is_present())
            if alert_action == "accept":
                self.driver.switch_to.alert.accept()
            else:
                self.driver.switch_to.alert.dismiss()
            return True

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            step1(xpath_click)
            if step2(alert_action):
                return True
            sleep(variables.WAIT_SEC_2)
        raise xpathException(id)

    @display_func_name
    def locate_xpaths_repeater(self, xpaths, id=0):

        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            for i, xpath in enumerate(xpaths):
                if step1(xpath):
                    return xpath
        raise xpathException(id)

    @display_func_name
    def locate_xpath_repeater(self, xpath, id=0):

        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step1(xpath):
                return 0
        raise xpathException(id)

    @display_func_name
    def locate_and_locate_xpath_repeater(self, xpath1, xpath2, id=0):

        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step1(xpath1):
                if step1(xpath2):
                    return True
                else:
                    return False
        raise xpathException(id)

    @display_func_name
    def click_radio_and_check_repeater(self, xpath, id=0):

        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.driver.find_element_by_xpath(xpath).click()
            return True

        @xpath_exception_handler(1)
        def step2(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).get_attribute("CHECKED")

        @xpath_exception_handler(1)
        def step3(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).get_attribute("disabled")

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step2(xpath) == "true":
                return True
            if step3(xpath) == "true":
                raise xpathException(ex.EXCEPT_CHECKBOX_DISABLED)
            step1(xpath)
            if step2(xpath) == "true":
                return True
            sleep(variables.WAIT_SEC_2)
        raise xpathException(id)

    @display_func_name
    def locate_and_get_attribute_repeater(self, xpath, attribute, id=0):

        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True

        @xpath_exception_handler(1)
        def step2(xpath, attribute):
            return self.driver.find_element_by_xpath(xpath).get_attribute(attribute)

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step1(xpath):
                return step2(xpath, attribute)
        raise xpathException(id)

    @display_func_name
    def locate_and_get_text_repeater(self, xpath, id=0):

        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True

        @xpath_exception_handler(1)
        def step2(xpath):
            return self.driver.find_element_by_xpath(xpath).text

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step1(xpath):
                return step2(xpath)
        raise xpathException(id)

    @display_func_name
    def locate_and_count_repeater(self, xpath, id=0):

        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True

        @xpath_exception_handler(1)
        def step2(xpath):
            return len(self.driver.find_elements_by_xpath(xpath))

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
            self.driver.find_element_by_xpath(xpath).click()
            return True

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step1(xpath):
                if step2(xpath):
                    return True
        raise xpathException(id)

    @display_func_name
    def locate_and_get_select_repeater(self, xpath, id=0):
        @xpath_exception_handler(1)
        def step1(xpath):
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return True
        @xpath_exception_handler(1)
        def step2(xpath):
            select = Select(self.driver.find_element_by_xpath(xpath))
            return select.first_selected_option.text

        start_time = datetime.now().timestamp()
        while datetime.now().timestamp() - start_time < variables.WAIT_SEC_120:
            if step1(xpath):
                return step2(xpath)
        raise xpathException(id)

    @display_func_name
    def locate_xpaths_and_click_repeater(self, xpath, id=0):
        @xpath_exception_handler(1)
        def step1(xpath):
            return self.driver.find_elements_by_xpath(xpath)
        @xpath_exception_handler(1)
        def step2(element):
            element.click()

        for element in step1(xpath):
            step2(element)
        return True

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

    @display_func_name
    def locate_checked_and_uncheck_repeater(self, id=0):
        @xpath_exception_handler(1)
        def step1():
            return self.driver.find_elements_by_xpath("//input[@type='checkbox' and @value='on']")

        for x in step1():
            if x.get_attribute("CHECKED") == "true":
                x.click()
        return True

    # others:

    @xpath_exception_handler(1)
    @display_func_name
    def locate_xpath(self, xpath):
        WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.presence_of_element_located((By.XPATH, xpath)))
        WebDriverWait(self.driver, variables.WAIT_SEC_2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return True

    @xpath_exception_handler(1)
    @display_func_name
    def execute_js(self, script):
        return self.driver.execute_script(script)

    @display_func_name
    def check_is_disabled(self, xpath, id=0):
        ret = self.locate_and_get_attribute_repeater(xpath, "disabled", id)
        if ret == "true":
            return True
        else:
            return False

    @display_func_name
    def check_is_checked(self, xpath, id=0):
        ret = self.locate_and_get_attribute_repeater(xpath, "CHECKED", id)
        if ret == "true":
            return True
        else:
            return False

if __name__ == "__main__":
    print("sel library")
    a = ()
    for i in a:
        print(i)