import datetime

def publication_sort(url_list):
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
        elif url_list[i] == 'foursquare':
            url_rating[i] = 10
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
        elif url_list[i] == 'timeout':
            url_rating[i] = 10
        elif url_list[i] == 'tripsavvy':
            url_rating[i] = 20
        elif url_list[i] == 'vice':
            url_rating[i] = 20
        else:
            url_rating[i] = 10
            
    return url_rating

def author_scores(df):
    
    df_authors = df
    
    col = df_authors.columns

    author_score = [0] * len(df_authors)

    anony_writers = ['Time Out contributors', 'Foursquare City Guide', 'Edge of the City', 'Team Infatuation', 'Munchies Staff', ]

    for j in range(len(df_authors)):
        for i in range(len(col)):
            if len(df_authors[col[i]][j]) > 1:
                author_score[j] += 3
                if df_authors[col[i]][j] == 'Robert Sietsema':
                    author_score[j] += 17
                elif df_authors[col[i]][j] == 'Pete Wells':
                    author_score[j] += 17
                elif df_authors[col[i]][j] not in [anony_writers]:
                    author_score[j] += 1

    for k in range(len(author_score)):
        if 0 < author_score[k] < 10:
            author_score[k] = 10

    df_authors['score'] = author_score
            
    return df_authors

def time_score(df):
    
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
            
    df['time_score'] = time_score
    
    return df