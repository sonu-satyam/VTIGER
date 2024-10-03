from Library.Lib import SeleniumWrapper

class AddLead:
    def __init__(self,driver):
        self.driver = driver

    def add_lead(self):
        a= SeleniumWrapper(self.driver)
        a.click_element(("xpath", "(//a[text()='Leads'])[1]"))
        a.click_element(("xpath", "//img[@title='Create Lead...']"))
        a.send_data(("xpath","//input[@name='lastname']"),"sam")
        a.send_data(("xpath", "//input[@name='company']"),"cognigant")
        a.dropdown(("xpath","//select[@name='assigned_user_id']"),"Hello World")
        a.click_element(("xpath","(//input[@name='button'])[3]"))