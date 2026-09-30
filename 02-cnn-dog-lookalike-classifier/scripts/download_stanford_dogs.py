"""Download the Stanford Dogs dataset (images + bounding box annotations).

Source page : http://vision.stanford.edu/aditya86/ImageNetDogs/
Files       : images.tar (~750 MB) and annotation.tar (~21 MB)

Usage:
    python scripts/download_stanford_dogs.py

Extracts to data/Images/<breed folder>/*.jpg and data/Annotation/<breed folder>/<image id>
(the annotation files are XML without an extension). Writes data/DOWNLOAD_DATE.txt so the
notebook can say exactly when the data was fetched.
"""

import tarfile
from datetime import date
from pathlib import Path
from urllib.request import Request, urlopen

BASE = "http://vision.stanford.edu/aditya86/ImageNetDogs/"
FILES = {"images.tar": "Images", "annotation.tar": "Annotation"}
DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def download(name: str) -> Path:
    target = DATA_DIR / name
    if target.exists():
        print(f"Already downloaded: {target}")
        return target
    print(f"Downloading {BASE + name} ...")
    request = Request(BASE + name, headers={"User-Agent": "dog-lookalike-classifier/1.0"})
    with urlopen(request, timeout=120) as response, open(target, "wb") as out:
        while chunk := response.read(1 << 20):
            out.write(chunk)
    print(f"Saved {target} ({target.stat().st_size / 1e6:.0f} MB)")
    return target


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    for name, folder in FILES.items():
        if (DATA_DIR / folder).exists():
            print(f"{folder}/ already extracted")
            continue
        archive = download(name)
        print(f"Extracting {name} ...")
        with tarfile.open(archive) as tar:
            tar.extractall(DATA_DIR)
        archive.unlink()  # the extracted folder is all we need, saves ~750 MB of disk
    stamp = DATA_DIR / "DOWNLOAD_DATE.txt"
    if not stamp.exists():
        stamp.write_text(date.today().isoformat() + "\n")
    n_img = sum(1 for _ in (DATA_DIR / "Images").rglob("*.jpg"))
    print(f"Done. {n_img} images found (expected 20580).")


if __name__ == "__main__":
    main()
