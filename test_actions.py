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
    current_action = None
    
    while(True):
        key = readchar.readchar()
        print(key + " pressed.")

        for action, keys in config.items():
            if keys[0] == key:
                if (current_action != None):
                    current_action.deactivate()
                action.activate()
                current_action = action
            elif keys[1] == key:
                action.deactivate()
                current_action = None

        if(key == "x"):
            sys.exit()

def update(actions):
    while(True):
        for action in actions:
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
        actions_obj += [c for c in inspect.getmembers(m, inspect.isclass) if c[0] == my_capitalize(classname)]
    
    actions = [o[1]() for o in actions_obj if o[0] != 'Action']

    print(actions)

    config = {
        actions[1]: ["q","a"],
        actions[2]: ["e","d"]
    }
    for action, keys in config.items():
        print("{0}: Binded {1} to activate, {2} to deactivate.".format(action, keys[0], keys[1]))
    exe.submit(key_and_run, config)
    exe.submit(update, actions)
