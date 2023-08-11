from flask import Flask, jsonify
import requests
from decouple import config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/playtime')
def get_playtime():
    API_KEY = config('STEAM_API_KEY')
    STEAM_ID = '76561198362405830'

    url = f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={API_KEY}&steamid={STEAM_ID}&include_played_free_game>'
    response = requests.get(url)
    data = response.json()

    playtime_data = {}

    for game in data['response']['games']:
        if game['appid'] == 438100:  # VRChat's app ID
            playtime_data['vrchat'] = game['playtime_forever']
        elif game['appid'] == 620980:  # Beat Saber's app ID
            playtime_data['beat_saber'] = game['playtime_forever']

    return jsonify(playtime_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)