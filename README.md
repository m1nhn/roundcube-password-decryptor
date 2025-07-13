# 🔓 Roundcube Password Decryptor

This is a simple PHP script to decrypt encrypted Roundcube passwords, typically found in session data or user preferences.

> 🛡️ This tool is for **educational, forensic, or incident response purposes only**. Do not use it on systems you do not own or have explicit permission to audit.

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

---

## ✅ Usage

1. Clone or download this repository.
2. Open the `decrypt.php` file and:
   - Replace the `$encrypted` variable with the base64 string you found in the Roundcube database (e.g., from the `session` or `preferences` columns).
   - Replace the `$key` with the 24-byte DES key from your Roundcube configuration:

     ```php
     // config/config.inc.php
     $config['des_key'] = 'rcmail-!24ByteDESkey*Str';  // Example only
     ```

3. Run the script:
   ```bash
   php decrypt.php
