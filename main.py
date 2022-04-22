from pprint import pprint
import pandas as pd

from chessdotcom import get_leaderboards


def getList(dict):
    return [*dict]

def show_lbs():
    """ return list of leaderboards
    """
    data = get_leaderboards()
    # pprint(getList(data.json['leaderboards']))

    live_rapid_lbs = data.json['leaderboards']['live_rapid']
    # pprint(live_rapid_lbs)
    return(live_rapid_lbs)

# show_lbs()

def modify_leaders_data(list_of_leaders):
    leaders_modified = []
    keys_to_delete = ['avatar', 'player_id', '@id', 'trend_rank', 'trend_score', 'url', 'username']

    for leader in list_of_leaders:
        for key in keys_to_delete:
            leader.pop(key, None)

        leader['country'] = leader['country'][-2:]

        leaders_modified.append(leader)

    df = pd.DataFrame(leaders_modified)
    pd.to



def get_leaderboard_countries(list_of_lbs):
    lbs_truncated = []
    keys_to_delete = ['avatar', 'player_id', '@id', 'trend_rank', 'trend_score', 'url', 'username']
    for lb in list_of_lbs:
        for key in keys_to_delete:
            lb.pop(key, None)

        try:
            # leader['rank']:
            print(f"{lb['rank']}: {lb['name']} ")
            print('country: ', lb['country'][-2:])
            print(lb['score'])
            print('-------------------------------------------')
        except KeyError:
            pass

# get_leaderboard_countries(show_lbs())

modify_leaders_data(show_lbs())
