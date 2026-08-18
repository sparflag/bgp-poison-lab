#!/usr/bin/env python3
"""BGP Poison Lab — real mini-challenge (bgp-poison-lab)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", 'route-hijack')


def main():
    mat = fetch_material()
    key = CHALLENGE_KEY or "bgp-key"
    with open("/challenge/flag.enc", "w") as fh:
        fh.write(mat.get("delivery_blob", ""))
    update = (
        "=== bgp.update (route leak simulation) ===\n"
        "UPDATE msg from AS65001 -> AS65002\n"
        "NLRI: 203.0.113.0/24\n"
        f"BGP path attribute COMMUNITY: 65001:{hash(key) % 100000}:{key}\n"
        "ORIGIN: INCOMPLETE\n"
        "NOTE: community third segment encodes exfil seed\n"
        "---\n"
    )
    with open("/challenge/bgp.update", "w") as fh:
        fh.write(update)
    print("BGP Poison Lab — parse COMMUNITY attribute in bgp.update for the seed.")


if __name__ == "__main__":
    main()
