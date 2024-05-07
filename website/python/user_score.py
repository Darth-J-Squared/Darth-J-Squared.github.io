from flask import Blueprint, request, jsonify
import json
import sys

# Creating a Blueprint object to define API routes
user_score_bp = Blueprint('user_score', __name__)
