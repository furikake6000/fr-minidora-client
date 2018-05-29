import sys
import time
import readchar
import concurrent.futures

from modules.actions.randomMove import RandomMove

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
    
    action = RandomMove()
    config = {
        action: ["w", "s"]
    }
    exe.submit(key_and_run, config)
    exe.submit(update, action)
