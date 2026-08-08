"""Page Object Model for basic Google Maps browser automation.

Sprint 2.1 only verifies that Playwright can open Google Maps, submit one
keyword, wait until search results appear, and close the browser safely. This
module intentionally does not scrape, scroll, parse, or export data.
"""

from __future__ import annotations

import logging
import time
from urllib.parse import quote_plus

from playwright.sync_api import Browser, BrowserContext, Page, Playwright, TimeoutError, sync_playwright

from config import HEADLESS, SEARCH_DELAY, TIMEOUT, USER_AGENT

logger = logging.getLogger(__name__)


class GoogleMapsPage:
    """Page object responsible only for interactions with Google Maps."""

    def __init__(self) -> None:
        """Initialize empty Playwright resources before the browser is opened."""

        self._playwright: Playwright | None = None
        self._browser: Browser | None = None
        self._context: BrowserContext | None = None
        self._page: Page | None = None

    def open(self) -> None:
        """Open Google Maps in Chromium using the project configuration."""

        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(headless=HEADLESS)
        self._context = self._browser.new_context(user_agent=USER_AGENT, locale="id-ID")
        self._page = self._context.new_page()
        self._page.set_default_timeout(TIMEOUT)
        self._page.goto("https://www.google.com/maps", wait_until="domcontentloaded")
        self._page.wait_for_load_state("load")

    def search(self, keyword: str) -> None:
        """Type a keyword into Google Maps search box and submit it.

        Args:
            keyword: Search keyword that will be entered into Google Maps.
        """

        if self._page is None:
            raise RuntimeError("Google Maps page must be opened before searching.")

        search_box_selectors = [
            "#searchboxinput",
            'input[aria-label*="Search"]',
            'input[aria-label*="Telusuri"]',
            'input[placeholder*="Search"]',
            'input[placeholder*="Telusuri"]',
        ]

        for selector in search_box_selectors:
            search_box = self._page.locator(selector).first
            try:
                search_box.wait_for(state="visible", timeout=5_000)
                search_box.fill(keyword)
                search_box.press("Enter")
                time.sleep(SEARCH_DELAY)
                return
            except TimeoutError:
                logger.debug("Search box selector not found: %s", selector)

        logger.warning("Search box not found; using direct Google Maps search URL fallback.")
        search_url = f"https://www.google.com/maps/search/{quote_plus(keyword)}?hl=id"
        self._page.goto(search_url, wait_until="domcontentloaded")
        self._page.wait_for_load_state("load")
        time.sleep(SEARCH_DELAY)

    def wait_search_result(self) -> None:
        """Wait until Google Maps displays search results for the submitted keyword."""

        if self._page is None:
            raise RuntimeError("Google Maps page must be opened before waiting for results.")

        self._page.wait_for_url("**/maps/search/**", wait_until="domcontentloaded")
        result_selectors = (
            '[role="feed"], '
            '[aria-label*="Results for"], '
            '[aria-label*="Hasil untuk"], '
            'a[href*="/maps/place/"], '
            'div[role="main"]'
        )
        self._page.locator(result_selectors).first.wait_for(state="visible")

    def close(self) -> None:
        """Close Playwright resources safely if they were created."""

        if self._context is not None:
            self._context.close()
            self._context = None
        if self._browser is not None:
            self._browser.close()
            self._browser = None
        if self._playwright is not None:
            self._playwright.stop()
            self._playwright = None
        self._page = None
