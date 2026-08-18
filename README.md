# BGP Poison Lab (`bgp-poison-lab`)

**Category:** networking · **Difficulty:** hard · **Points:** 425

A lab BGP hijack lets you intercept traffic that carries the seed.

## Run it

```bash
docker build -t sparflag/bgp-poison-lab .
# `deca-ai start bgp-poison-lab` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is Fernet ciphertext. Discover the key seed, derive the Fernet key, then decrypt.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit bgp-poison-lab 'sparflag{...}'
```

## Hints

- Announce a more-specific prefix in the lab topology.
- Sniff the diverted flow for the Fernet seed.
