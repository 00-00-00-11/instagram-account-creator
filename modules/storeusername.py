import logging

from .config import ASSET_DIR


def store(account):
    with open(ASSET_DIR + "/users.txt", "a+") as f:
        u = account["username"]
        p = account["password"]
        e = account["email"]
        logging.info("Storing username {}".format(u))
        f.write(",".join([u, p, e]) + "\n")
