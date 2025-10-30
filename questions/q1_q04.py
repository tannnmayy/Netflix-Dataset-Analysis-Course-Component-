# ============================================
# QUESTION 4: Release Year Trend (Line Chart)
# ============================================
# QUESTION: How has the volume of content production changed over the years?
# 
# VALIDATION/JUSTIFICATION:
# This time-series analysis is valuable because:
# 1. Line charts are optimal for showing trends and patterns over continuous time periods
# 2. It reveals whether Netflix focuses on newer content or maintains a classic library
# 3. Spikes or drops in certain years can indicate industry events or strategic shifts
# 4. Content freshness is a key competitive advantage in streaming services
# 5. Historical content acquisition patterns help predict future content needs
# 6. This helps identify the "golden age" of content production for the platform
# 7. Investors use this to assess whether Netflix is acquiring recent vs archival content
# 8. Marketing teams can highlight "new releases" vs "classic collection" campaigns

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (14, 6)

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
print("QUESTION 4: Content Release Year Trend")
print("="*50)

year_counts = df['release_year'].value_counts().sort_index()
print("\nContent by Release Year:")
print(year_counts.tail(10))

plt.figure(figsize=(14, 6))
plt.plot(year_counts.index, year_counts.values, marker='o', 
         color='#E50914', linewidth=2, markersize=6)
plt.title('Netflix Content by Release Year', fontsize=16, weight='bold', pad=20)
plt.xlabel('Release Year', fontsize=12, weight='bold')
plt.ylabel('Number of Titles', fontsize=12, weight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


