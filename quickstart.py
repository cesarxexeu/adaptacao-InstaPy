""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(username="__venus_light__",
                  password="xazam123",
                  headless_browser=False)

with smart_run(session):
    # general settings
    session.set_user_interact(amount=4,
                        percentage=63,
                        randomize=True)
    session.set_do_follow(enabled=True, percentage=90,times=1)
    session.set_comments(comments=["legal","massa","top"])
    session.set_do_comment(enabled=True, percentage=25)

    # activity
    #session.interact_user_followers(['0_1_0_0_1_1_0_1','razerbrasil'], amount=200, randomize=True)
    session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM", unfollow_after=1*60*60, sleep_delay=655)

