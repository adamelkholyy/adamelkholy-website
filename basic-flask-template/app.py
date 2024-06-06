#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Peter Simeth's basic flask pretty youtube downloader (v1.3)
https://github.com/petersimeth/basic-flask-template
© MIT licensed, 2018-2023
"""

from flask import Flask, render_template

DEVELOPMENT_ENV = True

app = Flask(__name__)

app_data = {
    "name": "Adam's Webpage",
    "description": "Adam's Website",
    "author": "Adam El Kholy and Peter Simeth",
    "html_title": "Adam's Website",
    "project_name": "Adam's Website",
    "keywords": "flask, webapp, template, basic",
}


#TODO
# Retitle 
# Go over github + properly display diss and prev projects with descriptions and downlaod links 
# Homepage 
# Reading/Essays section ? 
# Add in python game for artwork model 

@app.route("/")
def index():
    return render_template("index.html", app_data=app_data)


@app.route("/projects")
def about():
    return render_template("projects.html", app_data=app_data)


@app.route("/links")
def service():
    return render_template("links.html", app_data=app_data)


@app.route("/reading")
def contact():
    return render_template("reading.html", app_data=app_data)


if __name__ == "__main__":
    app.run(debug=DEVELOPMENT_ENV)
