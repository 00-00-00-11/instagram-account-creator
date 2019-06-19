from .config import ASSET_DIR


def list_created_account():
    with open(ASSET_DIR + "/users.txt", "r") as f:
        accounts = f.read().splitlines().split(",")
    return [{"username": i[0], "password": i[1], "email": i[2]} for i in accounts]


if __name__ == "__main__":
    acc = list_created_account()
    print(
        "\n".join(["Name: {} Password: {} Email: {}".format(i.values()) for i in acc])
    )
