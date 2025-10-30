# ============================================
# QUESTION 9: Movies vs TV Shows by Year (Stacked Area Chart)
# ============================================
# QUESTION: How has the balance between Movies and TV Shows evolved over release years?
# 
# VALIDATION/JUSTIFICATION:
# This visualization is valuable because:
# 1. Stacked area charts show both total volume and composition changes over time
# 2. It reveals strategic shifts in content type preferences across different eras
# 3. This helps understand if Netflix is pivoting toward original series vs films
# 4. Historical trends inform future content production roadmaps
# 5. Different decades had different production norms (more movies in 90s, more series recently)
# 6. Investment allocation between movie rights and TV show licenses can be evaluated
# 7. This shows how streaming has influenced content production patterns

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
print("QUESTION 9: Movies vs TV Shows Over Release Years")
print("="*50)

year_type = df.groupby(['release_year', 'type']).size().unstack(fill_value=0)
# Ensure both columns exist for stackplot
year_type = year_type.reindex(columns=['Movie', 'TV Show'], fill_value=0)
print("\nContent Type by Year:")
print(year_type.tail(10))

plt.figure(figsize=(14, 6))
plt.stackplot(year_type.index, year_type['Movie'], year_type['TV Show'], 
              labels=['Movie', 'TV Show'], colors=['#E50914', '#B20710'], alpha=0.8)
plt.title('Movies vs TV Shows by Release Year (Stacked)', fontsize=16, weight='bold', pad=20)
plt.xlabel('Release Year', fontsize=12, weight='bold')
plt.ylabel('Number of Titles', fontsize=12, weight='bold')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


