import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / (df['height'] ** 2) * 10000 > 25).astype(int)

# 3
df['cholesterol'] = ((df['cholesterol'] - 1 ).astype(bool)).astype(int)
df['gluc'] = ((df['gluc'] - 1 ).astype(bool)).astype(int)
df.rename(columns={'sex': 'gender'})
# 4 Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot():
    # 5 Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    df_cat = df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco','cardio', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # 6 Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = None


    # 7 Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import : sns.catplot()


    chart = sns.catplot(x="variable", hue='value', col="cardio", col_wrap=2,
                    data=df_cat,
                    kind="count")
    chart.set_ylabels('total')
    # 8
    fig = chart.figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) 
               & (df['height'] >= df['height'].quantile(0.025)) 
               & (df['height'] <= df['height'].quantile(0.975)) 
               & (df['weight'] >= df['weight'].quantile(0.025)) 
               & (df['weight'] <= df['weight'].quantile(0.975))  
               ]

    # 12
    
    corr = df_heat.corr() 

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(10, 8) )

    # 15
    sns.heatmap(corr, annot=True, fmt='.1f', cmap="coolwarm", mask=mask)


    # 16
    fig.savefig('heatmap.png')
    return fig
