from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def wait_(some_func):
    def wrapper(*args,**kwargs):
        instance = args[0]
        locator = args[1]
        w = WebDriverWait(instance.driver,15)
        w.until(ec.presence_of_element_located(locator))
        return some_func(*args,**kwargs)
    return wrapper


class SeleniumWrapper:

    def __init__(self,driver):
        self.driver = driver

    @wait_
    def click_element(self,locator):
        self.driver.find_element(*locator).click()

    @wait_
    def send_data(self,locator,data):
        self.driver.find_element(*locator).send_keys(data)

    @wait_
    def dropdown(self,locator,data):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(data)



    def alert_accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def alert_dismiss(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def windows_handle(self,n):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[n])

    @wait_
    def drag_drop(self,source_locator,target_locator):
        source_element = self.driver.find_element(*source_locator)
        target_element = self.driver.find_element(*target_locator)
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element,target_element)

    def screenshot(self):
        self.driver.save_screentshot("screenshot.png")

    @wait_
    def mouse_hover(self,locator):
        element = self.driver.find_element(*locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    @wait_
    def right_click(self,locator):
        element = self.driver.find_element(*locator)
        action = ActionChains(element)
        action.context_click(element).perform()

    @wait_
    def double_click(self,locator):
        element = self.driver.find_element(*locator)
        action = ActionChains(element)
        action.double_click(element).perform()

    @wait_
    def iframe(self,locator):
        element = self.driver.find_element(*locator)
        self.driver.switch_to.frame(element)

    def iframe_default(self):
        self.driver.switch_to.default_content()





