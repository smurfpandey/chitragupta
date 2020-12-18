"""Methods for Game & related resource"""
from datetime import datetime

from flask import current_app

from chitragupta.extensions import db
from chitragupta.models.game import Game, GamePlayActivity

def create_game_start_activity(game_activity):
    """Create new game play activity"""
    # Check if this is a new game
    game_name = game_activity['game']['Name']
    this_game = Game.query.filter_by(name=game_name).first()
    if this_game is None:
        this_game = Game(
            name=game_name,
            attributes=game_activity['game']
        )
        db.session.add(this_game)
        db.session.commit()

    # Create GamePlayActivity
    play_activity = GamePlayActivity(
        game=this_game.id,
        start_datetime=datetime.utcnow()
    )
    db.session.add(play_activity)
    db.session.commit()

    return True

def mark_game_stop_activity(game_activity):
    """Mark previous game play as complete"""
    game_name = game_activity['game']['Name']
    this_game = Game.query.filter_by(name=game_name).first()
    if this_game is None:
        current_app.logger.info('Game not found')
        return False
    
    # Find a latest start activity for this game
    this_play_activity = GamePlayActivity.query.filter_by(game=this_game.id,stop_datetime=None).first()    
    
    if this_play_activity is None:
        current_app.logger.info('No in-game activity found')
        return False

    # Mark it as complete
    this_play_activity.stop_datetime = datetime.utcnow()
    this_play_activity.duration_in_sec = game_activity['elapsed_seconds']

    db.session.commit()
    