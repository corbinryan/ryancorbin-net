from flask import render_template

class MainController:
    def index(self):
        return render_template("main/index.html", title="Welcome to RyanCorbin.net")
