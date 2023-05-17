"""Setup at app startup"""

from flask import Flask
import psycopg2
from site.views import app

app = Flask(__name__)
postgres = psycopg2.connect(
    host="dpg-chi7kmu4dadc9vlu2pr0-a.oregon-postgres.render.com",
    database="todo_ix3c",
    user="root",
    password="LMNxpNiO0RgPl1WB5GeSAFEAaKWYCmnE")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position

from app import routes
