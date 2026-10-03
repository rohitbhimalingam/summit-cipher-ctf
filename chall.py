#!/usr/bin/env python3
"""Player-facing challenge printer."""

import json


with open("challenge.json") as f:
    challenge = json.load(f)

print("The veil is made from two weak layers.")
print("Recover the hidden mask, undo the prime leak, and decrypt the flag.")
print()
print(json.dumps(challenge, indent=2))
