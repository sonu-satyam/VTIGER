from POM.login import Login
from Library.Lib import SeleniumWrapper

def test_login(driver_):
    a = SeleniumWrapper(driver_)
    l = Login(driver_)
    l.login()