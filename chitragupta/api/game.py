"""Methods for Game & related resource"""
from datetime import datetime

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
            metadata=game_activity['game']
        )
        db.session.add(this_game)
        db.session.commit()

    # Create GamePlayActivity
    play_activity = GamePlayActivity(
        game=this_game.id,
        start_datetime=datetime.utcnow()
    )

    return True

def mark_game_stop_activity():
    """Mark previous game play as complete"""

    # Find a latest start activity for this game
    # Mark it as complete