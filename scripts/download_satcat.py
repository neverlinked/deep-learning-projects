"""Download the CelesTrak satellite catalogue (SATCAT) as a dated CSV.

Source page : https://celestrak.org/satcat/
Column docs : https://celestrak.org/satcat/satcat-format.php

Usage:
    python scripts/download_satcat.py

Saves to data/satcat_YYYY-MM-DD.csv using today's date, so every notebook run
can state exactly which snapshot of the catalogue it used.
"""

from datetime import date
from pathlib import Path
from urllib.request import urlopen, Request

SATCAT_URL = "https://celestrak.org/pub/satcat.csv"
DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    target = DATA_DIR / f"satcat_{date.today().isoformat()}.csv"

    if target.exists():
        print(f"Already downloaded: {target} ({target.stat().st_size / 1e6:.1f} MB)")
        return

    print(f"Downloading {SATCAT_URL} ...")
    request = Request(SATCAT_URL, headers={"User-Agent": "space-object-classifier/1.0"})
    with urlopen(request, timeout=60) as response:
        payload = response.read()

    target.write_bytes(payload)
    print(f"Saved {target} ({len(payload) / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
