

# ----------------------------------------------------------------------------
# imports and setup
# ----------------------------------------------------------------------------

# import standard libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import yaml


def CleanCauseCountRawData() -> None:
    '''
    Outputs cleaned raw death cause count data (taken from web scraping) 
    '''

    # read config file
    with open("config.yml", 'r') as file:
        config = yaml.safe_load(file)

    # ----------------------------------------------------------------------------
    # read data
    # ----------------------------------------------------------------------------
    file_name = config["file_names"]["cause_count_raw"]

    full_path = f"{os.getcwd()}/{file_name}"

    df = pd.read_csv(full_path)

    # ----------------------------------------------------------------------------
    # visualize data
    # ----------------------------------------------------------------------------

    # to get more insight, calculate how many times each cause occured in total
    death_cause_occurance = (df.iloc[:, 1:-1] > 0).sum()
    death_cause_not_accured = (df.iloc[:, 1:-1] == 0).sum()

    # create a bar plot for insights (look into the data)
    plt.figure(figsize=(8, 6))
    sns.barplot(x=death_cause_occurance.values, y=death_cause_occurance.index)

    # set the title and axis labels
    plt.title("Frequency of death causes being reported in the news")
    plt.xlabel("Nr of times reported in media")
    plt.ylabel("Death cause")

    # set the style
    sns.set_style("darkgrid")

    # show the plot
    plt.show()

    # ----------------------------------------------------------------------------
    # clean data
    # ----------------------------------------------------------------------------

    # convert nr of occurances in an article to binary
    # e.g. if a cause occured 10 times, we will record that a cause occured in an article
    # explain why later
    df.iloc[:, 1:-1] = df.iloc[:, 1:-1].applymap(lambda x: 1 if x != 0 else 0)

    # ----------------------------------------------------------------------------
    # export
    # ----------------------------------------------------------------------------

    file_name = config["file_names"]["cause_count_processed"]
    df.to_csv('cause_count_news.csv', index=False)


CleanCauseCountRawData()
