import json
# JSON到字典转化
f2 = open('config.json', 'r')
info_data = json.load(f2)
print(info_data)


class init_json(object):
    def __init__(self, **args):
        self.__dict__.update(args)
        return


config = init_json(**info_data)
