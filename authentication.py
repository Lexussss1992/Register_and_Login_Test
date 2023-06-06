import json
from tkinter import *

from canvas import tk
from helpers import clean_screen
from products import render_products

def login(username, pword):
    with open("db/user_credentials_db.txt", "r") as file:
        data = file.readlines()
        for line in data:
            name, password = line[:-1].split(", ")
            if name == username and password == pword:
                with open("db/current_user.txt", "w") as file:
                    file.write(name)
                render_products()
                return
        render_login(error="Invalid username or password")