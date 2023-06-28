import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def draw_cat_plot():
    # Read the dataset
    df = pd.read_csv('medical_examination.csv')

    # Create an overweight column
    df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

    # Normalize cholesterol and glucose columns
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

    # Create a count plot
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    sns.catplot(data=df, x='variable', hue='value', col='cardio', kind='count', palette='pastel', ax=axes)
    axes[0].set_title('No Cardiovascular Disease')
    axes[1].set_title('Cardiovascular Disease')
    axes[0].set_xlabel('')
    axes[1].set_xlabel('')
    axes[0].set_ylabel('Total')
    axes[1].set_ylabel('Total')
    axes[0].set_xticklabels(['Cholesterol', 'Glucose', 'Alcohol', 'Active', 'Smoking'], rotation=45)
    axes[1].set_xticklabels(['Cholesterol', 'Glucose', 'Alcohol', 'Active', 'Smoking'], rotation=45)
    plt.tight_layout()

    # Save the plot to a file
    plt.savefig('catplot.png')

def draw_heat_map():
    # Read the dataset
    df = pd.read_csv('medical_examination.csv')

    # Clean the data
    df = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df.corr()

    # Create a mask for the upper triangle
    mask = (corr.mask(np.triu(np.ones(corr.shape)).astype(bool)))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, center=0, linewidths=0.5, annot=True, fmt=".1f", cbar_kws={'shrink': 0.8})

    # Save the plot to a file
    plt.savefig('heatmap.png')

