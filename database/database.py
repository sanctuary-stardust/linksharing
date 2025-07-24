forced_channels = set()

def add_forced_channel(channel_id: str):
    forced_channels.add(channel_id)
    return True

def remove_forced_channel(channel_id: str):
    forced_channels.discard(channel_id)
    return True

def get_forced_channels():
    return list(forced_channels)
