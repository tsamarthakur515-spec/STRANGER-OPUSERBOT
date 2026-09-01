from os import getenv
from dotenv import load_dotenv
from data import THE_SHUKLA

load_dotenv()

#----------------------------------- REQUIRED --------------------------------------#

API_ID = int(getenv("10079905"))
API_HASH = getenv("e4a5fa251e2e055f26e5c2add8401530")
SESSION1 = getenv("BQC86fAAX3P3focETLU9i2MuywIhrmcoVGZfNikwZ4JRd3BtWZrRymgG16n6nQ_gknaB7ERl1Qlh9bixAlffytP-nsSZ4Y9U9XKja-0h49IQVPr2R9L5RErQwNSCV1llhvIFIzdkzrR3eZJceCtxU_0qyv9tGtT_hR4xQcCYZYFVArf-ABFsf5l0-WjmwmudwDegUy6LG1fStl_ptXSvdCA7jxE_ClrQyCQJLTWhW8DLKYyplVwiBLAbhpLlQIL7XXCh4-CjIPCZMyukGHQQpwszZueOF0wgdUQq7TcYMfh9l0BxbTqwpCc51lanIZVeQoU3cFd2ZVq0nHOUNlczPOKRDBoeJAAAAAH-nwzIAA")
BOT_TOKEN = getenv("8582978557:AAHwJ2MvCpIKEOB9FbarmXzhdXSIJOpZSgY")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8582978557").split()))

#-------------------------------- OPTIONAL -------------------------------------#

SESSION2 = getenv("SESSION2")
SESSION3 = getenv("SESSION3")
SESSION4 = getenv("SESSION4")
SESSION5 = getenv("SESSION5")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

EXTRA_IMG = getenv("EXTRA_IMG", "https://files.catbox.moe/uufiry.jpg")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8841848847").split()))

for y in OWNER_ID:
    SUDO_USERS.append(y)

for x in THE_SHUKLA:
    SUDO_USERS.append(x)

LOAD = []
NO_LOAD = []
HELPABLE = {}