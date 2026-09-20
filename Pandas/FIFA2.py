import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', None)

df = pd.read_csv('data.csv', index_col=0)
df = df.set_index(['Club', 'Name'])
# df = df.sort_values('Value', ascending=False)
print(df.head(20), '\n')

cols = df.columns
print(df[cols[:2]], '\n')

df['Overall'] = df.iloc[:, 9:].mean(axis=1)
df = df.sort_values('Club', ascending=False)
print(df.head(50))
df = df.drop(['Work Rate', 'Preferred Foot', 'Value', 'Potential', 'SlidingTackle', 'StandingTackle', 'Composure',
              'Marking', 'Interceptions', 'Balance', 'Jersey Number', 'Weight', ], axis=1)
print(df.head(50), '\n')

juv = df.loc['Juventus'].sort_values('Nationality')
bar = df.loc['FC Barcelona'].sort_values('Nationality')

bar = bar.reset_index()
bar = bar.set_index(['Nationality', 'Name'])
bar = bar.sort_values('Nationality')
print(bar, '\n')

juv = juv.reset_index()
juv = juv.set_index(['Nationality', 'Name'])
juv = juv.sort_values('Nationality')
print(juv, '\n')


mix = pd.concat([juv, bar])
mix = mix.reset_index()
mix = mix.set_index(['Nationality', 'Name'])
mix = mix.sort_values('Nationality')
print(mix, '\n')
