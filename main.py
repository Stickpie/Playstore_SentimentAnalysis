from textblob import TextBlob
import csv
import pandas as pd
import matplotlib.pyplot as plt

with open ('Whatsapp.csv', 'r') as csv_file: #Insert name of csv file here to analyze

    pol = []
    sub = []
    print("Loading graph, please wait...")

    rows = csv.reader(csv_file)
    for row in rows:
        sentence = row[0]
        blob = TextBlob(sentence)
        pol.append(blob.sentiment.polarity)
        sub.append(blob.sentiment.subjectivity)

    data = { 'Polarity': pol,
             'Subjectivity': sub}

    df = pd.DataFrame(data, columns = ['Polarity', 'Subjectivity'])
    df.plot (y = 'Subjectivity', x = 'Polarity', kind = 'scatter')
    plt.title('Sentiment Analysis')
    plt.show()

    def avg(lst):
        return sum(lst)/len(lst)

    average = avg(pol)
    print("Average of polarity:", round (average, 2))
    average = avg(sub)
    print("Average of subjectivity:", round(average, 2))