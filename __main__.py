"""
CFB Pickem ETL
Author: Gabe Baduqui

Scrape, transform and load college football and NFL schedule data from various web pages
"""
import etl.extract.extract as ext
import etl.transform.transform as trf
import etl.load.load as load

def main():
    #cfb_games_raw, cfb_teams_raw, cfb_locations_raw = ext.full_extract('CFB', 2024, 15)
    #nfl_games_raw, nfl_teams_raw, nfl_locations_raw = ext.full_extract('NFL', 2024, 18)

    #cfb_games, cfb_teams, cfb_locations = trf.full_transform('CFB', cfb_games_raw, cfb_teams_raw, cfb_locations_raw)
    #nfl_games, nfl_teams, nfl_locations = trf.full_transform('NFL', nfl_games_raw, nfl_teams_raw, nfl_locations_raw)

    #load.full_load('CFB', cfb_games, cfb_teams, cfb_locations)
    #load.full_load('NFL', nfl_games, nfl_teams, nfl_locations)

    mlb_games_raw, mlb_teams_raw, mlb_locations_raw = ext.full_extract('MLB')
    mlb_games, mlb_teams, mlb_locations = trf.full_transform('MLB', mlb_games_raw, mlb_teams_raw, mlb_locations_raw)
    load.full_load('MLB', mlb_games, mlb_teams, mlb_locations)

if __name__ == '__main__':
    main()
