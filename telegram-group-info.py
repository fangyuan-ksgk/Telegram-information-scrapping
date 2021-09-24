from telethon import TelegramClient, events, sync
from telethon import functions, types, utils

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = #API ID# example: 8733505
api_hash = #API Hash# example: '9557d411b02ba50172e8b9fe94a00060'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

# user information 
me = client.get_entity('me')
username = utils.get_display_name(me)
print(utils.get_display_name(me))

# channel with join link can be accessed in this way
my_channel = client.get_entity('https://t.me/joinchat/cMkUXlSPNdxkZTg0')
print(my_channel)
# the 'my_channel' is now a specific 'chat' object in telethon API, which can be used later on

# Full description of the channel:
result = client(functions.channels.GetFullChannelRequest(
        channel=my_channel
    ))
print(result.stringify())

# We create a list of all IDs in 'my_channel' here
id_list = []
for user in client.iter_participants(my_channel):
    print(user.id)
    id_list += [str(user.id)]
print('list of user-IDs',id_list)

# Alternatively, the dialogs return all the entities (conversations/channels which currently involved)
# which your account is associated to, from there we can know all the channels' information
dialogs = client.get_dialogs()
print(dialogs)

from telethon.tl.types import PeerUser, PeerChat, PeerChannel
# for instance we retrieve the channel's peer_id from the printed /dialogs/
peer_id=PeerChannel(channel_id=1389385773)
print(peer_id)
specific_channel = client.get_entity(peer_id)
print(specific_channel)

# We create a list of all IDs in 'specific_channel' here
id_list = []
for user in client.iter_participants(specific_channel):
    print(user.id)
    id_list += [str(user.id)]
print('list of user-IDs',id_list)
