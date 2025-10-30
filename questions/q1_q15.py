# ============================================
# QUESTION 15: Top 5 Countries - Content Type Breakdown (Grouped Bar Chart)
# ============================================
# QUESTION: How does the Movie/TV Show split differ across top content-producing countries?
# 
# VALIDATION/JUSTIFICATION:
# This comparative analysis is powerful because:
# 1. Grouped bar charts excel at comparing subcategories across main categories
# 2. Regional content preferences and production capabilities vary significantly
# 3. Some countries specialize in films (Bollywood) while others in series (US TV industry)
# 4. This informs regional partnership strategies and content acquisition focus
# 5. Cultural differences in storytelling formats (episodic vs feature-length) are revealed
# 6. Market-specific content strategies can be developed based on regional strengths
# 7. This validates whether Netflix's regional content mix matches local production trends
# 8. Investment priorities can be adjusted per region based on content type strengths

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

# Precompute primary country for this analysis
df['primary_country'] = df['countries'].fillna('Unknown').str.split(',').str[0].str.strip()

print("\n" + "="*50)
print("QUESTION 15: Top 5 Countries - Content Type Breakdown")
print("="*50)

top5_countries = df['primary_country'].value_counts().head(5).index
top5_df = df[df['primary_country'].isin(top5_countries)]
country_type_pivot = pd.crosstab(top5_df['primary_country'], top5_df['type'])

print("\nTop 5 Countries Content Breakdown:")
print(country_type_pivot)

ax = country_type_pivot.plot(kind='bar', color=['#E50914', '#B20710'], figsize=(12, 6))
plt.title('Top 5 Countries: Movies vs TV Shows', fontsize=16, weight='bold', pad=20)
plt.xlabel('Country', fontsize=12, weight='bold')
plt.ylabel('Number of Titles', fontsize=12, weight='bold')
plt.legend(title='Content Type', fontsize=10)
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()


