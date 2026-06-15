import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Unemployment Trend Over Time
# -----------------------------
def plot_trend(df):
    plt.figure(figsize=(12,6))
    sns.lineplot(data=df, x='Date', y='Unemployment_Rate')
    plt.title("Unemployment Rate Trend (COVID Impact)")
    plt.xlabel("Date")
    plt.ylabel("Unemployment Rate (%)")
    plt.show()


# -----------------------------
# 2. State-wise Unemployment
# -----------------------------
def plot_statewise(df):
    state_data = df.groupby('Region')['Unemployment_Rate'].mean().sort_values(ascending=False)

    plt.figure(figsize=(12,6))
    sns.barplot(x=state_data.values, y=state_data.index)
    plt.title("State-wise Unemployment Rate")
    plt.xlabel("Unemployment Rate (%)")
    plt.ylabel("State")
    plt.show()


# -----------------------------
# 3. Urban vs Rural Comparison
# -----------------------------
def plot_area_comparison(df):
    plt.figure(figsize=(8,5))
    sns.barplot(data=df, x='Area', y='Unemployment_Rate')
    plt.title("Urban vs Rural Unemployment Rate")
    plt.xlabel("Area")
    plt.ylabel("Unemployment Rate (%)")
    plt.show()


# -----------------------------
# 4. Year-wise Trend
# -----------------------------
def plot_yearly_trend(df):
    yearly = df.groupby('Year')['Unemployment_Rate'].mean()

    plt.figure(figsize=(8,5))
    yearly.plot(kind='bar', color='orange')
    plt.title("Year-wise Unemployment Trend")
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate (%)")
    plt.show()


# -----------------------------
# 5. Correlation Heatmap
# -----------------------------
def plot_correlation(df):
    plt.figure(figsize=(8,5))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Correlation Between Variables")
    plt.show()


