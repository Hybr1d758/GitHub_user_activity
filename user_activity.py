import requests
import argparse

def fetch_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    username  = "Hybr1d758"
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for user {username}")
        return None

def display_activity(events):
    if events:
        for event in events:
            print(f"{event['type']} at {event['created_at']}")
    else:
        print("There are no logged events for this user")

def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub user activity")
    parser.add_argument("username", help="GitHub username")
    args = parser.parse_args()

    events = fetch_user_activity(args.username)
    display_activity(events)

if __name__ == "__main__":
    main()