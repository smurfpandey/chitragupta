"""Game & related models"""

from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID, JSONB

from chitragupta.extensions import db

class Game(db.Model):
    """Game model"""
    __tablename__ = "games"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    metadata = db.Column(JSONB)

class GamePlayActivity(db.Model):
    """Model to record Game played activity"""
    __tablename__ = "games_activity"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)
    game = db.Column(UUID(as_uuid=True), nullable=False, db.ForeignKey(Game.id, ondelete='CASCADE')))
    start_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    stop_datetime = db.Column(db.DateTime, nullable=True)
    duration_in_sec = db.Column(db.Integer, default=0)
