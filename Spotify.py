import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.offline as ply
import plotly.express as px


music = pd.read_csv('data.csv')

music['artists'] = music['artists'].apply(lambda x: x[1:-1].replace("'",''))  #Remove The brackets

corr = music.corr()
#plt.figure(figsize=(18,8))
#sns.heatmap(corr, annot=True,cmap='RdBu_r', square=True)   #Correlation: Year vs Popularity and Energy vs Loudness
#plt.show()

def popularity():  #Most Popular Artists overall
    x = music.groupby('artists')['popularity'].sum().sort_values(ascending=False)[:20]
    sns.barplot(x.index, x)
    plt.xticks(rotation=90)
    plt.show()
#print(popularity())

def recentPopularity():
    popular = music.sort_values('popularity', ascending=False).head(20)
    popular = popular[['artists', 'name', 'popularity', 'year']]
    new = popular.groupby('name')['popularity'].sum().sort_values(ascending=False).head(20)
    sns.barplot(new.index, new)
    plt.xticks(rotation=90)
    plt.show()
#print(recentPopularity())

def FirstDecade():
    Decade = (music['year'] >= 2000) & (music['year'] <= 2010)   #Popular Artists in the 2000s
    First = music[Decade]
    sort = First.groupby('artists')['popularity'].sum().sort_values(ascending=False).head(20)
    sns.barplot(sort.index, sort)
    plt.xticks(rotation=90)
    plt.show()
#print(FirstDecade())

def SecondDecade():
    Second = (music['year'] >= 2010) & (music['year'] <= 2020)
    Full = music[Second]
    second_sort = Full.groupby('artists')['popularity'].sum().sort_values(ascending=False).head(20)
    sns.barplot(second_sort.index, second_sort)
    plt.xticks(rotation=90)
    plt.show()
#print(SecondDecade())

def popularSongs():
    songs = music.groupby('name')['popularity'].sum().sort_values(ascending=False).head(20)
    sns.barplot(songs.index, songs)
    plt.xticks(rotation=90)
    plt.show()
#print(popularSongs())

def testArtist():
    Queen = music[music['artists'] == 'The Beatles']
    sns.lineplot(x='release_date', y='popularity', data=Queen)
    plt.xlabel('Year')
    plt.ylabel('Popularity')
    plt.xticks(rotation=90)
    plt.show()
#print(testArtist())


def timeGraph():
    sns.set(style='whitegrid')
    plt.figure(figsize=(10,8))
    types = ['acousticness','danceability','liveness']
    for type in types:
        mean = music.groupby('year')[type].mean()
        axis = sns.lineplot(x=mean.index, y=mean, label=type)
    plt.show()
#print(timeGraph())

def TempoGraph():
    sns.set(style='whitegrid')
    plt.figure(figsize=(10,8))
    tempo = ['tempo', 'loudness']
    for t in tempo:
        tempo_mean = music.groupby('year')[t].mean()
        temp_graph = sns.lineplot(x=tempo_mean.index, y=tempo_mean)
        plt.ylabel('Mean Measure')
        plt.show()
#print(TempoGraph())

def explicit():
    sns.set(style='whitegrid')
    plt.figure(figsize=(10,8))
    bad = ['explicit']
    for b in bad:
        bad_mean = music.groupby('year')[b].mean()
        bad_graph = sns.lineplot(x=bad_mean.index, y=bad_mean, label=b)
        plt.ylabel('Mean Measure')
        plt.show()
#print(explicit())

