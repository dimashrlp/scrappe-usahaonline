"""Template module for verifying search results before saving them.

The future implementation can use this module to confirm that collected records
are relevant to Kota Prabumulih and match the target business criteria.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


class SearchVerifier:
    """Placeholder verifier for future business record validation."""

    def is_relevant_location(self, address: str | None, target_location: str) -> bool:
        """Check whether a record address belongs to the target location.

        Args:
            address: Address text collected by the future scraper.
            target_location: Expected city or region.

        Returns:
            ``False`` until real verification rules are implemented.
        """

        logger.debug("Location verification placeholder: %r vs %r", address, target_location)
        return False

    def is_duplicate(self, business_name: str | None, existing_names: set[str]) -> bool:
        """Check whether a business name already exists in the current dataset."""

        if business_name is None:
            return False
        return business_name.strip().lower() in existing_names
