# ============================================
# QUESTION 14: Release Year vs Date Added Gap (Scatter Plot)
# ============================================
# QUESTION: How long after release does content typically get added to Netflix?
# 
# VALIDATION/JUSTIFICATION:
# This time-lag analysis is insightful because:
# 1. Scatter plots show relationships between two continuous variables effectively
# 2. It reveals if Netflix acquires fresh content or relies on catalog/archive content
# 3. Short gaps indicate aggressive recent content acquisition or original productions
# 4. Long gaps suggest catalog content or classic movie collections
# 5. This informs licensing strategy and production vs acquisition balance
# 6. Windowing strategies (theatrical → streaming → TV) affect acquisition timing
# 7. Competitive advantage: shorter gaps mean fresher content for subscribers
# 8. Different gaps for movies vs TV shows indicate different content strategies

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
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
print("QUESTION 14: Release Year vs Addition Date Gap")
print("="*50)

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['year_gap'] = df['year_added'] - df['release_year']
df_gap = df[df['year_gap'].notna() & (df['year_gap'] >= 0)].copy()

print("\nYear Gap Statistics:")
print(df_gap['year_gap'].describe())

plt.figure(figsize=(14, 6))
plt.scatter(df_gap['release_year'], df_gap['year_gap'], 
            c=df_gap['type'].map({'Movie': '#E50914', 'TV Show': '#B20710'}), 
            alpha=0.5, s=30)
plt.title('Time Gap: Release Year to Netflix Addition', fontsize=16, weight='bold', pad=20)
plt.xlabel('Release Year', fontsize=12, weight='bold')
plt.ylabel('Years Until Added to Netflix', fontsize=12, weight='bold')
plt.grid(True, alpha=0.3)
legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor='#E50914', 
                          markersize=10, label='Movie'),
                   Line2D([0], [0], marker='o', color='w', markerfacecolor='#B20710', 
                          markersize=10, label='TV Show')]
plt.legend(handles=legend_elements, loc='upper left')
plt.tight_layout()
plt.show()


