from behave import *


@given('Open a Chrome browser')
def launchbrowser(context):
    assert True, "Test passed"


@when('Hit OrangeHRM home page')
def openorangehrm(context):
    assert True, "Test passed"


@when('Put a Username and Password')
def userpassword(context):
    assert True, "Test passed"


@when('Hit the login button')
def loginbutton(context):
    assert True, "Test passed"


@then('User able to successfully login to Dashboard page')
def dashboard(context):
    assert True, "Test passed"


@when('navigate to Search page')
def search(context):
    assert True, "Test passed"


@then('Search page should be displayed')
def searchpage(context):
    assert True, "Test passed"


@when('navigate to Advance Search page')
def advsearch(context):
    assert True, "Test passed"


@then('Advanced Search page should be displayed')
def advancepage(context):
    assert True, "Test passed"
