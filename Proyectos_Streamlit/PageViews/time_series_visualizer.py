import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
                 names=['date', 'Page Views'], header=0, parse_dates=True, index_col=0)

# Clean data
df = df[(df['Page Views'] < df['Page Views'].quantile(0.975)) &
        (df['Page Views'] > df['Page Views'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 10))
    ax = df.plot(title="'Daily freeCodeCamp Forum Page Views 5/2016-12/2019'",
                 xlabel="'Date'", ylabel='Page Views', c='red', legend=False, ax=ax)
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.resample('M').mean()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    average_page_views = df_bar.groupby(['year', 'month']).mean().unstack()
    average_page_views.columns = pd.date_range(
        start='2016-01-01', periods=12, freq='M').strftime('%B')
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 10))
    average_page_views.plot(kind="bar", ax=ax)
    ax.set(title='Average Page Views per Month',
           xlabel='Years', ylabel='Average Page Views')
    plt.legend(average_page_views.columns)
    plt.xticks(rotation=90)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(20, 10))
    sns.boxplot(x='year', y='Page Views', data=df_box, ax=axes[0], palette="tab10").set(title='Year-wise Box Plot (Trend)',
                                                                                        xlabel='Year', ylabel='Page Views')
    sns.boxplot(x='Month', y='Page Views', data=df_box, ax=axes[1], palette="husl").set(
        title='Month-wise Box Plot (Seasonality)')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
