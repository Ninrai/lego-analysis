import pandas as pd

df = pd.read_csv("datasets/lego_sets.csv")
theme = pd.read_csv("datasets/parent_themes.csv")

# 1. What percentafge of all licensed sets ever released were Star Wars themed?
theme['name']
theme_licensed = theme.loc[theme["name"].str.contains('Star Wars')]

licensed_list = theme_licensed[theme["is_licensed"]]['name'].tolist()

df_licensed = df.loc[df['theme_name'].isin(licensed_list)]
df_licensed[df['parent_name'] == "Star Wars"].shape[0]
the_force = round(df_licensed[df['parent_theme'] == "Star Wars"].shape[0] / df_licensed.shape[0] * 100, 2)


# 2. In which year was Star Wars not the most popular licensed theme (in terms of number of sets released that year)?
