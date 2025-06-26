from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from server.app import db

appearance_bp = Blueprint('appearance', __name__, url_prefix='/appearances')

@appearance_bp.route('/', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')

    if not all([rating, guest_id, episode_id]):
        return jsonify({'message': 'Missing required fields'}), 400

    if not Guest.query.get(guest_id):
        return jsonify({'message': 'Guest not found'}), 404

    if not Episode.query.get(episode_id):
        return jsonify({'message': 'Episode not found'}), 404

    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(appearance)
    db.session.commit()

    return jsonify({
        'id': appearance.id,
        'rating': appearance.rating,
        'guest_id': appearance.guest_id,
        'episode_id': appearance.episode_id
    }), 201