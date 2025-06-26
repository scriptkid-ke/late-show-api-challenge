from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.app import db

episode_bp = Blueprint('episode', __name__, url_prefix='/episodes')

@episode_bp.route('/', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{'id': episode.id, 'date': episode.date.isoformat(), 'number': episode.number} for episode in episodes]), 200

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [{
        'id': appearance.id,
        'rating': appearance.rating,
        'guest': {
            'id': appearance.guest.id,
            'name': appearance.guest.name,
            'occupation': appearance.guest.occupation
        }
    } for appearance in episode.appearances]

    return jsonify({
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number,
        'appearances': appearances
    }), 200

@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode deleted successfully'}), 200