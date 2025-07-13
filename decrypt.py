#!/usr/bin/env python3
"""
Roundcube Password Decryptor (for educational & forensic analysis purposes)

Usage:
  - Replace 'encrypted' with the base64-encoded encrypted password string.
  - Replace 'key' with your known DES 24-byte key from Roundcube config.

This tool replicates the decryption logic used by Roundcube's `rcube.php`.
"""

from base64 import b64decode
from Crypto.Cipher import DES3


def decrypt_roundcube_password(b64_input: str, key: bytes) -> str:
    """
    Decrypts a Roundcube password encrypted with des-ede3-cbc and prepended IV.

    :param b64_input: The base64-encoded encrypted password string
    :param key: The 24-byte DES key (as bytes)
    :return: Decrypted plaintext string
    """
    raw = b64decode(b64_input)
    iv = raw[:8]
    ciphertext = raw[8:]

    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    return plaintext.rstrip(b'\0').decode()


if __name__ == "__main__":
    # 🔐 Replace with your actual base64 string (from Roundcube session/prefs)
    encrypted = "REPLACE_THIS_WITH_YOUR_BASE64_STRING"

    # 🔐 Replace with your 24-byte DES key from config.inc.php
    # Example: b'rcmail-!24ByteDESkey*Str'
    key = b"REPLACE_THIS_WITH_YOUR_24_BYTE_KEY"

    try:
        result = decrypt_roundcube_password(encrypted, key)
        print(f"🔓 Decrypted password: {result}")
    except Exception as e:
        print(f"[!] Decryption failed: {e}")
