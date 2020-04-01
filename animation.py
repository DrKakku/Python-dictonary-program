import itertools
import threading
import time
import sys

"""
This module aims to provide a animation for various(hopefully) animated emojis


"""

def cry_animation():
    animation = "‧º·(˚ ˃̣̣̥⌓˂̣̣̥ )‧º·˚˚‧º·(˚ ˃̣̣̥⌓˂̣̣̥ )‧º·˚"
    def animate():
        for c in itertools.cycle(['‧º·(˚ ˃̣̣̥⌓˂̣̣̥ )‧º·', '˚˚‧º·(˚ ˃̣̣̥⌓˂̣̣̥ )‧º·˚˚']):
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)
    t = threading.Thread(target=animate)
    t.start()