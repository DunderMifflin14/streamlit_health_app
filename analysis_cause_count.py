
'''
-02 file
'''


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



path = r'PATH TO THE FILE/cause_count.csv'
df = pd.read_csv(path)

death_cause_occurance = (df.iloc[:,1:-1] > 0).sum()
death_cause_not_accured = (df.iloc[:,1:-1] == 0).sum()



# create a bar plot using seaborn
plt.figure(figsize=(8, 6))
sns.barplot(x=death_cause_occurance.values, y=death_cause_occurance.index)

# set the title and axis labels
plt.title("Frequency of death causes being reported in the news")
plt.xlabel("Times reported in media")
plt.ylabel("Death cause")

# set the style
sns.set_style("darkgrid")


# show the plot
plt.show()


death_cause_occurance1 = (df.iloc[:,1:-1] > 0).sum()
death_cause_not_accured1 = (df.iloc[:,1:-1] == 0).sum()

# double check this line if pasted into correct location
df.iloc[:,1:-1] = df.iloc[:,1:-1].applymap(lambda x: 1 if x != 0 else 0)


df.to_csv('cause_count_news.csv', index=False)

