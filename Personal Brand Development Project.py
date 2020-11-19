######################################
### Personal Development Survey ###

#########################
#### Import Packages ####
#########################
import pandas as pd
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import Blobber
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from dateutil.parser import parse
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#############################
#### Import & Clean Data ####
#############################

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('./My First Project-12908e4c547a.json', scope)
gc = gspread.authorize(credentials)

# Find a workbook by name and open the first sheet
spreadsheet_key = '12J8UoC9yG7UHwiM7koaRah3yNdaqYGxHaUF24gux520'
book = gc.open_by_key(spreadsheet_key)
worksheet = book.worksheet("Form Responses 1")
table = worksheet.get_all_values()

#Convert table data into a dataframe
df = pd.DataFrame(table[1:], columns=table[0])

df = df.drop_duplicates(subset=["When is the last time you've heard me play music?", 'Personality Word #1',
                                'Personality Word #2', 'Personality Word #3'], keep="first")

# Reformat data
personality = pd.melt(df, id_vars=['Timestamp', "When is the last time you've heard me play music?"],
                      value_vars=['Personality Word #1', 'Personality Word #2', 'Personality Word #3'],
                      var_name = 'Category', value_name='personality_words')

music = pd.melt(df, id_vars=['Timestamp', "When is the last time you've heard me play music?"],
                      value_vars=['Music Word #1', 'Music Word #2', 'Music Word #3'],
                      var_name = 'Category', value_name='music_words')

# Define Functions
def toBlob(text):
    return TextBlob(text)

def make_consistent(col_name):
    col_name = col_name.capitalize()
    col_name = col_name.strip()
    col_name = col_name.replace('Hard-working', 'Hardworking')
    return col_name


# Make Data Consistent
music['music_words'] = music['music_words'].apply(make_consistent)
personality['personality_words'] = personality['personality_words'].apply(make_consistent)

# Create Music WordCloud
music_blob = music['music_words']
music_blob = music_blob.to_string()
music_blob = toBlob(music_blob)

allwords = ''.join([wrd for wrd in music_blob])
wordcloud = WordCloud(width=400, height=300, random_state=20, max_font_size=120,
                      collocations=False, color_func=lambda *args, **kwargs: "white").generate(allwords)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Show Music WordCounts
music['music_words'].value_counts()
music.groupby(['music_words', "When is the last time you've heard me play music?"]).count().sort_values('Category', ascending=False)

# Create Personality WordCloud
personality_blob = personality['personality_words']
personality_blob = personality_blob.to_string()
personality_blob = toBlob(personality_blob)

allwords = ''.join([wrd for wrd in personality_blob])
wordcloud = WordCloud(width=400, height=300, random_state=20, max_font_size=120,
                      collocations=False, color_func=lambda *args, **kwargs: "white").generate(allwords)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Show Personality WordCounts
personality['personality_words'].value_counts()
personality.groupby(['personality_words', "When is the last time you've heard me play music?"]).count().sort_values('Category', ascending=False)['Category']


