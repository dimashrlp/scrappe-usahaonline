"""Entry point for the BPS Prabumulih online business scraping project.

Sprint 2.2 validates that Playwright can run Google Maps searches for several
configured keywords without scraping, scrolling, parsing, or exporting data.
"""

from __future__ import annotations

import logging

from config import (
    DATE_FORMAT,
    DEFAULT_KEYWORDS,
    LOG_FILE,
    LOG_FORMAT,
    LOG_LEVEL,
    PROJECT_NAME,
    SPRINT_2_2_KEYWORD_LIMIT,
)
from scraper.maps_scraper import MapsScraper


def setup_logging() -> None:
    """Configure console and file logging for the project.

    Logs are written to ``logs/scraping.log`` and also displayed in the console.
    The function is intentionally lightweight so future modules can call
    ``logging.getLogger(__name__)`` without duplicating logging setup.
    """

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=LOG_LEVEL,
        format=LOG_FORMAT,
        datefmt=DATE_FORMAT,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
        ],
        force=True,
    )


def main() -> None:
    """Run the Sprint 2.2 Google Maps multi-keyword automation check."""

    setup_logging()
    logger = logging.getLogger(__name__)
    keywords = DEFAULT_KEYWORDS[:SPRINT_2_2_KEYWORD_LIMIT]

    logger.info("Project Started")
    logger.info("Project Name: %s", PROJECT_NAME)
    logger.info("Sprint 2.2 keyword validation count: %d", len(keywords))

    try:
        scraper = MapsScraper()
        scraper.start_keywords(keywords)
    except Exception:
        logger.error("Project Failed")
        raise
    finally:
        logger.info("Project Finished")


if __name__ == "__main__":
    main()
