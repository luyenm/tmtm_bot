import re
import pandas as pd
import numpy as np

data = pd.read_csv('Administrative/dictionary.csv')
blacklist = data.loc[:, 'BlackList'].dropna()
whitelist = data.loc[:, 'WhiteList'].dropna()


# Sifts through the black and whitelist for words in the messages
# If a word is in the white-list it ignores the word.
# Returns a boolean depending if it finds a word in the blacklist
def checkphrase(message):
    phrase = message.content.lower()
    processed_word = ''
    if any(safe_words in phrase for safe_words in whitelist.tolist()):
        for safe_word in whitelist.tolist():
            processed_word = phrase[:phrase.index(safe_word)] + phrase[len(safe_word) * 2:]
    else:
        processed_word = phrase
    if any(banned_words in processed_word.replace(' ', '') for banned_words in blacklist.tolist()):
        return 1
    return 0

