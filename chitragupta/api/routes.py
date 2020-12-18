# -*- coding: utf-8 -*-
"""API routes."""
from flask import (
    Blueprint,
    current_app,    
    jsonify,
    request,
    url_for,
)

from chitragupta.api.game import create_game_start_activity, mark_game_stop_activity

blueprint = Blueprint("api", __name__, url_prefix="/api")

@blueprint.route("/games", methods=["GET"])
def games():
    """Games Activity."""

    return {"msg": "ok"}

@blueprint.route("/games", methods=["POST"])
def create_game_activity():
    """Create a Game activity."""    
    req_data = request.json
    current_app.logger.info('Creating new game activity')

    activity = req_data['activity'].lower()

    if activity == "start":
        create_game_start_activity(req_data)
    elif activity == "stop":
        mark_game_stop_activity(req_data)
    else:
        current_app.logger.warn('Invalid activity provided')
        return jsonify({ "status": "BAD_REQUEST", "message": "Invalid activity"}), 400


    return {"msg": "ok"}
