import pandas as pd
import requests
from datetime import datetime

# request the data
def get_fast_moves():
    fast_moves_url = "https://pogoapi.net/api/v1/fast_moves.json"
    return pd.json_normalize(requests.get(fast_moves_url).json()), datetime.now()

my_fast_moves, created_at = get_fast_moves()

# index config
my_fast_moves.index.name = 'id'
my_fast_moves.index += 1

# set new columns
my_fast_moves['total_damage'] = my_fast_moves['power']*my_fast_moves['duration']
my_fast_moves['created_at'] = created_at.strftime("%Y-%m-%d %H:%M:%S")

# save only required columns
my_columns = ['stamina_loss_scaler', 'name', 'power', 'duration', 
              'energy_delta', 'type', 'total_damage', 'created_at']
my_fast_moves.to_csv('pokemon.csv', index = True, header = True, columns = my_columns)