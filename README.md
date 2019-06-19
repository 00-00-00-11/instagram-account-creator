# Insta Mass Account creator

Small script to create a number of random instagram accounts

## Installation

Clone it

`pip install -r requirements.txt`

Then you may want chromedriver for use in selenium, put it to your path


## Configuration
open config.py in modules

| Config | Usage |
| :---         |  :---     |
| bot_type| Default is 1 to use selenium to create accounts or use 2 to use python requests|
| use_local_ip_address | using local IP to create accounts, default is False  |
| use_custom_proxy | use your own custom proxy, Default is False change to True add list of proxies to Assets/proxies.txt |
| amount_of_account | amount of account to create |  
| proxy_file_path | Path to the proxy file .txt format |
| amount_per_proxy| for custom proxy, amount of account to create for each proxy |
| email_domain | for custom domain name, is useful for use own email_domain
| country | the country of account
| identity | the complete name of created accounts

run **`python creator.py`**

All usernames, passwords and emails are stored in Assets/users.txt

### Features

This script creates account with random name get by the web and doesn't use random name or random usernames. All users created are older than 18 years.

### Important

-  The new fake Instagram account with an unverified phone number after ~ 1-24 hours could not do any requests. All requests will be redirected to the page           
[instagram.com/challenge](https://instagram.com/challenge)

### Contributing

- Fork this repo.
- Add new features.
- Create a new pull request for this branch.


### Credits
[Matteo Gaito for the base](https://github.com/matteogaito)
