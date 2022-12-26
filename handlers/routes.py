from flask import render_template, request
from modules import modules
from flask import request, jsonify
from flask_cors import cross_origin
from modules import modules, cyk

def configure_routes(app):
    @app.route("/")
    def index():
        hello = modules.hello()
        content = modules.content()
        return render_template("index.html", hello=hello, content=content)

    @app.route("/app", methods=["GET", "POST"])
    def app():
        if (request.method == "POST"):
            string = request.form["sentenceinput"]
            result = cyk.getValid(string)
            return render_template("app.html", result=result, submit=True, string=string)
        else:
            return render_template("app.html", submit=False)

        
    
