# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "16214694"))
API_HASH = getenv("API_HASH", "7545825d90eb7adae543d59909c73121")
BOT_TOKEN = getenv("BOT_TOKEN", "5817724211:AAEgJCwpSDyl18AYuW2N4O1Xp8iF8lc2ER8")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5543709855").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://sandeep123:<db_password>@cluster0.ggtof.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1001664442987")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002411457380"))
