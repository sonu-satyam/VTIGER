from Library.Lib import SeleniumWrapper

class AddOrg:
    def __init__(self,driver):
        self.driver = driver

    def addorg(self):
        a = SeleniumWrapper(self.driver)

        a.click_element(("xpath","(//a[text()='Organizations'])[1]"))
        a.click_element(("xpath", "//img[@title='Create Organization...']"))
        a.send_data(("xpath", "//input[@name='accountname']"),"Tysss")
        a.dropdown(("xpath","//select[@name='assigned_user_id']"),"Bill Gates")
        a.click_element(("xpath", "(//input[@name='button'])[3]"))