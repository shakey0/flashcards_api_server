from flask import Blueprint, request, redirect, url_for, session, jsonify
from .. import oauth
import os

auth_blueprint = Blueprint('auth', __name__)


# Oauth setup goes here
