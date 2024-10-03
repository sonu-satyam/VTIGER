from POM.addorg import AddOrg
from POM.login import Login

def test_addorg(driver_):
    l = Login(driver_)
    l.login()
    ad_ = AddOrg(driver_)
    ad_.addorg()
