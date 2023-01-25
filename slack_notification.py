import json
from slack_sdk import WebClient


def slack_dm(msg="DONE"):
    """Slack sends DM when processing is complete.
    Args:
        msg: content of the message you want to send.

    Returns:
        Nothing.

    Settings:
        1. login https://api.slack.com/apps/
        2. select your workspace
        3. choose a bot (Scopes)
        4. add permission -> im:write
        5. install to workspace
        6. make slack.json
            ex) slack.json
            {"token":"xoxb-999999999999-9999999999999-xxxxxxxxxxxxxxxxxxxxxxxx",
            "user_id":"xxxxxxxxxxx"}
    """

    with open("slack.json", mode="r") as f:
        json_data = json.load(f)

    token = json_data["token"]

    client = WebClient(token)
    user_id = json_data["user_id"]

    res = client.conversations_open(users=user_id)
    dm_id = res['channel']['id']
    client.chat_postMessage(channel=dm_id, text=msg)
