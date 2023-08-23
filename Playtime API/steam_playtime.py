from flask import Flask, jsonify
import requests
from decouple import config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def get_game_images(app_ids):
    app_images = {}

    for app_id in app_ids:
        url = f'https://store.steampowered.com/api/appdetails?appids={app_id}'
        response = requests.get(url)
        data = response.json()

        if app_id in data and 'data' in data[app_id] and 'header_image' in data[app_id]['data']:
            app_images[app_id] = data[app_id]['data']['header_image']

    return app_images


@app.route('/playtime')
def get_playtime():
    API_KEY = config('STEAM_API_KEY')
    STEAM_ID = '76561198362405830'

    url = f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={API_KEY}&steamid={STEAM_ID}&include_played_free_game>'
    response = requests.get(url)
    data = response.json()

    playtime_data = {}

    app_ids = {
        '438100': 'vrchat',
        '620980': 'beat_saber'
        # Add more app IDs and names as needed
    }

    for game in data['response']['games']:
        app_id = str(game['appid'])
        if app_id in app_ids:
            playtime_data[app_ids[app_id]] = {
                'playtime': game['playtime_forever']
            }

    game_images = get_game_images(app_ids.keys())
    for app_id, app_name in app_ids.items():
        if app_id in game_images:
            playtime_data[app_name]['image'] = game_images[app_id]

    return jsonify(playtime_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)