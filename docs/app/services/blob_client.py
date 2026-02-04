from pathlib import Path


class LocalContentClient:
    """
    Local filesystem client used to simulate Azure Blob Storage during local dev & tests.
    """
    def __init__(self, base_dir: str = "data"):
        self.base_path = Path(base_dir)

    def read_text(self, filename: str) -> str:
        file_path = self.base_path / filename
        if not file_path.exists():
            raise FileNotFoundError(f"Content file not found: {file_path}")
        return file_path.read_text(encoding="utf-8")
