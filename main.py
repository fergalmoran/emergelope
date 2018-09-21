import json
import os
from urllib.request import urlopen

from flask import Flask, jsonify, render_template
from twilio.rest import Client

from data_store import save_number

app = Flask(__name__)
account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
call_xml = os.environ['CALL_XML']
to_numbers = os.environ['NUMBER_LIST']
from_number = os.environ['FROM_NUMBER']


def parse_json():
    json_url = urlopen(to_numbers)

    text = json.loads(json_url.read())
    return text


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/debug')
def debug():
    return jsonify(
        {
            'account_sid': account_sid,
            'auth_token': auth_token,
            'call_xml': call_xml,
            'to_numbers': to_numbers,
            'from_number': from_number
        }
    )


@app.route('/3c9d6880-107b-4c03-8356-2778b7bd8209')
def initiate_cluster_fuck():
    return

    client = Client(account_sid, auth_token)
    sids = []
    numbers = parse_json()
    for number in numbers:
        try:
            sids.append(
                client.calls.create(
                    to=number,
                    from_=from_number,
                    url=call_xml,
                    method='GET'
                )
            )
        except:
            print('Error sending message')

    return "Succeeded"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
