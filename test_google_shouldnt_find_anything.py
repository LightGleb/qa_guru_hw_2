from selene import browser, be, have


def test_google_shouldnt_find_anything(open_browser):
    browser.element('[name="q"]').should(be.blank).type('erfjrjajwnewg').press_enter()
    browser.element('[id="search"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))
