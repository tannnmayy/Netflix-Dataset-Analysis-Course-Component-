# ============================================
# QUESTION 8: Content Added Over Time (Line Chart)
# ============================================
# QUESTION: At what rate is Netflix adding new content to its platform over time?
# 
# VALIDATION/JUSTIFICATION:
# This time-series analysis is essential because:
# 1. Line charts excel at showing trends and growth patterns over time
# 2. It reveals Netflix's content acquisition velocity and strategic timing
# 3. Spikes might correspond to major releases, seasonal trends, or strategic launches
# 4. Investors track content addition rate as a key performance indicator
# 5. Competitive analysis: comparing growth rate with other streaming platforms
# 6. This helps predict infrastructure needs (storage, bandwidth, servers)
# 7. Marketing teams can align campaigns with content drop patterns
# 8. Monthly/yearly patterns reveal content licensing cycles and renewal schedules
# 9. Declining trends might indicate market saturation or strategic pivots
# 10. This validates whether Netflix is maintaining its promised content refresh rate

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
print("QUESTION 8: Content Added to Netflix Over Time")
print("="*50)

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['month_added'] = df['date_added'].dt.to_period('M')

monthly_additions = df.groupby('month_added').size().sort_index()

print("\nMonthly Content Additions:")
print(monthly_additions.tail(10))

plt.figure(figsize=(14, 6))
monthly_additions.plot(color='#E50914', linewidth=2)
plt.title('Content Added to Netflix Over Time', fontsize=16, weight='bold', pad=20)
plt.xlabel('Date', fontsize=12, weight='bold')
plt.ylabel('Number of Titles Added', fontsize=12, weight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


