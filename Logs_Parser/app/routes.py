'''
Author: Rishabh Sharma

'''

from app.connector import function1, function2
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/index", methods=["POST", "GET"])
def user_defined_function():
    message = {}
    message1 = {}

    if request.method == "POST":
        log_string = request.form["text"]
        target_name = request.form["target"]
        message["log_string"] = log_string
        message["target_name"] = target_name

        result_dict, result_dict1 = function1(log_string)

        if result_dict == "No violations":
            message["no_voil"] = "Noviolations"
        elif target_name == "unknown":
            result_dict["BPM"] = ["Unknown", "Target name is not provided"]
            message["results"] = result_dict
            message1 = result_dict1
        else:
            function2(result_dict, target_name)
            message["results"] = result_dict
            message1 = result_dict1
            return render_template("index.html", message=message, message1=message1)

    return render_template("index.html", message=message, message1=message1)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
