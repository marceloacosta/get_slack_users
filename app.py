import os
import csv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

def get_slack_users():
    try:
        response = client.users_list()
        users = []
        for member in response['members']:
            if not member['is_bot'] and not member['deleted']:
                user_id = member['id']
                user_name = member['profile']['real_name_normalized']
                users.append((user_id, user_name))
        return users
    except SlackApiError as e:
        print(f"Error: {e}")
        return []

def save_users_to_csv(users, output_file):
    with open(output_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['user_id', 'user_name'])
        for user in users:
            writer.writerow(user)

users = get_slack_users()
save_users_to_csv(users, 'slack_users.csv')
