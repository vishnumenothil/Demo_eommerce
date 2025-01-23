from pytest import mark
from pom.registrationpage import registration
from pom.homepage import Homepage
from utility.excel import read_headers
from utility.excel import read_data

headers=read_headers("test_registration","smoke")
data=read_data("test_registration","smoke") 
print(headers)
print(data)
@mark.parametrize(headers,data)
def test_register(setup_tear_down,_config,request,gender,fname,lname,email,password,confirmpassword):
#    usig pagemaker
    robj=registration(setup_tear_down)
    hompage=Homepage(setup_tear_down)
    hompage.register()
    robj.register(gender,fname,lname,email,password,confirmpassword)
    
   
   
@mark.parametrize(headers,data)
def test_negative_register(setup_tear_down,_config,request,gender,fname,lname,email,password,confirmpassword):
    robj=registration(setup_tear_down)
    hompage=Homepage(setup_tear_down)
    hompage.register()
    robj.register(gender,fname,lname,email,password,confirmpassword)