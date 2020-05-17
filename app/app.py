"""This handles the app logic to serve up APIs and display the app"""
from flask import Flask, render_template

APPLICATION = Flask("personal-website")


@APPLICATION.route("/", methods=["GET"])
def home_page():
    """This method handles serving up the main home page of the website"""
    return render_template("home.html")


@APPLICATION.route('/projects', methods=["GET"])
def projects_page():
    projects = {
        "Who's That Pokémon": "http://whos-that-pokemon.raghav-nair.com/",
        "View For Donations": "http://donate-to-charity.raghav-nair.com/",
        "Introduction To Python": "https://github.com/nairraghav/Introduction-To-Python"
    }
    return render_template("items.html", page_title="Personal Projects", items=projects)


@APPLICATION.route('/resume', methods=["GET"])
def resume_page():
    return render_template("resume.html")
