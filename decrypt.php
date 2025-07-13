<?php
/**
 * Roundcube Password Decryptor (for educational & forensic analysis purposes)
 * 
 * Usage:
 *   - Replace $encrypted with your base64-encoded encrypted password string.
 *   - Replace $key with your known DES key from config file (NOT included here).
 */

function decrypt_roundcube_password($b64_input, $key) {
    $raw = base64_decode($b64_input);
    $iv = substr($raw, 0, 8);
    $ciphertext = substr($raw, 8);
    return openssl_decrypt($ciphertext, 'des-ede3-cbc', $key, OPENSSL_RAW_DATA, $iv);
}
// Example usage
$encrypted = 'REPLACE_THIS_WITH_YOUR_DEBASE64_SESSION_KEY';

// 🔐 Replace with your actual DES key from Roundcube config:
// $key = 'your-24-byte-des-key-here';

$key = 'REPLACE_THIS_WITH_YOUR_24_BYTE_DES_KEY';

$plaintext = decrypt_roundcube_password($encrypted, $key);
echo "🔓 Decrypted password: " . rtrim($plaintext, "\0") . "\n";
