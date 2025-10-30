# ============================================
# QUESTION 13: Content Addition by Month of Year (Bar Chart)
# ============================================
# QUESTION: Are there seasonal patterns in when Netflix adds content?
# 
# VALIDATION/JUSTIFICATION:
# This seasonal analysis is valuable because:
# 1. Identifies if Netflix has strategic content drop periods (e.g., holiday seasons)
# 2. Bar charts effectively show cyclical patterns across 12 months
# 3. Content marketing campaigns can be planned around high-addition months
# 4. Competitor analysis: are there industry-wide seasonal patterns?
# 5. Licensing renewals and expirations often follow calendar patterns
# 6. Major entertainment events (awards season, summer blockbusters) influence timing
# 7. This helps predict future content pipeline and manage subscriber expectations
# 8. Resource allocation (QA, localization teams) can be planned based on seasonal peaks

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
print("QUESTION 13: Content Addition by Month")
print("="*50)

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['month_number'] = df['date_added'].dt.month
monthly_pattern = df['month_number'].value_counts().sort_index()
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

print("\nContent Added by Month:")
print(monthly_pattern)

plt.figure(figsize=(12, 6))
plt.bar(range(1, 13), [monthly_pattern.get(i, 0) for i in range(1, 13)], color='#E50914')
plt.title('Seasonal Pattern: Content Added by Month', fontsize=16, weight='bold', pad=20)
plt.xlabel('Month', fontsize=12, weight='bold')
plt.ylabel('Number of Titles Added', fontsize=12, weight='bold')
plt.xticks(range(1, 13), month_names)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()


