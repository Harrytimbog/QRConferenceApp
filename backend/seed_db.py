from app import create_app, db
from models.conference import Conference
from models.user import User
import datetime
import random

app = create_app()

# Sample conference data
conferences = [
    {
        "title": "Tech Conference 2023",
        "description": "A conference about the latest in technology.",
        "date_time": datetime.datetime(2023, 11, 15, 10, 30),
        "venue": "Tech Convention Center",
        "rsvp": "tech-conference-2023.eventbrite.com",
        "image_url": "https://images.unsplash.com/photo-1526045004414-3e7ed02f9ca1?auto=format&fit=crop&q=60&w=800&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y29uZmVyZW5jZSUyMHZlbnVlc3xlbnwwfHwwfHx8MA%3D%3D",
        "url": "https://tech-conference-2023.com",
    },
    {
        "title": "AI Symposium 2023",
        "description": "Deep dives into artificial intelligence and its applications.",
        "date_time": datetime.datetime(2023, 12, 5, 9, 0),
        "venue": "AI Hub Center",
        "rsvp": "ai-symposium-2023.eventbrite.com",
        "image_url": "https://images.unsplash.com/photo-1560439514-e960a3ef5019?auto=format&fit=crop&q=60&w=800&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8Y29uZmVyZW5jZSUyMHZlbnVlc3xlbnwwfHwwfHx8MA%3D%3D",
        "url": "https://ai-symposium-2023.com",
    },
    {
        "title": "Web Development Con 2023",
        "description": "Exploring the modern web technologies and frameworks.",
        "date_time": datetime.datetime(2023, 12, 20, 11, 0),
        "venue": "Web Dev Arena",
        "rsvp": "webdev-con-2023.eventbrite.com",
        "image_url": "https://images.unsplash.com/photo-1559223607-a43c990c692c?auto=format&fit=crop&q=60&w=800&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y29uZmVyZW5jZSUyMHZlbnVlc3xlbnwwfHwwfHx8MA%3D%3D",
        "url": "https://webdev-con-2023.com",
    },
    {
        "title": "Mobile Dev Meet 2023",
        "description": "Best practices in mobile application development.",
        "date_time": datetime.datetime(2023, 11, 28, 10, 0),
        "venue": "Mobile Center",
        "rsvp": "mobile-dev-2023.eventbrite.com",
        "image_url": "https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&q=60&w=800&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fGNvbmZlcmVuY2UlMjB2ZW51ZXN8ZW58MHx8MHx8fDA%3D",
        "url": "https://mobile-dev-2023.com",
    },
    {
        "title": "Cloud and Infrastructure 2023",
        "description": "Scaling and managing modern infrastructure.",
        "date_time": datetime.datetime(2023, 12, 10, 9, 30),
        "venue": "Cloud Palace",
        "rsvp": "cloud-infra-2023.eventbrite.com",
        "image_url": "https://images.unsplash.com/photo-1559223607-b4d0555ae227?auto=format&fit=crop&q=60&w=800&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGNvbmZlcmVuY2UlMjB2ZW51ZXN8ZW58MHx8MHx8fDA%3D",
        "url": "https://cloud-infra-2023.com",
    },
    {
        "title": "Blockchain Summit 2023",
        "description": "Understanding decentralized technologies and cryptocurrencies.",
        "date_time": datetime.datetime(2023, 12, 15, 12, 0),
        "venue": "Crypto Convention Center",
        "rsvp": "blockchain-summit-2023.eventbrite.com",
        "image_url": "https://plus.unsplash.com/premium_photo-1679547203075-0e38c2bc51cc?auto=format&fit=crop&q=60&w=800&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Y29uZmVyZW5jZXxlbnwwfHwwfHx8MA%3D%3D",
        "url": "https://blockchain-summit-2023.com",
    },
    {
        "title": "Design & UX Conference 2023",
        "description": "Mastering user experience in the modern digital age.",
        "date_time": datetime.datetime(2023, 11, 25, 13, 0),
        "venue": "Design Center of Excellence",
        "rsvp": "design-ux-2023.eventbrite.com",
        "image_url": "https://images.unsplash.com/photo-1591115765373-5207764f72e7?auto=format&fit=crop&q=60&w=800&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8Y29uZmVyZW5jZXxlbnwwfHwwfHx8MA%3D%3D",
        "url": "https://design-ux-2023.com",
    },
    {
        "title": "Gaming Expo 2023",
        "description": "Exploring innovations in the gaming industry.",
        "date_time": datetime.datetime(2023, 11, 30, 14, 30),
        "venue": "Gaming Stadium",
        "rsvp": "gaming-expo-2023.eventbrite.com",
        "image_url": "https://plus.unsplash.com/premium_photo-1661952480813-2bb91e2104df?auto=format&fit=crop&q=60&w=800&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGNvbmZlcmVuY2V8ZW58MHx8MHx8fDA%3D",
        "url": "https://gaming-expo-2023.com",
    },
    {
        "title": "Robotics Workshop 2023",
        "description": "Hands-on sessions on building and programming robots.",
        "date_time": datetime.datetime(2023, 12, 1, 9, 30),
        "venue": "Robotics Lab",
        "rsvp": "robotics-workshop-2023.eventbrite.com",
        "image_url": "https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?auto=format&fit=crop&q=60&w=800&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGNvbmZlcmVuY2V8ZW58MHx8MHx8fDA%3D",
        "url": "https://robotics-workshop-2023.com",
    },
    {
        "title": "Space Exploration Con 2023",
        "description": "Discussing advancements in space technology and exploration.",
        "date_time": datetime.datetime(2023, 12, 3, 15, 0),
        "venue": "Space Center Auditorium",
        "rsvp": "space-con-2023.eventbrite.com",
        "image_url": "https://plus.unsplash.com/premium_photo-1679547203121-6fc522271ba8?auto=format&fit=crop&q=60&w=800&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fGNvbmZlcmVuY2V8ZW58MHx8MHx8fDA%3D",
        "url": "https://space-con-2023.com",
    },
]


with app.app_context():
    # Let's fetch a user to associate with these conferences
    # user = User.query.first()
    user = User.query.offset(1).limit(1).first()

    if not user:
        print("No users found in the database! Please create a user first.")
        exit()

    for conf_data in conferences:
        conf = Conference(
            title=conf_data["title"],
            description=conf_data["description"],
            date_time=conf_data["date_time"],
            venue=conf_data["venue"],
            rsvp=conf_data["rsvp"],
            image_url=conf_data["image_url"],
            url=conf_data["url"],
            user_id=user.id,
        )
        db.session.add(conf)

    db.session.commit()
    print(f"Added {len(conferences)} conferences to the database!")
