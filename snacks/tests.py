from django.test import TestCase

# Create your tests here.
# Tested using httpie http POST :8000/api/token/ username=admin password=admin command
# to get access and refresh tokens
# Formatted the bearer to accept post

# Got the below credentials required when not logged in
# "detail": "Authentication credentials were not provided."

# Did docker-compose down and docker-compose up to test database persistence.