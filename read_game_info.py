import json


try:
    with open('leroy_info.json', 'r') as f:
        info = json.load(f)
except Exception as e:
    print('COULD NOT OPEN FILE')
    print(e)
    # no file saved, open new game
    info = {'name':'no_name', 'score':0}
else:
    print('success!')


print(info)

