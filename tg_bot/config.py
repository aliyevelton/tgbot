from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = "1064219453"  # my telegram ID
    OWNER_USERNAME = "AliyevElton"  # my telegram username
    API_KEY = "1823852396:AAG4U7QJqJ48u1rzTR0HbJy75ILXEvr68G8"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-1001429318006' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1064219453]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
