import pandas as pd

df = pd.read_csv("datasets/lego_sets.csv")
theme = pd.read_csv("datasets/parent_themes.csv")

# 1. What percentafge of all licensed sets ever released were Star Wars themed?
# Merge
df_merged = df.merge(theme, left_on='parent_theme', right_on='name')
df_merged.head()

# Clean
df_merged.drop(columns="name_y", inplace=True)
df_merged.isna().sum()
df_merged_cleaned = df_merged.dropna(subset=['set_num'])

licensed = df_merged_cleaned[df_merged_cleaned['is_licensed']]
star_wars = licensed[licensed['parent_theme'] == 'Star Wars']
the_force = int(star_wars.shape[0] / licensed.shape[0] * 100)


# 2. In which year was Star Wars not the most popular licensed theme (in terms of number of sets released that year)?
df_licensed = licensed.copy()
df_licensed['count'] = 1
df_licensed_sorted = df_licensed.sort_values('year')
df_licensed_sorted_summed = df_licensed.groupby(['year', 'parent_theme'] ).sum().reset_index()
df_licensed_sorted_summed.sort_values('count', ascending=False).drop_duplicates('year').sort_values('year')

new_era = 2017

# 3. Break down number of sets by year
df2 = df_merged_cleaned.copy()
df2['count'] = 1
sets_per_year = df2.groupby(['year']).sum().reset_index().sort_values('year')[['year', 'count']]

sets_per_year

for index, row in sets_per_year.iterrows():
    print(row['year'], row['count'])
    

for index, row in sets_per_year.iterrows():
    print(index)
    