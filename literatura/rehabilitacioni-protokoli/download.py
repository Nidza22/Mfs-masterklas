#!/usr/bin/env python3
"""MFS Masterklas: preuzimanje javno dostupnih originalnih rehab PDF dokumenata.

Skripta NE uvozi PDF-ove u javni GitHub repozitorijum. Skida ih lokalno.
VALD i izvori koji zahtevaju formular ostaju samo linkovi u sources.json.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "sources.json"
OUTPUT = HERE / "pdf"
REPORT = HERE / "izvestaj-preuzimanja.json"
MAX_BYTES = 65 * 1024 * 1024


def pdf_ok(path: Path) -> bool:
    try:
        with path.open("rb") as handle:
            return handle.read(5) == b"%PDF-"
    except OSError:
        return False


def download(item: dict, force: bool = False) -> dict:
    target = OUTPUT / item["fajl"]
    if target.is_file() and pdf_ok(target) and not force:
        return {"id": item["id"], "status": "vec_postoji", "putanja": str(target.relative_to(HERE))}
    req = urllib.request.Request(
        item["url"],
        headers={"User-Agent": "MFS-Masterklas-research-library/1.0 (educational-use)",
                 "Accept": "application/pdf,*/*;q=0.8"},
    )
    temp_path = None
    try:
        with urllib.request.urlopen(req, timeout=55) as response:
            if getattr(response, "status", 200) != 200:
                raise ValueError(f"HTTP status {response.status}")
            with tempfile.NamedTemporaryFile(mode="wb", suffix=".part", prefix="mfs-", dir=OUTPUT, delete=False) as fout:
                temp_path = Path(fout.name)
                total = 0
                digest = hashlib.sha256()
                first = True
                while True:
                    chunk = response.read(131072)
                    if not chunk:
                        break
                    if first:
                        if not chunk.startswith(b"%PDF-"):
                            raise ValueError("Odgovor nije PDF (moguce HTML/registracija)")
                        first = False
                    total += len(chunk)
                    if total > MAX_BYTES:
                        raise ValueError("Prekoracena granica od 65 MB")
                    digest.update(chunk)
                    fout.write(chunk)
                if total < 100:
                    raise ValueError("Dokument je prazan ili previse kratak")
        temp_path.replace(target)
        return {"id": item["id"], "status": "preuzeto", "putanja": str(target.relative_to(HERE)),
                "bajtova": total, "sha256": digest.hexdigest(), "originalni_url": item["url"]}
    except (OSError, ValueError, urllib.error.URLError) as exc:
        return {"id": item["id"], "status": "greska", "opis": str(exc), "originalni_url": item["url"]}
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="MFS: lokalno preuzimanje PDF rehab protokola")
    parser.add_argument("--list", action="store_true", help="Prikazi dokumente bez preuzimanja")
    parser.add_argument("--only", metavar="ID", help="Preuzmi samo jedan ID iz sources.json")
    parser.add_argument("--force", action="store_true", help="Ponovo preuzmi vec postojeci PDF")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    direct = [item for item in manifest["izvori"] if item["tip"] == "direktan_pdf"]
    if args.only:
        direct = [item for item in direct if item["id"] == args.only]
        if not direct:
            print("Nepoznat ID ili nije javni direktan PDF.", file=sys.stderr)
            return 2
    if args.list:
        for item in direct:
            print(f'{item["id"]:33} {item["naziv"]}')
        print(f"Ukupno javnih PDF linkova: {len(direct)}")
        return 0

    OUTPUT.mkdir(parents=True, exist_ok=True)
    results = []
    for idx, item in enumerate(direct, 1):
        print(f'[{idx}/{len(direct)}] {item["id"]} ...', flush=True)
        outcome = download(item, args.force)
        print(f'  -> {outcome["status"]}' + (f': {outcome.get("opis")}' if outcome["status"] == "greska" else ""))
        results.append(outcome)

    report = {"generisano_utc": datetime.now(timezone.utc).isoformat(), "rezultati": results}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    good = sum(r["status"] != "greska" for r in results)
    print(f"Uspesno/dostupno: {good}/{len(results)}. Izvestaj: {REPORT}")
    return 0 if good == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
