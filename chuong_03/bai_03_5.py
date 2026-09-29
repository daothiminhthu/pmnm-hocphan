from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class ListConverter(BaseConverter):
    regex = r"-?\d+(,-?\d+)*"

    def to_python(self, value):
        return [int(x) for x in value.split(",")]

    def to_url(self, values):
        return ",".join(str(x) for x in values)


app.url_map.converters["list"] = ListConverter


@app.route("/sum/<list:numbers>")
def sum_numbers(numbers):
    return {
        "numbers": numbers,
        "sum": sum(numbers)
    }


@app.route("/")
def index():
    return url_for("sum_numbers", numbers=[4, 5, 6])