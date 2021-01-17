from time import sleep
import keyboard
import json

# 41 = "|"


def rquest_home(home="h", delay=0.07):
    keyboard.press_and_release("t")
    sleep(delay)
    keyboard.write(f"/home {home}")
    sleep(delay)
    keyboard.press_and_release("enter")
    sleep(delay)  # counter spam


def on_start():
    print("Home listener is now turned On")


def static_config():  # old way
    return {  # key : home | pair
        "tab": "h",
        41: "p",  # 41 = "|"
        "0": "n",
        "plus": "wood"
    }


def load_config():  # new way
    with open('config.json') as json_file:
        config = json.load(json_file)
        new_config = {}

        for item in config:
            if "int-" in item:
                name = str(item)[len("int-"):]
                value = config[item]

                new_config[int(name)] = value
            else:
                new_config[item] = config[item]
    return new_config


if __name__ == "__main__":
    on_start()

    running = True
    input_keys = load_config()

    while running:
        for key in input_keys:
            if keyboard.is_pressed(key):
                rquest_home(input_keys[key])
