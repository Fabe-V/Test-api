from flask import *
import json, time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def website():
    data_set = {'Page': 'Website', 'URL': 'none', 'Server': 'local.host', 'Time': time.time()}
    json_output = json.dumps(data_set)

    return json_output


@app.route('/user/', methods=['GET'])
def user_date():
    user_query = str(request.args.get('user'))  # /user/?user=User

    user_data = {'Page': 'user_data', 'URL': 'https', 'Server': 'local.host', 'User': f'{user_query}'}
    json_output = json.dumps(user_data)

    return json_output


if __name__ == '__main__':
    app.run(port=2001)
