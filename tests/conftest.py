import pytest
import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.product_price_page import ProductPrice
from pathlib import Path
import allure


ALLURE_SCREENSHOTS_DIR = Path("allure-results/screenshots")
ALLURE_SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

# Load .env configs
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://example.com")


@pytest.fixture(scope="session")
def user_cred():
    return  {
        "username": os.getenv("TEST_USERNAME", "standard_user"),
        "password": os.getenv("TEST_PASSWORD", "secret_password"),
    }

@pytest.fixture(scope="session")
def browser():
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()

@pytest.fixture
def page(browser, base_url):
    context = browser.new_context(base_url=base_url)
    page = context.new_page()
    yield page
    context.close()

# Page object fixtures
@pytest.fixture
def login_page(page):
    return LoginPage(page)    

@pytest.fixture
def product_price_page(page):
    return ProductPrice(page)