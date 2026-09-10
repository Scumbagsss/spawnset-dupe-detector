"""Portfolio-only interface skeleton. This module is intentionally non-runnable."""


class SpawnsetDupeDetectorInterface:
    """Architectural surface of the private production implementation."""

    async def ingest_activity_batch(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

    async def build_timeline(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

    async def evaluate_case(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

    async def calculate_confidence(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

    async def update_case_state(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

