import datetime
import pandas as pd

def publication_score(url_list):
    """Returns a list of scores (integers) based on a list of
    sites giving reviews.
    """
    url_rating = [None] * len(url_list)
    for i in range(len(url_list)):
        if url_list[i] == 'amny':
            url_rating[i] = 5
        elif url_list[i] == 'delish':
            url_rating[i] = 15
        elif url_list[i] == 'departures':
            url_rating[i] = 5
        elif url_list[i] == 'eater':
            url_rating[i] = 15
        elif url_list[i] == 'edgeofthecityblog':
            url_rating[i] = 5
        elif url_list[i] == 'grubstreet':
            url_rating[i] = 15
        elif url_list[i] == 'guide':
            url_rating[i] = 20
        elif url_list[i] == 'nytimes':
            url_rating[i] = 20
        elif url_list[i] == 'seriouseats':
            url_rating[i] = 15
        elif url_list[i] == 'theinfatuation':
            url_rating[i] = 15
        elif url_list[i] == 'tripsavvy':
            url_rating[i] = 20
        elif url_list[i] == 'vice':
            url_rating[i] = 20
        else:
            url_rating[i] = 10
            
    return url_rating

def author_scores(df):
    
    """Returns a list of scores based on the dataframe columns
    'author_1', 'author_2', 'author_3', 'author_4', 'author_5'
    """
    
    df = df[['author_1', 'author_2', 'author_3', 'author_4', 'author_5']]
    
    df.fillna('', inplace = True)

    col = df.columns

    author_score = [0] * len(df)
    anony_writers = ['Time Out contributors', 'Foursquare City Guide', 'Edge of the City', 'Team Infatuation', 'Munchies Staff', ]

    for j in range(len(df)):
        for i in range(len(col)):
            if len(df[col[i]][j]) > 1:
                author_score[j] += 3
                if df[col[i]][j] == 'Robert Sietsema':
                    author_score[j] += 17
                elif df[col[i]][j] == 'Pete Wells':
                    author_score[j] += 17
                elif df[col[i]][j] not in [anony_writers]:
                    author_score[j] += 1

    for k in range(len(author_score)):
        if 0 < author_score[k] < 10:
            author_score[k] = 10

    return author_score

def time_score(df):
    
    """Returns a list of scores.
    
    The time score assigns a value to how recently a review
    was written or was updated. The dataframe needs to have
    a list of dates in the columns 'pub_date' and 'mod_date'.
    """
    
    df.pub_date = pd.to_datetime(df.pub_date)

    df.mod_date.fillna(df.pub_date, inplace = True)

    d0 = datetime.datetime(2010, 1, 1)
    d1 = datetime.datetime(2018, 7, 1) 
    d2 = datetime.datetime(2018, 4, 1) 
    d3 = datetime.datetime(2018, 1, 1) 
    d4 = datetime.datetime(2017, 10, 1) 
    d5 = datetime.datetime(2017, 7, 1) 
    d6 = datetime.datetime(2017, 4, 1) 
    d7 = datetime.datetime(2017, 1, 1) 
    d8 = datetime.datetime(2016, 10, 1) 
    d9 = datetime.datetime(2016, 7, 1) 
    d10 = datetime.datetime(2016, 4, 1) 
    d11 = datetime.datetime(2016, 1, 1) 
    
    df.mod_date.fillna(d0, inplace = True)

    df.mod_date = pd.to_datetime(df.mod_date, utc = True)

    dates = df.mod_date
    
    time_score = [0] * len(dates)
    
    for i in range(len(dates)):
        if dates[i].replace(tzinfo=None) > d1:
            time_score[i] += 20
        elif dates[i].replace(tzinfo=None) > d2:
            time_score[i] += 19
        elif dates[i].replace(tzinfo=None) > d3:
            time_score[i] += 18
        elif dates[i].replace(tzinfo=None) > d4:
            time_score[i] += 17
        elif dates[i].replace(tzinfo=None) > d5:
            time_score[i] += 16
        elif dates[i].replace(tzinfo=None) > d6:
            time_score[i] += 15
        elif dates[i].replace(tzinfo=None) > d7:
            time_score[i] += 14
        elif dates[i].replace(tzinfo=None) > d8:
            time_score[i] += 13
        elif dates[i].replace(tzinfo=None) > d9:
            time_score[i] += 12
        elif dates[i].replace(tzinfo=None) > d10:
            time_score[i] += 11
        elif dates[i].replace(tzinfo=None) > d11:
            time_score[i] += 10
        else:
            time_score[i] += 5
            
    return time_score

def domain_clean(df):
    """Looks for a column 'feature_url' in the dataframe,
    strips out anything but the domain name. It also
    works around Eater's ny.eater.com domain.
    
    Returns the dataframe with a new 'site' column,
    removes the 'feature_url' column.
    """

    domains = df.feature_url.copy()
    
    for i in range(len(domains)):
        domains[i] = domains[i].replace('https://www.', '')
        domains[i] = domains[i].replace('http://www.', '')
        domains[i] = domains[i].replace('https://', '')
        domains[i] = domains[i].replace('http://', '')
        domains[i] = domains[i].split('.')[0]
        if domains[i] == 'ny':
            domains[i] = 'eater'
            
    df['site'] = domains
    
    df.drop('feature_url', axis = 1, inplace = True)
    
    return df