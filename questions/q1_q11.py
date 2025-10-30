# ============================================
# QUESTION 11: Content Addition by Year (Bar Chart)
# ============================================
# QUESTION: In which years did Netflix add the most content to its platform?
# 
# VALIDATION/JUSTIFICATION:
# This analysis is critical because:
# 1. Bar charts clearly show year-over-year comparisons of content additions
# 2. Peak years indicate major content acquisition initiatives or market expansion
# 3. Declining years might signal market maturity or strategic content pruning
# 4. This correlates with Netflix's subscriber growth and competitive landscape
# 5. Content budgets and licensing deals can be inferred from addition patterns
# 6. Regulatory changes or competitive pressures show up as year-over-year changes
# 7. This validates Netflix's "content is king" strategy execution over time

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
print("QUESTION 11: Content Added by Year")
print("="*50)

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

yearly_additions = df['year_added'].value_counts().sort_index()
print("\nContent Added per Year:")
print(yearly_additions)

plt.figure(figsize=(12, 6))
yearly_additions.plot(kind='bar', color='#E50914')
plt.title('Content Added to Netflix by Year', fontsize=16, weight='bold', pad=20)
plt.xlabel('Year', fontsize=12, weight='bold')
plt.ylabel('Number of Titles Added', fontsize=12, weight='bold')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()


