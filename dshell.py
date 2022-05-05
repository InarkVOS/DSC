import configparser
import platform
import os
config = configparser.ConfigParser()
config.read('commands.ini')

def as_dict():
    dictionary = {}
    for section in config.sections():
        dictionary[section] = {}
        for option in config.options(section):
            dictionary[section][option] = config.get(section, option)
    return dictionary

d = as_dict()

def getProp(property,app):
    prop = d.get(app)
    prop2 = prop.get(property)
    return prop2
def Exists(app):
    if config.has_section(app.lower()):
        return True
    else:
        return False
def openapp(app, args):
    if app.lower() == "exit":
        try:
            code = int(args[0])
        except:
            code = 0
        exit(code)
    elif app.lower() == "rlprompt":
        reload()
    if Exists(app):
        python = "python" if platform.system() == "Windows" else "python3"
        global inp_onlyargs
        inp_onlyargs = ' '.join(inp_onlyargs)
        os.system(f'{python} {getProp("path", app)} {inp_onlyargs}')
    else:
        print('Command or application not found!')

def reload():
    init_prompt()
    reload_config()

def reload_config():
    config.read('commands.ini')
    d = as_dict()

def init_prompt():
    f = open('.dshellrc', 'r')
    lines = f.readlines()
    f.close()
    user = ''
    host = ''
    for line in lines:
        line = line.splitlines()[0]
        if line.startswith('user '):
            user = line.split(' ')[1:]
            user = ' '.join(user)
        if line.startswith('host '):
            host = line.split(' ')[1:]
            host = ' '.join(host)
    global prompt
    prompt = f'{user}@{host}> '
init_prompt()
while True:
    reload()
    init_prompt()
    inp = input(prompt)
    inp_transformed = inp.split(' ',1)
    inp_onlyargs = inp.split(' ')
    inp_onlyargs.pop(0)
    openapp(inp_transformed[0],inp_onlyargs)