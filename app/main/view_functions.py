"""Functions which map to views."""
from app import db

from flask import jsonify

from internal.errors import HTTPException
from internal.helper import (
    json_from_request,
    check_keys
)

from .models import User


def user_authenticate(request):
    """Validate a user's credentials."""
    json_data = json_from_request(request)
    expected_keys = ['email', 'password']

    check_keys(expected_keys, json_data)

    user = User.query.filter_by(email=json_data['email']).first()
    if user is not None and user.check_password_hash(json_data['password']):
        return jsonify(user.to_dict()), 200
    else:
        raise HTTPException(
            409,
            {'email': ['Invalid email or password.']}
        )


def user_create(request):
    """User creation."""
    json_data = json_from_request(request)

    expected_keys = [
        "email",
        "password",
        "first_name",
        "last_name"
    ]

    check_keys(expected_keys, json_data)

    user = User()
    for key in expected_keys:
        value = json_data.get(key)
        setattr(user, key, value)

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201
