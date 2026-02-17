"""
News service for fetching historical events from Wikipedia.
"""
import requests
from datetime import datetime


class NewsService:
    """Fetches 'On This Day' events from Wikipedia API"""

    def __init__(self):
        self.wiki_base_url = "https://en.wikipedia.org/api/rest_v1/feed/onthisday/events"
        self.headers = {
            "User-Agent": "TheOldTimesAI/1.0 (Email: ofir08@gmail.com)"
        }

    def get_todays_events(self):
        """
        Fetch events that happened on this day in history.
        Returns list of event dicts with: year, title, date
        """
        today = datetime.now()
        month = today.strftime("%m")  # "02"
        day = today.strftime("%d")    # "17"

        url = f"{self.wiki_base_url}/{month}/{day}"

        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()

            data = response.json()
            events = []

            if 'events' in data:
                # Get ALL events (no limit)
                for event in data['events']:
                    events.append({
                        'year': event.get('year', 'Unknown'),
                        'title': event.get('text', 'No description'),
                        'date': today.strftime("%b %d")
                    })

            return events

        except Exception as e:
            print(f"Error fetching news: {e}")
            return []
