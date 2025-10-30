# ============================================
# QUESTION 12: Average Movie Duration by Rating (Bar Chart)
# ============================================
# QUESTION: Does movie runtime vary by content rating?
# 
# VALIDATION/JUSTIFICATION:
# This analysis reveals important patterns:
# 1. Grouped bar charts show average values across categories effectively
# 2. Family content (PG, PG-13) might have different runtime norms than mature content (R, TV-MA)
# 3. This helps content creators understand industry standards for different audiences
# 4. Programming blocks and scheduling decisions depend on content length by rating
# 5. Children's content typically has shorter runtimes than adult content
# 6. This validates whether Netflix's catalog aligns with typical rating-duration relationships
# 7. User session planning differs for short family movies vs long adult dramas

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
print("QUESTION 12: Average Movie Duration by Rating")
print("="*50)

movies_df = df[df['type'] == 'Movie'].copy()
movies_df['duration_min'] = movies_df['duration'].str.extract(r'(\d+)').astype(float)

avg_duration_by_rating = movies_df.groupby('rating')['duration_min'].mean().sort_values(ascending=False)
print("\nAverage Duration by Rating:")
print(avg_duration_by_rating)

plt.figure(figsize=(12, 6))
avg_duration_by_rating.plot(kind='bar', color='#B20710')
plt.title('Average Movie Duration by Content Rating', fontsize=16, weight='bold', pad=20)
plt.xlabel('Rating', fontsize=12, weight='bold')
plt.ylabel('Average Duration (minutes)', fontsize=12, weight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()


