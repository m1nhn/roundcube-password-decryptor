# 🔓 Roundcube Password Decryptor

This is a simple PHP script to decrypt encrypted Roundcube passwords, typically found in session data or user preferences.


---

## 📚 How Roundcube Encrypts Passwords

Roundcube stores passwords encrypted using OpenSSL symmetric ciphers (e.g. `des-ede3-cbc`). The encryption process is defined in [rcube.php](https://github.com/roundcube/roundcubemail/blob/master/program/lib/Roundcube/rcube.php), using the following logic:

- A **random IV (initialization vector)** is generated and prepended to the ciphertext.
- A **cipher method** (usually `des-ede3-cbc`) is used with a 24-byte key (`$config['des_key']`).
- The result is **base64-encoded** and stored in the database.

To decrypt:
1. Base64-decode the string.
2. Extract the IV.
3. Extract the ciphertext.
4. Decrypt using `openssl_decrypt()` with the correct cipher and key.
