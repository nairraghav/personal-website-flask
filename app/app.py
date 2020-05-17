"""This handles the app logic to serve up APIs and display the app"""
from flask import Flask, render_template

APPLICATION = Flask("personal-website")


@APPLICATION.route("/", methods=["GET"])
def home_page():
    """This method handles serving up the main home page of the website"""
    return render_template("home.html")


@APPLICATION.route('/career', methods=["GET"])
def careers_page():
    careers = {
        "The Pokémon Company International": "https://www.pokemon.com/us/",
        "The Walt Disney Company": "https://www.disney.com/",
        "Starbucks": "https://www.starbucks.com/",
        "Airbiquity": "https://www.airbiquity.com/",
        "Apollo Education Group": "https://www.apollo.edu/",
        "PointInside": "https://www.pointinside.com/"
    }
    return render_template("items.html", page_title="Careers", items=careers)


@APPLICATION.route('/projects', methods=["GET"])
def projects_page():
    projects = {
        "Who's That Pokémon": "https://whispering-cove-17469.herokuapp.com/",
        "View For Donations (TBD)": "",
        "Introduction To Python": "https://github.com/nairraghav/Introduction-To-Python"
    }
    return render_template("items.html", page_title="Personal Projects", items=projects)


@APPLICATION.route('/resume', methods=["GET"])
def resume_page():
    return render_template("resume.html")
