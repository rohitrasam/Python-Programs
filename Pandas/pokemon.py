import pandas as pd
import re

pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', False)

"""Loading data"""
df = pd.read_csv('pokemon_data.txt')
print(df.head())
print(df.tail(3))


"""Reading data in Pandas"""

# 1. Reading headers
print(df.columns)

# 2. Read each column
print(df['Name'][0:5], '\n')  # == print(df.Name[0:5])
print(df[['Name', 'Type 1', 'HP']].head(), '\n')

# 3. Reading Each Row
print(df.iloc[1], '\n')
print(df.iloc[0:4], '\n')
# for index, row in df.iterrows():
#     print(index, row)
# for index, row in df.iterrows():
#     print(index, row['Name'])
print(df.loc[df['Type 1'] == 'Fire'], '\n')

# 4. Read a specific location (R, C)
print(df.iloc[2, 1], '\n')


"""Sorting/Describing Data"""
# print(df.describe())  # prints mean std etc

# print(df.sort_values('Name', ascending=False).head(), '\n')
print(df.sort_values(['Type 1', 'HP'], ascending=[True, False]).head(), '\n')


"""Making changes to the data"""
# adding a column
df['Total'] = df.iloc[:, 4:10].sum(axis=1)  # == df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(), '\n')

# Dropping a column
# df = df.drop(columns=['Total'])
# print(df.head(), '\n')

# Relocating column
cols = list(df.columns)
df = df[cols[:4] + [cols[-1]] + cols[4:12]]  # Switch Total column to the left side
print(df.head(), '\n')



"""Saving Data(Exporting into Desired Format"""
# df.to_csv('modified.csv', index=False)
# df.to_excel('modified.xlsx', index=False)
# df.to_csv('modified.txt', index=False, sep='\t')


"""Filtering Data"""
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
new_df.reset_index(drop=True, inplace=True)  # == new_df = new_df.reset_index(drop=True)
print(new_df, '\n')
# print(df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')], '\n')

mega = df.loc[df['Name'].str.contains('Mega')]  # Table containing all the names with Mega in them
print(mega, '\n')

# notMega = df.loc[~df['Name'].str.contains('Mega')]  # Table containing all the names that don't have Mega in them
# print(notMega.head(), '\n')

mega = df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]  # df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I regex=True)]
print(mega.head(), '\n')

mega = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
print(mega.head(), '\n')

"""Conditional Changes"""
# df.loc[df['Type 1'] == 'Water', 'Type 1'] = 'Hydro'  # Changes Type 1 from Water to Hydro
# print(df.head(20))

# df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True  # Sets Fire pokemon to legendary
# print(df.head(20), '\n')

print(df.head(20), '\n')
# df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['TEST VALUE', 'TEST VALUE2']
# print(df, '\n')

"""Aggregate Statistics(Groupby)"""
df['Count'] = 1
print(df.head(20), '\n')
# print(df.groupby(['Type 1']).count())
print(df.groupby(['Type 1', 'Type 2']).count()['Count'], '\n')


"""Working with large amounts of data"""
new_df = pd.DataFrame(columns=df.columns)  # Create a new data frame that's empty with the same columns of df

# for df in pd.read_csv('modified.csv', chunksize=5):
#     results = df.groupby(['Type 1']).count()
#
#     new_df = pd.concat([new_df, results])
