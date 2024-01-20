"""
Pickem ETL
Author: Gabe Baduqui

Extract TeamID from a given HREF attribute.
"""

def get_team_id(team_href_attr: str):
    """Function that extracts team ID from the given HREF attribute
       Accepts `team_href_attr`: String 
       Returns `team_id`: String"""
    # Example `team_href_attr` string: 'https://www.espn.com/mlb/team/_/name/abbreviation/teamLocation-teamMascot'
    begin_idx = team_href_attr.index('/name/') + 6
    end_idx = team_href_attr.rfind('/')
    team_id = team_href_attr[begin_idx:end_idx]
    return team_id