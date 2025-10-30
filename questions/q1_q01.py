# QUESTION 1: Content Type Distribution (Pie Chart)
# ============================================
# QUESTION: What is the proportion of Movies vs TV Shows in the Netflix catalog?
# 
# VALIDATION/JUSTIFICATION:
# This visualization is essential because:
# 1. It provides a quick overview of Netflix's content strategy (movie-focused vs series-focused)
# 2. Pie charts are ideal for showing parts of a whole when there are few categories (2 in this case)
# 3. Percentages help stakeholders understand resource allocation and content balance
# 4. This metric influences content acquisition decisions and user interface design
# 5. Investors and analysts use this to assess Netflix's content diversification strategy

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better-looking plots
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Step 1: Load the Netflix dataset (robust path handling)
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
print("QUESTION 1: Content Type Distribution")
print("="*50)

type_counts = df['type'].value_counts()
print("\nContent Type Counts:")
print(type_counts)

plt.figure(figsize=(8, 8))
colors = ['#E50914', '#B20710']
plt.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%', 
        colors=colors, startangle=90, textprops={'fontsize': 14, 'weight': 'bold'})
plt.title('Netflix Content Type Distribution', fontsize=16, weight='bold', pad=20)
plt.tight_layout()
plt.show()


