import pandas as pd
import datetime

from nba_api.stats.endpoints import scoreboardv2
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.live.nba.endpoints import playbyplay

pd.options.display.max_columns = 999

# today = datetime.datetime.today().strftime('%m/%d/%Y')
# tomorrow = datetime.datetime.today()
# tomorrow = tomorrow + datetime.timedelta(days=1)
# tomorrow = tomorrow.strftime('%m/%d/%Y')
# gameFinder = leaguegamefinder.LeagueGameFinder(
#                               date_from_nullable='10/30/2022',
#                               date_to_nullable='10/30/2022',
#                               )

# gamedf = gameFinder.get_data_frames()

# score = scoreboardv2.ScoreboardV2(
#                                   day_offset='0',
#                                   game_date='10/30/2022',
#                                   league_id='00',
#                                   )

# scoredf = score.line_score.get_data_frame()

# print(scoredf)

pbp = playbyplay.PlayByPlay(
                            game_id='0022200094'
                            )

df = pbp.actions.data
df = pd.DataFrame.from_dict(df)
df.to_csv('pbp.csv')