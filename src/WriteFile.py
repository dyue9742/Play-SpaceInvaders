from PIL import Image
import datetime
import numpy as np
import sys

def write_and_save(need_to_write=None, type=None):
    if need_to_write is None:
        print("To be honest, nothing need to write!")
        sys.exit()
    else:
        if type == "png":
            if isinstance(need_to_write, np.ndarray):
                now = write_and_save_png()
                data = Image.fromarray(need_to_write)
                data.save(now)
        elif type == "txt":
            now = write_and_save_txt()
            f = open(now, "w+")
            for element in need_to_write:
                f.write(str(element))

def write_and_save_png():
    now_png = "test_{date:%Y-%m-%d_%H:%M:%S}.png".format(date=datetime.datetime.now())
    return now_png

def write_and_save_txt():
    now_txt = "test_{date:%Y-%m-%d_%H:%M:%S}.txt".format(date=datetime.datetime.now())
    return now_txt
