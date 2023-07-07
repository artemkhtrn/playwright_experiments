import re
from playwright.sync_api import Page, expect


def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page.get_by_role("link", name="Get started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro"))


def test_login(page: Page):
    # launch browserstack demo
    page.goto("https://bstackdemo.com/")
    # click on sign button
    page.click('#signin')
    # select Username
    page.get_by_text("Select Username").click()
    page.locator("#react-select-2-option-0-0").click()
    # select Password
    page.get_by_text("Select Password").click()
    page.locator("#react-select-3-option-0-0").click()
    # click login
    page.get_by_role("button", name="Log In").click()
    # verify user have logged in
    assert page.get_by_text("demouser").is_visible()


def test_add_to_cart(page: Page):
    # launch browser
    page.goto("https://bstackdemo.com/")
    page.locator("[id=\"\\31 \"]").get_by_text("Add to cart").click()
    assert page.locator(".float-cart.float-cart--open").is_visible()
    expect(page.locator('.sub-price__val')).to_have_text('$ 799.00')
