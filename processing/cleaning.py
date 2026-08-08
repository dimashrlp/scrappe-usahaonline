"""Template functions for cleaning scraped business data.

The functions in this module are intentionally lightweight placeholders. They
make the expected cleaning responsibilities explicit before Sprint 2 adds real
scraping data and Sprint 3 adds stronger validation rules.
"""

from __future__ import annotations

import logging
from dataclasses import asdict, is_dataclass
from typing import Any

import pandas as pd

from config import FIELD_NAMES
from scraper.maps_scraper import BusinessRecord

logger = logging.getLogger(__name__)


def clean_business_data(records: list[BusinessRecord]) -> pd.DataFrame:
    """Clean raw business records and return a dataset-ready DataFrame.

    Args:
        records: Business records collected by the future scraping process.

    Returns:
        A DataFrame with columns ordered according to ``config.FIELD_NAMES``.
        Detailed cleaning rules will be added after real data is available.
    """

    logger.info("Cleaning placeholder received %d records.", len(records))
    dataframe = pd.DataFrame([record.to_dict() for record in records], columns=FIELD_NAMES)
    return dataframe


def normalize_text(value: str | None) -> str | None:
    """Normalize repeated whitespace in general text fields."""

    if value is None:
        return None
    return " ".join(value.split())


def clean_phone_number(value: str | None) -> str | None:
    """Prepare phone-number normalization rules for Sprint 3 cleaning."""

    return normalize_text(value)


def clean_rating(value: str | float | int | None) -> float | None:
    """Prepare rating conversion from raw Google Maps text to ``float``."""

    if value is None or isinstance(value, float):
        return value
    if isinstance(value, int):
        return float(value)
    return None


def clean_review_count(value: str | int | None) -> int | None:
    """Prepare review-count conversion from raw text to ``int``."""

    if value is None or isinstance(value, int):
        return value
    return None


def normalize_address(value: str | None) -> str | None:
    """Prepare address normalization for Prabumulih business locations."""

    return normalize_text(value)


def remove_duplicate_business(records: list[BusinessRecord]) -> list[BusinessRecord]:
    """Prepare duplicate-removal rules based on business identity fields."""

    return records


def build_digital_channel(record: BusinessRecord) -> str | None:
    """Build a summary of available verified digital channels for one record."""

    channels = [
        channel_name
        for channel_name in ("website", "instagram", "facebook", "tiktok", "shopee", "tokopedia")
        if getattr(record, channel_name)
    ]
    return ", ".join(channels) if channels else None


def record_to_dict(record: BusinessRecord) -> dict[str, Any]:
    """Convert one dataclass record into a dictionary for tabular processing."""

    if not is_dataclass(record):
        raise TypeError("record_to_dict expects a dataclass-based BusinessRecord")
    return asdict(record)
