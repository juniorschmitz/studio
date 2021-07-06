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
