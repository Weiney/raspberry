import random

from flask import current_app
import os
from uuid import uuid4


def get_data_path(file_dir="img"):
    data_path = os.path.join(current_app.root_path, current_app.config.get("DATA_DIR"))
    file_path = os.path.join(data_path, file_dir)
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    return file_path


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid4().hex + ext
    return new_filename


def randon_code(length=4):
    a = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    b = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    c = [str(x) for x in range(10)]
    d = a + b + c
    rt = ""
    for _ in range(length):
        rt += random.choice(d)
    return rt
