from flask import Flask
from BluePrints.main_blueprint import main_views
from BluePrints.auth_blueprint import auth_views

app=Flask(__name__)

# @app.route("/", strict_slashed=False, methods=["GET"])
# def index():
#     return "<h1>This is the Home Page<h1>"

app.register_blueprint(main_views)
app.register_blueprint(auth_views)


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/