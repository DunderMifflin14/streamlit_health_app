

import requests
import re
import pandas as pd
import os
import yaml


def NewsAPICauseCount():
    '''
    outputs csv with count of the death causes found/mentioned in news articles
    '''

    # read config file
    with open("config.yml", 'r') as file:
        config = yaml.safe_load(file)

    with open("params.yml", 'r') as file:
        params = yaml.safe_load(file)

    causes_of_death = config["causes_of_death"]
    causes_of_death_param = ' OR '.join(causes_of_death)

    # Define the NewsAPI endpoint and parameters
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': causes_of_death_param,
        'qInText': causes_of_death_param,
        'pageSize': 100,  # The number of results to return per page. max 100
        'apiKey': params["api_key"]
    }

    # Send a GET request to the NewsAPI endpoint with the defined parameters
    response = requests.get(url, params=params)

    # Get the response data in JSON format
    data = response.json()

    # Create a dictionary to store the count of each cause of death for each article
    article_cause_count = {}

    # Loop through each article in the response and extract its content
    for article in data['articles']:
        # Send a GET request to the article link to get the full content
        article_response = requests.get(article['url'])
        article_content = article_response.text

        # make sure we are searching only artiles that mentioned death
        if re.search(r'\b(death|murder|kill)\b', article_content.lower()):
            # Create a dictionary to store the count of each cause of death in the current article
            cause_count = {}

            # Loop through each cause of death and count its occurrences in the article content
            for cause in causes_of_death:
                cause_count[cause] = article_content.count(cause)

            # also add article url
            cause_count['url'] = article['url']

            # Add the cause count dictionary to the article 'cause count' dictionary
            article_cause_count[article['title']] = cause_count

    df = pd.DataFrame.from_dict(article_cause_count, orient='index')

    # add a new column with article_id
    df_cause_count = df.reset_index(drop=True, inplace=False)
    df_cause_count.insert(0, 'article_id', range(1, len(df_cause_count) + 1))

    # check if the output file exists, and append data to the file if it does, else create a new file
    if os.path.isfile('cause_count.csv'):
        df_cause_count.to_csv('cause_count.csv', mode='a',
                              header=False, index=False)
    else:
        df_cause_count.to_csv('cause_count.csv', index=False)


if __name__ == "__main__":
    NewsAPICauseCount()
