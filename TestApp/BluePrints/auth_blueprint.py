from flask import Blueprint, request

auth_views=Blueprint("auth", __name__)

@auth_views.route("/register", strict_slashes=False, methods=["GET","POST"])
def register():
    if request.method=="POST":
        return "<h1>After Registration<h1>"
    return "<h1>This is Registration Page<h1>"

@auth_views.route("/login",strict_slashes=False, methods=["GET","POST"])
def login():
    if request.method=="POST":
        return "<h1>After Login<h1>"
    return "<h1>Here goes the Login Page<h1>"