from datetime import datetime

from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    NoSuchFrameException,
    NoSuchWindowException,
    UnexpectedAlertPresentException,
    JavascriptException,
    StaleElementReferenceException,
    ElementNotInteractableException)
from projekt.services import db, ex


# custom exception for screen element
class xpathException(Exception):
    id:int
    def __init__(self, id = 0):
        super().__init__()
        self.id = id
        db.db_log(ex.getWarning(self.id))

# decorator function in case window exception
def window_exception_handler(timeout=120):
    def checker(func):
        def wrapper(*args):
            counter = True
            fn = f"{func.__name__} with: {args[1:]}"
            start_time = datetime.now().timestamp()
            while datetime.now().timestamp() - start_time < timeout:
                try:
                    return func(*args)
                except TimeoutException:
                    if counter:
                        db.db_log("WARNING, timeout exception for " + fn)
                except NoSuchElementException:
                    if counter:
                        db.db_log("WARNING, no such element exception for " + fn)
                except NoSuchFrameException:
                    if counter:
                        db.db_log("WARNING, no such frame exception for " + fn)
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
                except NoSuchWindowException:
                    if counter:
                        db.db_log("WARNING, no such window exception for " + fn)
                if counter:
                    counter = False
            db.db_log("WARNING, timeout exception for " + fn)
            raise xpathException(ex.EXCEPT_TIMEOUT)
        return wrapper
    return checker

class Win:

    driver = None

    # display
    def display_info(self):
        print("*******************************")
        print("Actual tab title: ", self.driver.title)
        print("Tab handles: ", self.driver.window_handles)
        print("Actual tab: ", self.driver.current_window_handle)
        print("*******************************")

    @window_exception_handler(1)
    def maximize(self):
        self.driver.maximize_window()
        return True

    @window_exception_handler()
    def handler_initialize(self, handlers, context = "None"):
        self.select_context(context)
        handlers[self.driver.current_window_handle] = self.driver.title
        db.db_log(f"INFO, window registration: {self.driver.title}, {self.driver.current_window_handle}")
        return True

    @window_exception_handler()
    def check_window_exists(self, window:str):
        actual_window = self.driver.current_window_handle
        target_found = False
        for id in self.driver.window_handles:
            self.driver.switch_to.window(id)
            if self.driver.title == window:
                target_found = True
                break
        self.driver.switch_to.window(actual_window)
        return target_found

    @window_exception_handler()
    def handler_select(self, handlers, new_window:str, context="None"):
        for id in self.driver.window_handles:
            if id not in handlers.keys():
                self.driver.switch_to.window(id)
                if self.driver.title == new_window:
                    handlers[id] = self.driver.title
                    self.select_context(context)
                    db.db_log(f"INFO, switched to window: {self.driver.title}")
                    self.maximize()
                    return True
            else:
                if handlers[id] == new_window:
                    self.driver.switch_to.window(id)
                    self.select_context(context)
                    db.db_log(f"INFO, switched to window: {self.driver.title}")
                    self.maximize()
                    return True
                else:
                    self.driver.switch_to.window(id)
                    handlers[id] = self.driver.title
                    if handlers[id] == new_window:
                        self.select_context(context)
                        db.db_log(f"INFO, switched to window: {self.driver.title}")
                        self.maximize()
                        return True
        return False

    @window_exception_handler()
    def handler_close(self):
        for id in self.driver.window_handles:
            self.driver.switch_to.window(id)
            db.db_log(f"INFO, closed window: {self.driver.title}")
            self.driver.close()
        self.driver.quit()
        return True

    @window_exception_handler()
    def select_context(self, context="None"):
        self.maximize()
        if context == "None":
            self.driver.switch_to.default_content()
            db.db_log("INFO, window context set to default")
        else:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(context)
            db.db_log(f"INFO, window context set to {context}")
        return True

    @window_exception_handler()
    def window_close(self, handlers, window_to_close:str):
        for (k, v) in handlers.items():
            if v == window_to_close:
                self.driver.switch_to.window(k)
                db.db_log(f"INFO, closed window: {self.driver.title}")
                self.driver.close()
                del handlers[k]
                return True
        return False

if __name__ == "__main__":
    print("scenario")