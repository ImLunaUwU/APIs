# Important!
To use this API for yourself, you'll need to set your Steam Web API key (Yes, an API in an API, it's complicated.) in a file called ".env" using the following format:
```
# .env
STEAM_API_KEY=your_api_key_here
```
If you do not have this file in the same directory as the API server, the API will **not** work.

Please note: As provided here, the API will grab both the logo image of the game and playtime in minutes. I am not sure about Steam's API rate limits, so use with caution.

Other than that, have fun.

Example for including the API data on a website has been included in /index.html

Get an API key at https://steamcommunity.com/dev/apikey

If this key gets exposed to the public your Steam account could be in danger. 

Note: Luna is not responsible for your account safety nor does she assure this is allowed to do per Steam's TOS. Luna is ***not*** afiliated with Steam, nor Valve.