"""
Pickem ETL
Author: Gabe Baduqui

Extract TeamID from a given Game ID from a given HREF attribute.
"""

def get_team_id(team_href_attr: str):
    """Function that extracts team ID from the given HREF attribute
       Accepts `team_href_attr`: String 
       Returns `team_id`: String"""
    # Example `team_href_attr` string: 'https://www.espn.com/college-football/team/_/id/0000/schoolName-schoolMascot'
    begin_idx = team_href_attr.index('/id/') + 4
    end_idx = team_href_attr.rfind('/')
    team_id = team_href_attr[begin_idx:end_idx]
    return team_id


def get_record_text(record_td: str):
    """Function that extracts the record text from a given TD tag
       Accepts `record_td`: <td> HTML Element String
       Returns `record`: String"""
    # Exampe `record_td` string: '<div class="fw-bold clr-gray-01 Table__TD">...</div>'
    try:
        record_text = record_td.find('span').text
    except:
        record_text = None
    return record_text

def get_conference_record(team_standing_row: str):
    """Function that extracts the conference record from a given TR tag
       Accepts `team_standing_row`: <tr> HTML Element String
       Returns `conference_record`: String"""
    # Example `team_standing_row` string: '<div class="Table__TR Table__TR--sm Table__even">...</div>'
    try:
        conf_record_td = team_standing_row.find_all('td')[1]
        conf_record = get_record_text(conf_record_td)
    except:
        conf_record = None
    return conf_record

def get_overall_record(team_standing_row: str):
    """Function that extracts the overall record from a given TR tag
       Accepts `team_standing_row`: <tr> HTML Element String
       Returns `overall_record`: String"""
    # Example `team_standing_row` string: '<div class="Table__TR Table__TR--sm Table__even">...</div>'
    try:
        overall_record_td = team_standing_row.find_all('td')[2]
        overall_record = get_record_text(overall_record_td)
    except:
        overall_record = None
    return overall_record