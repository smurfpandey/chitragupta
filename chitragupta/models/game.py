"""Game & related models"""
from datetime import datetime
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.hybrid import hybrid_property

from chitragupta.extensions import db

class Game(db.Model):
    """Game model"""
    __tablename__ = "games"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    attributes = db.Column(JSONB)
    plays = db.relationship('GamePlayActivity', lazy=True)

    @hybrid_property
    def total_play_time(self):
        """Total play time for the game in secs"""
        return sum(play.duration_in_sec for play in self.plays)

    @total_play_time.expression
    def total_play_time(cls):
        return (
            db.select([db.func.sum(GamePlayActivity.duration_in_sec)]).
                where(GamePlayActivity.game == cls.id).
                    label('total_play_time')
        )

class GamePlayActivity(db.Model):
    """Model to record Game played activity"""
    __tablename__ = "games_activity"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)
    game = db.Column(UUID(as_uuid=True), db.ForeignKey(Game.id, ondelete='CASCADE'), nullable=False)
    start_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    stop_datetime = db.Column(db.DateTime, nullable=True)
    duration_in_sec = db.Column(db.Integer, default=0)
