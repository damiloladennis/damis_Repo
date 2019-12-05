# Import pandas
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv(r'C:\Users\user\Documents\git\NLTK\train.tsv', sep='\t')
print(data.head())
data.info()
data.Sentiment.value_counts()

Sentiment_count=data.groupby('Sentiment').count()
plt.bar(Sentiment_count.index.values, Sentiment_count['Phrase'])
plt.xlabel('Review Sentiments')
plt.ylabel('Number of Review')
plt.show()
