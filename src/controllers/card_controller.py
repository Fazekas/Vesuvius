from flask import request, jsonify, Blueprint, send_file

# from ..entities import card_entity
# from ..schemas import card_schema
# from ..dbms.rdb import db

from ..services import card_service

card_blueprint = Blueprint("card", __name__, url_prefix="/card")


# Create a Card mutation
@card_blueprint.route("/card", methods=["POST"])
def add_card():
    return card_service.add_card()


# # Get all cards query
@card_blueprint.route("/cards", methods=["GET"])
def get_cards():
    return card_service.get_cards()


# # Get card query
@card_blueprint.route("/card/<card_id>", methods=["GET"])
def get_card(card_id):
    return card_service.get_card(card_id)


# # Update a card mutation
@card_blueprint.route("/card/<card_id>", methods=["PUT"])
def update_card(card_id):
    return card_service.update_card(card_id)


# # Delete a card mutation
@card_blueprint.route("/card/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    return card_service.delete_card(card_id)


# Test route that returns a picture
@card_blueprint.route("/", methods=["GET"])
def get():
    return card_service.get_card()
