from typing import Union
from rsa import PublicKey, PrivateKey


def save_key(key: Union[PublicKey, PrivateKey], filename: str = "key.key") -> None:
    """Saves public or private key to file

    :param key: Key object
    :param filename: Key file name
    :return: None
    """
    with open(filename, "wb") as f:
        f.write(key.save_pkcs1())
