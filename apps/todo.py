import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://vanilton.net/web-test/todos/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("anne")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("teste")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.locator("li").filter(has_text="anne").get_by_role("checkbox").check()
    page.locator("li").filter(has_text="teste").get_by_role("checkbox").check()
    page.get_by_role("button", name="Clear completed").click()
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("att")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.locator("li").filter(has_text="att").get_by_role("checkbox").check()
    page.get_by_role("link", name="Active").click()
    page.get_by_role("button", name="Clear completed").click()

    # ---------------------
    context.close()
    browser.close()