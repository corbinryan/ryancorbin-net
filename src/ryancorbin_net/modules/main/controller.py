from flask import render_template

class MainController:
    def index(self):
        return render_template("main/index.html", title="Welcome to RyanCorbin.net")

    def resume(self):
        return render_template("main/resume.html", title="Ryan Corbin - Resume")
