from modules import list_created_accounts

acc = list_created_accounts.list_created_accounts()
print(
    "\n".join(["Name: {} Password: {} Email: {}".format(*(i.values())) for i in acc])
)
