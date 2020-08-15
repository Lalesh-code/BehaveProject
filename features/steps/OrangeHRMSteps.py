from behave import *
from selenium import webdriver

@given('Launch Chrome browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome(r"C:\Users\Admin\PycharmProjects\Lalesh_Python\Drivers\chromedriver.exe")

@when('open OrangeHRM home page')
def OpenHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('verify that the logo is present on the page')
def VerifyLogo(context):
    status=context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True

@then('close browser')
def CloseBrowser(context):
    context.driver.close()

