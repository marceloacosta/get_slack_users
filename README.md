# Slack Users List

This script retrieves a list of users from your Slack workspace and saves their IDs and names to a CSV file.

## Requirements

- Python 3.6 or later
- [slack-sdk](https://github.com/slackapi/python-slack-sdk) package
- [python-dotenv](https://github.com/theskumar/python-dotenv) package

Install the required packages with the following command:

pip install slack-sdk python-dotenv

## Setup
Create a Slack app and install it in your workspace. Follow the instructions here to create a Slack app and obtain a SLACK_API_TOKEN with the necessary scopes.

Create a .env file in the same directory as your script and add the following line:


SLACK_API_TOKEN=xoxb-your-token-here

Replace your-token-here with the actual Slack API token.

Make sure your Slack app has the following permission scopes:

users:read: To read user information, such as names and IDs.
Usage
After setting up the Slack app and obtaining the SLACK_API_TOKEN, run the script:


python slack_users_list.py

The script will save the users' IDs and names to a CSV file named slack_users.csv.