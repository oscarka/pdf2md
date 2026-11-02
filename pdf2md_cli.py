#!/usr/bin/env python3
"""Lightweight CLI client for PDF2MD (https://pdf2md.fun) — PDF ⇄ Markdown converter."""
import argparse, base64, json, os, sys, urllib.request
from pathlib import Path

API_BASE = os.environ.get("PDF2MD_URL", "https://pdf2md.fun")


def pdf_to_md(pdf_path: Path, out_path: Path, license_code: str = ""):
    b64 = base64.b64encode(pdf_path.read_bytes()).decode("ascii")
    headers = {"Content-Type": "application/json", "User-Agent": "pdf2md-cli/1.0"}
    if license_code:
        headers["Cookie"] = f"lic={license_code}"
    req = urllib.request.Request(
        f"{API_BASE}/api/convert",
        data=json.dumps({"pdf_b64": b64}).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        res = json.loads(r.read().decode("utf-8"))
    out_path.write_text(res["markdown"], encoding="utf-8")
    print(f"✓ Saved {res['chars']} chars to {out_path} (credits remaining: {res.get('credits')})")


def md_to_pdf(md_path: Path, out_path: Path, license_code: str = ""):
    md_text = md_path.read_text(encoding="utf-8")
    headers = {"Content-Type": "application/json", "User-Agent": "pdf2md-cli/1.0"}
    if license_code:
        headers["Cookie"] = f"lic={license_code}"
    req = urllib.request.Request(
        f"{API_BASE}/api/topdf",
        data=json.dumps({"markdown": md_text}).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        res = json.loads(r.read().decode("utf-8"))
    out_path.write_bytes(base64.b64decode(res["pdf_b64"]))
    print(f"✓ Saved {res['bytes']} bytes to {out_path} (credits remaining: {res.get('credits')})")


def main():
    ap = argparse.ArgumentParser(description="PDF2MD (https://pdf2md.fun) CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("pdf2md", help="Convert PDF to Markdown (.md)")
    p1.add_argument("input", type=Path)
    p1.add_argument("-o", "--output", type=Path, required=True)
    p1.add_argument("-k", "--code", default=os.environ.get("PDF2MD_CODE", ""), help="License code (LIC-XXXX-XXXX)")

    p2 = sub.add_parser("md2pdf", help="Convert Markdown (.md) to PDF")
    p2.add_argument("input", type=Path)
    p2.add_argument("-o", "--output", type=Path, required=True)
    p2.add_argument("-k", "--code", default=os.environ.get("PDF2MD_CODE", ""), help="License code (LIC-XXXX-XXXX)")

    args = ap.parse_args()
    if args.cmd == "pdf2md":
        pdf_to_md(args.input, args.output, args.code)
    else:
        md_to_pdf(args.input, args.output, args.code)


if __name__ == "__main__":
    main()
