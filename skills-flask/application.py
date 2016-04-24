from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Show an application form"""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def application_response():
    """Handles submission of a form in application-form.html to the
    route /application"""
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    title = request.form.get("title")
    salary = request.form.get("salary")

    return render_template("application-response.html", firstname=firstname,
                           lastname=lastname, salary=salary, title=title)


if __name__ == "__main__":
    app.run(debug=True)
