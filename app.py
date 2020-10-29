import os
from flask import Flask, render_template
import requests

app = Flask("name-gathering")

@app.route("/")
def root():

    return render_template("index.html")


@app.route("/getleto/")
def getleto():
    url = f"https://api.github.com/repos/equinor/gathering-leto"
    repo = requests.get(url).json()
    return repo

@app.route("/getissues/")
def getissues():
    url = f"https://api.github.com/repos/equinor/gathering-leto/issues/0"
    res = requests.get(url).json()
    return res

@app.route("/getrepos/")
def getrepos():
    url = f"https://api.github.com/users/markusdregi/repos"
    user_repos = requests.get(url).json()
    return user_repos[0]

@app.route("/getuser/")
def getuser():
    # github username
    username = "markusdregi"
    # url to request
    url = f"https://api.github.com/users/{username}"
    # make the request and return the json
    user_data = requests.get(url).json()
    # pretty print JSON data
    return user_data


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
