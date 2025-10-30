# ============================================
# QUESTION 2: Top 10 Countries by Content (Horizontal Bar Chart)
# ============================================
# QUESTION: Which countries produce the most content available on Netflix?
# 
# VALIDATION/JUSTIFICATION:
# This analysis is critical because:
# 1. It reveals Netflix's global content sourcing strategy and market focus
# 2. Horizontal bar charts are excellent for comparing categories with long names (country names)
# 3. Top 10 filtering prevents overcrowding while showing the most significant contributors
# 4. This helps identify which regional markets Netflix is investing in most heavily
# 5. Content localization teams can use this to prioritize dubbing and subtitle efforts
# 6. It shows cultural diversity and international expansion patterns
# 7. Regional licensing and production partnerships can be evaluated based on this data

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
print("QUESTION 2: Top Countries by Content")
print("="*50)

# Extract first country from countries column (some have multiple countries)
df['primary_country'] = df['countries'].fillna('Unknown').str.split(',').str[0].str.strip()

country_counts = df['primary_country'].value_counts().head(10)
print("\nTop 10 Countries:")
print(country_counts)

plt.figure(figsize=(12, 6))
country_counts.plot(kind='barh', color='#E50914')
plt.title('Top 10 Countries by Netflix Content', fontsize=16, weight='bold', pad=20)
plt.xlabel('Number of Titles', fontsize=12, weight='bold')
plt.ylabel('Country', fontsize=12, weight='bold')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


