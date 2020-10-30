from dash.testing.application_runners import import_app

# example of css selector for future,
# dash_duo.find_elements("div[attr='value']")

# css selector to search by text is not supported in selenium, hence use xpath

def test_main_headers(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app, port=8000, host="0.0.0.0")
    dash_duo.wait_for_element("#logo", timeout=10)

    header_pattern = ("//span[contains(@class, 'column-header-name') "
                      "and contains(text(), '{}')]")

    # checking for default table headers seems to be stable enough for now
    titles = dash_duo.driver.find_elements_by_xpath(header_pattern.format("title"))
    assert len(titles) == 1

    users = dash_duo.driver.find_elements_by_xpath(header_pattern.format("user"))
    assert len(users) == 1
