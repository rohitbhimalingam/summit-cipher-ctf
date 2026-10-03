# Summit Cipher CTF

A cryptography challenge about recovering a hidden mask, undoing a prime leak,
and decrypting an RSA ciphertext.

## Files

- `chall.py` prints the challenge data from `challenge.json`.
- `challenge.json` contains the RSA modulus and ciphertext, subset-sum weights,
  and the masked prime leak.
- `clarification.enc` contains the additional challenge clarification.

## Run

Use Python 3:

```sh
python chall.py
```

Keep `chall.py` and `challenge.json` in the same directory.
