from .config import ASSET_DIR


def list_created_accounts():
    with open(ASSET_DIR + "/users.txt", "r") as f:
        accounts = [l.split(",") for l in f.read().splitlines()]
    return [{"username": i[0], "password": i[1], "email": i[2]} for i in accounts]
