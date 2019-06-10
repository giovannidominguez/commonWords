CommonWords is a script written in Python3 that pulls from Hackernews
API and returns to the console the top 100 most frequent words ranked
along with their occurences from the top 30 stories and first 10
comments from each Hackernews post

The files provided are commonWords.py, commonWordsBonus.py, and
commonModule.py

DEPENDINCIES CommonWords is dependent on Requests for python. User
defined methods are placed in the commonModule within the same directory

To install Requests run command: pip3.x install requests and/or
python3.x -m pip install

To run CommonWords: python3 commonWords.py

CommonWordsBonus does the same as CommonWords but ignores the top 100
words in the english language

To run CommonWordsBonus: python3 commonWordsBonus.py
