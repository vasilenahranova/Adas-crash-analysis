"""Download NHTSA Standing General Order Level 2 ADAS crash reports."""
from pathlib import Path

import requests

BASE = "https://static.nhtsa.gov/odi/ffdd/sgo-2021-01"
RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"

FILES = {
    "adas_current.csv": f"{BASE}/SGO-2021-01_Incident_Reports_ADAS.csv",
    "adas_archive.csv": f"{BASE}/Archive-2021-2025/SGO-2021-01_Incident_Reports_ADAS.csv",
    "definitions_current.pdf": f"{BASE}/SGO-2021-01_Data_Element_Definitions.pdf",
    "definitions_archive.pdf": f"{BASE}/Archive-2021-2025/SGO-2021-01_Data_Element_Definitions.pdf",
}


def download(name: str, url: str) -> None:
    target = RAW_DIR / name
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    target.write_bytes(response.content)
    print(f"{name}: {len(response.content) / 1_000_000:.1f} MB")


if __name__ == "__main__":
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    for name, url in FILES.items():
        download(name, url)