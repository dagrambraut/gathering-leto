import os
from flask import Flask, render_template
import requests

import github

app = Flask("name-gathering")
g = github.Github()

@app.route("/get_leto_issue_count/")
def get_leto_issue_count():

    repo = g.get_repo("equinor/gathering-leto")
    issues = repo.get_issues()

    return str(issues.totalCount)

@app.route("/")
def root():
    return render_template("index.html", issue_count = get_leto_issue_count())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
