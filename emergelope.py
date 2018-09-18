import os

from flask import Flask, jsonify
from twilio.rest import Client

app = Flask(__name__)
account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
call_xml = os.environ['CALL_XML']
to_numbers = os.environ['NUMBER_LIST']
from_number = os.environ['FROM_NUMBER']


@app.route('/')
def home():
    return 'EmerGELOPE'


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
    client = Client(account_sid, auth_token)
    sids = []
    for number in to_numbers.split(','):
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

    return sids


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
