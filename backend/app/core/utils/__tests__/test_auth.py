from django.test import TestCase
from datetime import timedelta
from ..auth import (
    hash_password,
    compare_passwords,
    create_access_token,
    decode_access_token,
)


class AuthUtilsTests(TestCase):
    def test_hash_passwords(self):
        password = "smile"
        hashed_password = hash_password(password)
        self.assertIsNotNone(hashed_password)
        self.assertNotEqual(password, hashed_password)

    def test_compare_passwords(self):
        password = "smile"
        hashed_password = hash_password(password)
        self.assertTrue(compare_passwords(password, hashed_password))
        wrong_passwords = ["smile123", "password", "Smile", ""]
        for wrong_password in wrong_passwords:
            self.assertFalse(compare_passwords(wrong_password, hashed_password))

    def test_create_decode_access_token(self):
        user_id = "dummy_id"
        token = create_access_token(user_id)
        decoded_user_id = decode_access_token(token)
        self.assertEqual(user_id, decoded_user_id)

    def test_expired_token_returns_none(self):
        token = create_access_token("dummy_id", expires_delta=timedelta(seconds=-1))
        assert decode_access_token(token) is None

    def test_invalid_token_returns_none(self):
        invalid_token = "not.a.valid.jwt"
        assert decode_access_token(invalid_token) is None
