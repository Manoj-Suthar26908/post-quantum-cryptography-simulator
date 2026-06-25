"""Falcon benchmark wrapper."""

from pqcrypto.sign.falcon_512 import generate_keypair, sign, verify


def falcon_test():
    """Generate, sign, and verify a message with Falcon-512."""
    message = b"Post Quantum Crypto Test"

    public_key, secret_key = generate_keypair()
    signature = sign(secret_key, message)
    valid = verify(public_key, message, signature)

    return {
        "success": valid,
        "public_key_size": len(public_key),
        "private_key_size": len(secret_key),
        "data_size": len(signature),
    }
