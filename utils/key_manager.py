from typing import Union

import rsa
from rsa import PublicKey, PrivateKey


def save_key(key: Union[PublicKey, PrivateKey], filename: str = "key.key") -> None:
    """Saves public or private key to file

    :param key: Key object
    :param filename: Key file name
    :return: None
    """
    with open(filename, "wb") as f:
        f.write(key.save_pkcs1())


def load_public_key(filename: str) -> PublicKey:
    """Loads public key from file

    :param filename: Public key file name
    :return: Public key object
    """
    with open(filename, "rb") as f:
        return rsa.PublicKey.load_pkcs1(f.read())


def load_private_key(filename: str) -> PrivateKey:
    """Loads private key from file

    :param filename: Private key file name
    :return: Private key object
    """
    with open(filename, "rb") as f:
        return rsa.PrivateKey.load_pkcs1(f.read())
