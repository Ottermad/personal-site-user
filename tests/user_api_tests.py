"""User API tests."""
from app import db, create_app
from app.main.models import User

from internal.test import APITestCase
from internal.test.factories.user import UserFactory

import json

user_factory = UserFactory()


class UserAPITests(APITestCase):
    """User API tests."""

    def setUp(self):
        """Pass db and create_app to parent setUP method."""
        super(UserAPITests, self).setUp(db, create_app)

    def test_user_create(self):
        """Test whether User can be created."""
        user = user_factory.new()

        response = self.client.post(
            '/user',
            data=json.dumps(user),
            headers={'Content-Type': 'application/json'}
        )

        self.assertEqual(response.status_code, 201)
        user_from_db = User.query.filter_by(email=user['email']).first()
        self.assertIsNotNone(user_from_db)
