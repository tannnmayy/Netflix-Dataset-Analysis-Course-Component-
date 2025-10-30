# ============================================
# QUESTION 7: TV Show Seasons Distribution (Bar Chart)
# ============================================
# QUESTION: How many seasons do most TV shows have on Netflix?
# 
# VALIDATION/JUSTIFICATION:
# This analysis is crucial because:
# 1. It shows whether Netflix favors limited series or long-running shows
# 2. Bar charts clearly show discrete season counts and their frequencies
# 3. Multi-season shows indicate higher production investment and user engagement
# 4. Single-season shows might be mini-series, cancelled shows, or ongoing series
# 5. Content strategy differs for shows with different season counts (binge vs episodic)
# 6. This helps predict future content pipeline and renewal decisions
# 7. Longer shows provide more "stickiness" - users invest more time in multi-season series
# 8. Production costs scale with season count, affecting budget allocation
# 9. Recommendation algorithms treat single vs multi-season shows differently

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (10, 6)

def load_netflix_dataset() -> pd.DataFrame:
    candidate_paths = (
        '../netflix_titles_CLEANED.csv',
        '../netflix_titles.CLEANED.csv',
        'netflix_titles_CLEANED.csv',
        'netflix_titles.CLEANED.csv',
    )
    last_err = None
    for p in candidate_paths:
        try:
            return pd.read_csv(p)
        except FileNotFoundError as e:
            last_err = e
            continue
    raise last_err

df = load_netflix_dataset()

print("\n" + "="*50)
print("QUESTION 7: TV Show Seasons Distribution")
print("="*50)

tv_shows_df = df[df['type'] == 'TV Show'].copy()
tv_shows_df['num_seasons'] = tv_shows_df['duration'].str.extract(r'(\d+)').astype(float)

season_counts = tv_shows_df['num_seasons'].value_counts().sort_index()
print("\nSeasons Distribution:")
print(season_counts)

plt.figure(figsize=(10, 6))
season_counts.plot(kind='bar', color='#B20710')
plt.title('TV Show Seasons Distribution', fontsize=16, weight='bold', pad=20)
plt.xlabel('Number of Seasons', fontsize=12, weight='bold')
plt.ylabel('Number of Shows', fontsize=12, weight='bold')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


