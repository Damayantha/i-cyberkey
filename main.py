from flask import *
import json

app = Flask(__name__)


@app.route('/stickers/', methods=['GET'])
def request_sticker_pack():
    query = str(request.args.get('stickers'))  # /stickers/?sticker=bird
    try:
        with open(f'{query}.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError as err:
        data = "No such a file"

    return json.dumps(data)


if __name__ == '__main__':
    app.run()
