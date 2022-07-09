from plyer import notification
from PyDictionary import PyDictionary
import random
import time

if __name__ == "__main__":
    while True:
        dictionary = PyDictionary()
        word = ['adhere', 'anticipate', 'characteristic', 'compose', 'critical', 'determine', 'differentiate', 'engage', 'glaring', 'hypothesis', 'imminent', 'inevitable', 'intution', 'justify', 'omit', 'precede', 'redundant', 'relevant', 'trivial', 'uniform']
        result = random.choice(word)
        meaning = dictionary.meaning(result)
        notification.notify(
        title = result,
        message = str(meaning)[:101],
        timeout = 10
        )
        time.sleep(5)
    