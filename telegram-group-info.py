from telethon import TelegramClient, events, sync
from telethon import functions, types, utils

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 8733505
api_hash = '9557d411b02ba50172e8b9fe94a00060'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

#result = client(functions.channels.GetChannelsRequest(id=['Bob Dyln']))

me = client.get_entity('me')
username = utils.get_display_name(me)
print(utils.get_display_name(me))
chat = client.get_input_entity(username)
print(chat)

# channel which user is manager, or have a join link can be accessed in here

my_channel = client.get_entity('https://t.me/joinchat/cMkUXlSPNdxkZTg0')
print(my_channel)

print('The channel object can then be used for instance in https://tl.telethon.dev/types/input_channel.html')


# Search by name
#async for user in client.iter_participants(chat, search='name'):
#    print(user.username)

# full description of the channel: don't work
result = client(functions.channels.GetFullChannelRequest(
        channel=my_channel
    ))
print(result.stringify())



print('Try to print all the IDs')
id_list = []
for user in client.iter_participants(my_channel):
    print(user.id)
    id_list += [str(user.id)]
    print(type(user.id))
print('list of user-IDs',id_list)