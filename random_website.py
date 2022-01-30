import random
import webbrowser

sites = ['iti.com', 'google.com', 'youtube.com', 'freecodecamp.com', 'stackoverflow.com']


def random_site():
    site = sites[random.randint(0, 4)]
    return site


if __name__ == "__main__":
    url = random_site()
    webbrowser.open(url, new=0, autoraise=True)

