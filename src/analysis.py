def yearly_avg(df):
    return df.groupby('Year')['Unemployment_Rate'].mean()

def top_states(df):
    return df.groupby('Region')['Unemployment_Rate'].mean().sort_values(ascending=False)