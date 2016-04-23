from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")


@app.route("/application-form", methods=["GET"])
def application_form():
    """Show an application form"""

    return render_template("application-form.html")


if __name__ == "__main__":
    app.run(debug=True)
