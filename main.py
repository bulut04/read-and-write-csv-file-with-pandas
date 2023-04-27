import pandas as pd

df = pd.read_csv('exhibitA-input.csv', sep='\t')

df = df[df['PLAY_TS'].str.startswith('10/08/2016')]

distinct_play_counts = df.groupby('CLIENT_ID')['SONG_ID'].nunique().value_counts()

output_df = pd.DataFrame({'DISTINCT_PLAY_COUNT': distinct_play_counts.index, 'CLIENT_COUNT': distinct_play_counts.values})

output_df.to_csv('output_file.csv', index=False)