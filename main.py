"""Entry point for the BPS Prabumulih online business scraping project.

This module intentionally does not contain scraping logic yet. It prepares the
application logging utility and provides a clear starting point for Sprint 2.
"""

from __future__ import annotations

import logging

from config import DATE_FORMAT, LOG_FILE, LOG_FORMAT, LOG_LEVEL, PROJECT_NAME, PROJECT_VERSION


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
    """Run the project workflow placeholder.

    Future implementation steps can be called from here, for example:
    1. Load keywords and configuration.
    2. Start the Google Maps scraper.
    3. Verify digital channels with Google Search.
    4. Clean the scraped data.
    5. Export results into CSV/XLSX files.
    """

    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting %s version %s.", PROJECT_NAME, PROJECT_VERSION)
    logger.info("Sprint 2 scraping workflow is not implemented yet.")


if __name__ == "__main__":
    main()
