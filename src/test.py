from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create a list of word
text=("""Python Python Python Matplotlib Matplotlib Seaborn
      Network Plot Violin Chart Pandas Datascience Wordcloud
      Spider Radar Parrallel Alpha Color Brewer Density Scatter
      Barplot Barplot Boxplot Violinplot Treemap Stacked Area
      Chart Chart Visualization Dataviz Donut Pie Time-Series
      Wordcloud Wordcloud Sankey Bubble""")

# Create the wordcloud object
stopwords = ["Python", "Matplotlib"]
wordcloud = WordCloud(
    width=480, height=480,
    stopwords=stopwords,
    background_color='white'
).generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()