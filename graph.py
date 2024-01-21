import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def graph(df):

    fig, ax = plt.subplots()
    y = df.geo
    x = df.OBS_VALUE

    countries = df.geo.unique()
    num_countries = len(countries)

    y_axis = np.arange(num_countries)

    first_causes = df.loc[df.top_no == '1']
    second_causes = df.loc[df.top_no == '2']
    third_causes = df.loc[df.top_no == '3']
    bar_height = 0.3

    ax.barh(y_axis + bar_height, first_causes.OBS_VALUE, height = bar_height)
    ax.barh(y_axis, second_causes.OBS_VALUE, height = bar_height)
    ax.barh(y_axis-bar_height, third_causes.OBS_VALUE, height = bar_height)

    # Add labels to the bars using plt.text
    for i in range(len(countries)):
        ax.text(first_causes.OBS_VALUE.iloc[i] + 1, i + bar_height, first_causes.icd10.iloc[i], va='center', fontsize=14, style = 'italic')
        ax.text(second_causes.OBS_VALUE.iloc[i] + 1, i, second_causes.icd10.iloc[i], va='center', fontsize=14, style = 'italic')
        ax.text(third_causes.OBS_VALUE.iloc[i] + 1, i - bar_height, third_causes.icd10.iloc[i], va='center', fontsize=14, style = 'italic')

    ax.yticks(y_axis, countries, fontsize=16)
    ax.barh(x, y, 0.5)

    ax.yticks(y_axis, countries, fontsize=16)
    ax.title("Causes of death per EU country", fontsize=30)
    ax.legend()
    ax.show()


# df = pd.read_csv("/Users/marta/Documents_/Andrew_project/streamlit_health_app/df_final.csv")
# graph = graph(df)



    