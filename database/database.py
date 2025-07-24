# database/database.py

# For broadcasting or post management (e.g. newpost.py)
channels = set()

def save_channel(chat_id: str):
    channels.add(chat_id)
    return True

def delete_channel(chat_id: str):
    channels.discard(chat_id)
    return True

def get_channels():
    return list(channels)


# For forced subscription (multi-channel)
forced_channels = set()

def add_forced_channel(channel_id: str):
    forced_channels.add(channel_id)
    return True

def remove_forced_channel(channel_id: str):
    forced_channels.discard(channel_id)
    return True

def get_forced_channels():
    return list(forced_channels)


# Admin check
admin_users = set()

def add_admin(user_id: int):
    admin_users.add(user_id)

def remove_admin(user_id: int):
    admin_users.discard(user_id)

def is_admin(user_id: int) -> bool:
    return user_id in admin_users
