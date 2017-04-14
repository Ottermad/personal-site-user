"""Views file."""
from flask import Blueprint, request

from .models import *
from .view_functions import user_authenticate, user_create

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route("/")
def index():
    """Index Route."""
    return "Index"


@main_blueprint.route("/user", methods=("POST",))
def user_create_or_list():
    """Create a user or list them."""
    if request.method == "POST":
        return user_create(request)


@main_blueprint.route("/authenticate")
def auth_route():
    """Authenticate a user using an email and password."""
    return user_authenticate(request)
