from server.app import create_app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date

app = create_app()

def seed_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create test user
        user = User(username='testuser')
        user.set_password('testpass')
        db.session.add(user)

        # Create guests
        guests = [
            Guest(name='John Doe', occupation='Actor'),
            Guest(name='Jane Smith', occupation='Musician'),
            Guest(name='Bob Johnson', occupation='Comedian')
        ]
        db.session.add_all(guests)

        # Create episodes
        episodes = [
            Episode(date=date(2023, 1, 1), number=101),
            Episode(date=date(2023, 1, 2), number=102),
            Episode(date=date(2023, 1, 3), number=103)
        ]
        db.session.add_all(episodes)

        # Create appearances
        appearances = [
            Appearance(rating=4, guest_id=1, episode_id=1),
            Appearance(rating=5, guest_id=2, episode_id=1),
            Appearance(rating=3, guest_id=3, episode_id=2),
            Appearance(rating=5, guest_id=1, episode_id=3)
        ]
        db.session.add_all(appearances)

        db.session.commit()

if __name__ == '__main__':
    seed_data()
    print("Database seeded successfully!")