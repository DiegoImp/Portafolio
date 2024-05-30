
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(
    r'Proyectos_Streamlit\Data\btc-market-price.csv',
    index_col=0,
    parse_dates=True
)


# Selecciona los valores de la fecha
df_na = df.loc["2017-12-01":"2017-12-15"]
df_na['Ether'].isna().value_counts()  # Cuenta la cantidad de nans
# Rellena los nans con el valor anterior
df_na['Ether'].fillna(df_na['Ether'].ffill())


df_na.loc[df_na['Ether'].isna()]  # Muestra los valores nans en un DataFrame
# Rellena los nans con el valor siguiente permanentemente
# Al parecer al rellenar en la copia, esto cambia el original (bug)
df_na.fillna(method='bfill', inplace=True)
df.plot(figsize=(16, 9))
# Arreglado la falta de valores
df.loc['2017-12': '2017-12-15'].plot(y='Ether', figsize=(16, 9))
# Arreglando picos
# #zoom en la localilazion
df['2017-12-25':'2018-01-01'].plot()
df['2018-03-01': '2018-03-09'].plot()

# Esto elimina los picos
df_cleaned = df.drop(pd.to_datetime(['2017-12-28', '2018-03-04']))
df_cleaned.plot(figsize=(16, 9))  # La grafica se ve mejor
# ----------------------------------------------------
# Central Tendency
# We'll use a set of common indicators of to measure central tendency and identify these outliers:
# Both values seem too high. That's because the outliers are skewing with the mean:
df.mean()
df_cleaned.mean()
# The median is a better indicator of central tendency in the presence of outliers:
df_cleaned.median()
# Now we can use a few of the charts that we saw before + seaborn to visualize the distribution of our values.
# In particular, we're interested in histograms:
df_cleaned.plot(kind='hist', y='Ether', bins=150)
df_cleaned.plot(kind='hist', y='Bitcoin', bins=150)
# ---------------------------------------------------------------------------
# Visualizing bivariate distributions
# The most common way to observe a bivariate distribution is a scatterplot,
# the jointplot will also include the distribution of the variables:
sns.jointplot(x="Bitcoin", y="Ether", data=df_cleaned, size=9)
# If you want only a scatter plot, you can use the regplot method,
# that also fits a linear regression model in the plot:
# Colocar
fig, ax = plt.subplots(figsize=(15, 7))
sns.regplot(x="Bitcoin", y="Ether", data=df_cleaned, ax=ax)
# ---------------------------------------------------------------------------

# --------------------------------------------------------------------------
# Dispersion
# We'll use a few methods to measure dispersion in our dataset, most of them well known:

# Range
# Variance and Standard Deviation
# IQR
# Range
# Range is fairly simple to understand, it's just the max - min values:
# df_cleaned['Bitcoin'].max() - df_cleaned['Bitcoin'].min()
# IQR
# The Interquartile range is a good measure of "centered" dispersion,
# and is calculated as Q3 - Q1 (3rd quartile - 1st quartile).
df['Bitcoin'].quantile(.75) - df['Bitcoin'].quantile(.25)  # 6597.494147619047
# 6548.249242559523
df_cleaned['Bitcoin'].quantile(.75) - df_cleaned['Bitcoin'].quantile(.25)
# Analytical Analysis of invalid values
# Using std: Z scores
upper_limit = df['Bitcoin'].mean() + 2 * df['Bitcoin'].std()
lower_limit = df['Bitcoin'].mean() - 2 * df['Bitcoin'].std()
print("Upper Limit: {}".format(upper_limit))
print("Lower Limit: {}".format(lower_limit))
# Upper Limit: 27369.17635730169
# Lower Limit: -13377.16831365621
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df['Bitcoin'], ax=ax)
ax.axvline(lower_limit, color='red')
ax.axvline(upper_limit, color='red')
# Our lower limit doesn't make a lot of sense, as negative values are invalid.
# But our upper limit has a really good measure.
# Anything above $27,369 is considered to be an invalid value. Pretty accurate.


# Cleaning invalid values analytically
upper_limit = df['Bitcoin'].mean() + 2 * df['Bitcoin'].std()
df[df['Bitcoin'] < upper_limit].plot(figsize=(16, 7))
df.drop(df[df['Bitcoin'] > upper_limit].index).plot(figsize=(16, 7))
