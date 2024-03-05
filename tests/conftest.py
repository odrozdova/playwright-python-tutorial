import pytest

from pages.result_page import DuckDuckGoResultPage
from pages.search_page import DuckDuckGoSearchPage
from playwright.sync_api import Page


@pytest.fixture
def result_page(page: Page) -> DuckDuckGoResultPage:
    return DuckDuckGoResultPage(page)


@pytest.fixture
def search_page(page: Page) -> DuckDuckGoSearchPage:
    return DuckDuckGoSearchPage(page)