"""CRYSTALS-Kyber / ML-KEM benchmark wrapper."""

from pqcrypto.kem.ml_kem_512 import decrypt, encrypt, generate_keypair


def kyber_test():
    """Generate, encapsulate, and decapsulate an ML-KEM-512 shared secret."""
    public_key, secret_key = generate_keypair()

    ciphertext, shared_secret = encrypt(public_key)
    recovered_secret = decrypt(secret_key, ciphertext)

    return {
        "success": shared_secret == recovered_secret,
        "public_key_size": len(public_key),
        "private_key_size": len(secret_key),
        "data_size": len(ciphertext),
    }
