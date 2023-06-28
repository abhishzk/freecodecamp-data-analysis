import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def draw_line_plot():
    # Read the data from the CSV file
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    # Filter out the days when the page views were in the top or bottom 2.5%
    df = df[
        (df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
    ]

    # Create the line plot
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df['value'], color='r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)

    # Save and show the plot
    plt.savefig('line_plot.png')
    plt.show()


def draw_bar_plot():
    # Read the data from the CSV file
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])

    # Extract the year and month from the date column
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.strftime('%B')

    # Group the data by year and month and calculate the average page views
    df_bar = df.groupby(['year', 'month'], as_index=False)['value'].mean()

    # Set the order of the months for proper sorting
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=month_order, ordered=True)

    # Create the bar plot
    g = sns.catplot(
        x='year', y='value', hue='month', data=df_bar, kind='bar',
        palette='muted', legend=False, height=6, aspect=1.5
    )
    g.set_axis_labels('Years', 'Average Page Views')
    g.fig.suptitle('Average Daily Page Views on freeCodeCamp Forum')
    g.add_legend(title='Months')

    # Save and show the plot
    plt.savefig('bar_plot.png')
    plt.show()


def draw_box_plot():
    # Read the data from the CSV file
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])

    # Extract the year and month from the date column
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.strftime('%b')

    # Order the months for proper sorting in the box plots
    month_order = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)

    # Create the figure and subplots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Create the year-wise box plot
    sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Create the month-wise box plot
    sns.boxplot(x='month', y='value', data=df, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Adjust the layout
    plt.tight_layout()

    # Save and show the plot
    plt.savefig('box_plots.png')
    plt.show()
