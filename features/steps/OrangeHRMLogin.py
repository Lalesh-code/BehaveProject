from behave import *
from selenium import webdriver

@given('I launch a Chrome browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome(r"C:\Users\Admin\PycharmProjects\Lalesh_Python\Drivers\chromedriver.exe")

@when('I open a OrangeHRM home page')
def OpenOrangeHRM(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@when('enter a Username "{User}" and Password "{PWD}"')
def UserPWD(context,User,PWD):
    context.driver.find_element_by_id("txtUsername").send_keys(User)
    context.driver.find_element_by_id("txtPassword").send_keys(PWD)

@when('click on the login button')
def LoginButton(context):
    context.driver.find_element_by_id("btnLogin").click()

# @then('User must successfully login to Dashboard page')
# def DashboardSuccess(context):
#     text=context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
#     assert text=="Dashboard"
#     context.driver.close()

@then('User must successfully login to Dashboard page')
def DashboardSuccess(context):
    try:
        text=context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Test failed"
    if text=="Dashboard":
       context.driver.close()
       assert True, "Test Success"
