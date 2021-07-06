Feature: FakeEcommercePoc
    As Mario, the user
    I would like to search for buying clothes
    For not freeze

  Scenario: Search for valid product
    Given Mario is on the Homepage
    When Mario searches for "dress"
    Then Mario should see search results

  Scenario: Search for invalid product
    Given Mario is on the Homepage
    When Mario searches for "potato"
    Then Mario should not see search results
