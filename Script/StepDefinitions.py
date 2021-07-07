@given("Mario is on the Homepage")
def step_impl():
  browserWindow = Aliases.browser.BrowserWindow
  Browsers.Item[btChrome].Navigate("http://automationpractice.com/index.php")
  browserWindow.Maximize()
  aqObject.CheckProperty(Aliases.browser.pageMyStore.header.formSearchbox.textboxSearchQueryTop, "Exists", cmpEqual, True)

@when("Mario searches for {arg}")
def step_impl(search_term):
  browser = Aliases.browser
  textbox = browser.pageMyStore.header.formSearchbox
  textbox2 = textbox.textboxSearchQueryTop
  textbox2.Click()
  textbox2.SetText(search_term)
  textbox.buttonSearch.ClickButton()

@then("Mario should see search results")
def step_impl():
  aqObject.CheckProperty(Aliases.browser.pageIndex.textnode.textnodeQuickView289830515Printe, "Exists", cmpEqual, True)

@then("Mario should not see search results")
def step_impl():
  aqObject.CheckProperty(Aliases.browser.pageIndex.textnodeNoResultsWereFoundForYou, "contentText", cmpContains, "No results were found for your search")

@given("the hacker is on the Login Page")
def step_impl():
  browser = Aliases.browser
  browser.BrowserWindow.Maximize()
  page = browser.pageIndex
  page.header.linkSignIn.Click()
  page.Wait()
  aqObject.CheckProperty(Aliases.browser.pageIndex.formLoginForm.textboxEmailAddress, "Exists", cmpEqual, True)

@when("the hacker tries to login with email {arg} and password {arg}")
def step_impl(email, password):
  browser = Aliases.browser
  browser.BrowserWindow.Maximize()
  textbox = browser.pageIndex.formLoginForm
  textbox2 = textbox.textboxEmailAddress
  textbox2.Click()
  textbox2.SetText(email)
  passwordBox = textbox.passwordboxPassword
  passwordBox.Keys("[Tab]")
  passwordBox.SetText(password)
  textbox.buttonSignIn.ClickButton()

@then("the hacker should not be able to login")
def step_impl():
  aqObject.CheckProperty(Aliases.browser.pageIndex.textnodeAuthenticationFailed, "Exists", cmpEqual, True)
