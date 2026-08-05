"""Data model and scraper template for future Google Maps automation.

No scraping logic is implemented in this Sprint 1.5 foundation. The module only
prepares the final dataset model and extension points required before Sprint 2.
"""

from __future__ import annotations

import logging
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any

from scraper.google_maps_page import GoogleMapsPage

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class BusinessRecord:
    """Final dataset model for one Prabumulih business record.

    The fields mirror the columns expected in the CSV/Excel output. Google Maps
    is planned as the primary source, while Google Search verification can fill
    digital-channel fields such as Instagram, Facebook, TikTok, Shopee, and
    Tokopedia. The model remains a dataclass so records are explicit, typed, and
    easier to validate than plain dictionaries.
    """

    nama_usaha: str | None = None
    kategori: str | None = None
    alamat: str | None = None
    nomor_telepon: str | None = None
    website: str | None = None
    rating: float | None = None
    jumlah_review: int | None = None
    google_maps_url: str | None = None
    instagram: str | None = None
    facebook: str | None = None
    tiktok: str | None = None
    shopee: str | None = None
    tokopedia: str | None = None
    digital_channel: str | None = None
    keyword_pencarian: str | None = None
    waktu_scraping: datetime | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert the dataclass record to a dictionary for Pandas export."""

        return asdict(self)


class MapsScraper:
    """Coordinator for the Sprint 2.1 Google Maps browser automation check."""

    def __init__(self, google_maps_page: GoogleMapsPage | None = None) -> None:
        """Initialize the scraper coordinator with a Google Maps page object.

        Args:
            google_maps_page: Optional page object used to interact with Google Maps.
        """

        self.google_maps_page = google_maps_page or GoogleMapsPage()

    def start(self, keyword: str) -> None:
        """Run a single-keyword Google Maps search validation.

        Args:
            keyword: Search keyword that will be submitted to Google Maps.
        """

        self.start_keywords([keyword])

    def start_keywords(self, keywords: list[str]) -> None:
        """Run the Sprint 2.2 multi-keyword validation without scraping data.

        Args:
            keywords: Search keywords that will be submitted to Google Maps one by one.
        """

        try:
            logger.info("Open Google Maps")
            self.google_maps_page.open()
            for keyword in keywords:
                logger.info("Searching keyword: %s", keyword)
                self.google_maps_page.search(keyword)
                self.google_maps_page.wait_search_result()
                logger.info("Search Success: %s", keyword)
        except Exception:
            logger.exception("Google Maps automation failed.")
            raise
        finally:
            self.google_maps_page.close()

    def scrape(self, keyword: str, location: str) -> list[BusinessRecord]:
        """Keep a future-compatible scraping entry point without collecting data.

        Args:
            keyword: Search keyword to be used by the future Google Maps scraper.
            location: Target city or area.

        Returns:
            An empty list because Sprint 2.1 does not scrape data.
        """

        logger.info("Scrape placeholder called for keyword='%s', location='%s'.", keyword, location)
        return []

    def parse_business_card(self, raw_item: Any) -> BusinessRecord:
        """Return a blank record because parsing is outside Sprint 2.1 scope.

        Args:
            raw_item: Reserved for a future Playwright selector or response.

        Returns:
            A blank ``BusinessRecord`` placeholder.
        """

        logger.debug("Parse placeholder called with raw item: %r", raw_item)
        return BusinessRecord()
