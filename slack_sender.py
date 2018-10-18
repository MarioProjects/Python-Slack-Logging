# API info: https://pypi.org/project/slackclient/
# pip install slackclient
from slackclient import SlackClient
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Push Notificator with Slack by Mario Parren~o. Msc student Universidad Politecnica de Valencia maparla@inf.upv.es . Enjoy!')
    parser.add_argument('--slack_token', type=str, required=True, help='The message to send.')
    parser.add_argument('--msg', type=str, required=True, help='The message to send.')
    parser.add_argument('--channel', type=str, default='log_ai', help='The slack channel where we send the message.')
    aux=parser.parse_args()
    arguments=list()
    arguments=[aux.slack_token, aux.msg, aux.channel]
    return arguments

slack_token, msg, channel = parse_args()

def slack_message(slack_token, message, channel):
    token = slack_token
    sc = SlackClient(token)
    sc.api_call('chat.postMessage', channel=channel, 
                text=message, username='My Sweet Bot',
                icon_emoji=':robot_face:')

slack_message(slack_token, msg, channel)

