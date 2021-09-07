#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
We're trying to find all the damn profanity
'''

import regex
from pathlib import Path

########################################################################
### Universal variables ################################################
########################################################################

# load profane words
profaneWords = None  # this has to be a list object so we can do `.join` on it.
profaneWords = ["dick",
                "shit",
                "ass"]

# create regex
profanePattern = "|".join(profaneWords)
pattern = rf"{profanePattern}"

# load text
text = None  # A string object
text = "I love pie. I have a friend named Dick. He talks a lot of shit but it also comes out of his ass."

# Find results
results = regex.findall(pattern, text.lower())

print("The following curse words were found in your text:")
for result in results:
    print("\t" + result)
