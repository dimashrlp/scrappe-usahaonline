"""Data model and scraper template for future Google Maps automation.

No scraping logic is implemented in this Sprint 1.5 foundation. The module only
prepares the final dataset model and extension points required before Sprint 2.
"""

from __future__ import annotations

import logging
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any

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
    """Placeholder scraper class for future Playwright Google Maps automation."""

    def __init__(self, headless: bool = True) -> None:
        """Initialize scraper configuration without launching Playwright.

        Args:
            headless: Whether the future browser session should run headlessly.
        """

        self.headless = headless

    def scrape(self, keyword: str, location: str) -> list[BusinessRecord]:
        """Collect business records for a keyword and location in Sprint 2.

        Args:
            keyword: Search keyword to be used by the future Google Maps scraper.
            location: Target city or area.

        Returns:
            An empty list until scraping logic is implemented.
        """

        logger.info("Scrape placeholder called for keyword='%s', location='%s'.", keyword, location)
        return []

    def parse_business_card(self, raw_item: Any) -> BusinessRecord:
        """Convert a raw browser element or response item into a business record.

        Args:
            raw_item: Raw data from a future Playwright selector or response.

        Returns:
            A blank ``BusinessRecord`` placeholder.
        """

        logger.debug("Parse placeholder called with raw item: %r", raw_item)
        return BusinessRecord()
