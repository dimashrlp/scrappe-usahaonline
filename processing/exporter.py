"""Export helpers for saving processed scraping results.

The exporter is prepared for the final dataset schema but does not implement any
scraping behavior. It accepts typed ``BusinessRecord`` objects or cleaned
DataFrames and saves columns in the configured output order.
"""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from config import FIELD_NAMES
from scraper.maps_scraper import BusinessRecord

logger = logging.getLogger(__name__)


def records_to_dataframe(records: list[BusinessRecord]) -> pd.DataFrame:
    """Convert typed business records into a DataFrame with final columns."""

    return pd.DataFrame([record.to_dict() for record in records], columns=FIELD_NAMES)


def prepare_export_dataframe(data: pd.DataFrame | list[BusinessRecord]) -> pd.DataFrame:
    """Return a DataFrame aligned to ``FIELD_NAMES`` for CSV/XLSX export."""

    dataframe = records_to_dataframe(data) if isinstance(data, list) else data.copy()
    for field_name in FIELD_NAMES:
        if field_name not in dataframe.columns:
            dataframe[field_name] = None
    return dataframe[FIELD_NAMES]


def export_to_csv(data: pd.DataFrame | list[BusinessRecord], output_path: Path) -> None:
    """Save cleaned business data to a CSV file using the final field order."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe = prepare_export_dataframe(data)
    dataframe.to_csv(output_path, index=False)
    logger.info("CSV export placeholder saved file to %s.", output_path)


def export_to_excel(data: pd.DataFrame | list[BusinessRecord], output_path: Path) -> None:
    """Save cleaned business data to an Excel file using the final field order."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe = prepare_export_dataframe(data)
    dataframe.to_excel(output_path, index=False)
    logger.info("Excel export placeholder saved file to %s.", output_path)
