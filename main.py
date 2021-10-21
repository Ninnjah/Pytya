import os
from typing import Callable

import rsa
import colorama
from colorama import Fore

from utils import cli
from utils import key_manager

if __name__ == "__main__":
    colorama.init(autoreset=True)
    public_path: str = os.path.abspath("public.key")
    private_path: str = os.path.abspath("private.key")
    clear: Callable[[], None] = lambda: print("\033[H\033[J", end="")

    print("Loading...")

    # Load keys
    if os.path.exists(private_path) and os.path.exists(public_path):
        try:
            public_key = key_manager.load_public_key(public_path)
            private_key = key_manager.load_private_key(private_path)

        except ValueError:
            public_key, private_key = rsa.newkeys(2048)

    # Create new keys
    else:
        public_key, private_key = rsa.newkeys(2048)

    # Save keys
    key_manager.save_key(public_key)
    key_manager.save_key(private_key)

    clear()