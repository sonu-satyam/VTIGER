from Library.Lib import SeleniumWrapper

class Login:

    def __init__(self,driver):
        self.driver = driver

    def login(self):
        a = SeleniumWrapper(self.driver)
        a.send_data(("name","user_name"),"admin")
        a.send_data(("name","user_password"),"admin")
        a.click_element(("id","submitButton"))
