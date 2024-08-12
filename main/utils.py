import string
import random

from main.static import SHORT_URL_LENGTH


def random_url(length=SHORT_URL_LENGTH):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
