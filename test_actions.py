import sys
import time
import readchar
import concurrent.futures
import os
import inspect
import importlib
import glob

from modules.actions.randomMove import RandomMove

def my_capitalize(str):
    return (str[0]).upper() + str[1:]

def key_and_run(config):
    while(True):
        key = readchar.readchar()
        print(key + " pressed.")

        for action, keys in config.items():
            if keys[0] == key:
                action.activate()
            elif keys[1] == key:
                action.deactivate()

        if(key == "x"):
            sys.exit()

def update(action):
    while(True):
        if(action.active):
            action.update()

        time.sleep(1.0 / 60.0)

if __name__ == "__main__":
    exe = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    
    # Making action instances for each files in modules/actions
    actions_obj = []
    for f in glob.glob(os.path.join("modules/actions", "*.py")):
        # Loading each files as module
        classname = os.path.splitext(os.path.basename(f))[0]
        m = importlib.import_module("modules.actions.{}".format(classname))
        # Loading classes written in files
        print(my_capitalize(classname))
        actions_obj += [c for c in inspect.getmembers(m, inspect.isclass) if c[0] == my_capitalize(classname)]
    
    actions = [o[1]() for o in actions_obj if o[0] != 'Action']

    print(actions)

    config = {
        actions[0]: ["w", "s"]
    }
    exe.submit(key_and_run, config)
    exe.submit(update, actions[0])
