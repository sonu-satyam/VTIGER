from POM.addleads import AddLead
from POM.login import Login

def test_addlead(driver_):
    l = Login(driver_)
    l.login()
    al = AddLead(driver_)
    al.add_lead()