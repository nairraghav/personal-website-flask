"""This handles the app logic to serve up APIs and display the app"""
from flask import Flask, render_template

APPLICATION = Flask("personal-website")


@APPLICATION.route("/", methods=["GET"])
def home_page():
    """This method handles serving up the main home page of the website"""
    return render_template("index.html")
