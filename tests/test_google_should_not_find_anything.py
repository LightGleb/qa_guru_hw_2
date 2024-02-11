from selene import browser, be, have


def test_google_should_not_find_anything():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('erfjrjajwnewg').press_enter()
    browser.element('[id="search"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))
