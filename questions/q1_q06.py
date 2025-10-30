# ============================================
# QUESTION 6: Movie Duration Distribution (Histogram)
# ============================================
# QUESTION: What is the typical length of movies in the Netflix catalog?
# 
# VALIDATION/JUSTIFICATION:
# This distribution analysis is important because:
# 1. Histograms are ideal for showing frequency distributions of continuous data
# 2. It reveals user preferences - are people watching short, medium, or long films?
# 3. Content acquisition can target specific duration ranges based on gaps
# 4. Scheduling and recommendation algorithms use duration as a key feature
# 5. Understanding duration patterns helps in content categorization ("Quick Watch", "Feature Films")
# 6. Production teams can benchmark their content against industry standards
# 7. This identifies outliers (very short or very long movies) that may need special handling
# 8. User session time and engagement metrics correlate strongly with content duration

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (12, 6)

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
print("QUESTION 6: Movie Duration Distribution")
print("="*50)

movies_df = df[df['type'] == 'Movie'].copy()
movies_df['duration_min'] = movies_df['duration'].str.extract(r'(\d+)').astype(float)

print("\nMovie Duration Statistics:")
print(movies_df['duration_min'].describe())

plt.figure(figsize=(12, 6))
plt.hist(movies_df['duration_min'].dropna(), bins=20, color='#E50914', edgecolor='black')
plt.title('Distribution of Movie Durations', fontsize=16, weight='bold', pad=20)
plt.xlabel('Duration (minutes)', fontsize=12, weight='bold')
plt.ylabel('Frequency', fontsize=12, weight='bold')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()


