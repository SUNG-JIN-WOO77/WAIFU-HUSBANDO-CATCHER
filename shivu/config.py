class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5947904339"
    sudo_users = "5947904339"
    GROUP_ID = -4970580235
    TOKEN = "8069497597:AAHCG3qd9I4H5awf7uogQ3pVMEkoVrjbc-0"
    mongo_url = "mongodb+srv://freefire1379045919:ZJrcwCD0D1FIMMzz@cluster22.f1ro5nh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster22"
    PHOTO_URL = ["https://graph.org/file/f181c8be7b22c4198e712-47f15e0688dc6f742e.jpg", "https://graph.org/file/68bc036f99234e59ae255-e7302854249889d963.jpg"]
    SUPPORT_CHAT = "dekh_kya_rha_kar_join"
    UPDATE_CHAT = "dekh_kya_rha_kar_join"
    BOT_USERNAME = "dekh_kya_rha_kar_join"
    CHARA_CHANNEL_ID = "-1002500793096"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
