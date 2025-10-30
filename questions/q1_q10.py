# ============================================
# QUESTION 10: Top 10 Directors by Content Count (Bar Chart)
# ============================================
# QUESTION: Which directors have the most content on Netflix?
# 
# VALIDATION/JUSTIFICATION:
# This analysis is important because:
# 1. Identifies key content creators and potential partnership opportunities
# 2. Bar charts effectively rank and compare discrete entities
# 3. High-volume directors might have exclusive deals or strong relationships with Netflix
# 4. This data supports talent acquisition and retention strategies
# 5. Marketing can leverage popular directors for promotional campaigns
# 6. Understanding director portfolios helps in content curation and collections
# 7. Fans of specific directors can be targeted with personalized recommendations
# 8. This reveals Netflix's investment in auteur-driven vs commercial content

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
print("QUESTION 10: Top 10 Directors by Content Count")
print("="*50)

directors_list = df['directors'].dropna().str.split(',').explode().str.strip()
director_counts = directors_list.value_counts().head(10)

print("\nTop 10 Directors:")
print(director_counts)

plt.figure(figsize=(12, 6))
director_counts.plot(kind='barh', color='#831010')
plt.title('Top 10 Directors with Most Content on Netflix', fontsize=16, weight='bold', pad=20)
plt.xlabel('Number of Titles', fontsize=12, weight='bold')
plt.ylabel('Director', fontsize=12, weight='bold')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


