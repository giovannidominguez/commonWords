# CommonWords
CommonWords is a script written in Python3 that pulls from Hackernews
API and returns to the console the top 100 most frequent words ranked
along with their occurences from the top 30 stories and first 10
comments from each Hackernews post
![Preview of output of top words on HackerNews]

The files provided are commonWords.py, commonWordsBonus.py, and
commonModule.py

# Dependencies
CommonWords is dependent on [Requests](https://2.python-requests.org/en/master/) for python. User
defined methods are placed in the commonModule within the same directory

# Installation
## To install Requests run command: 
```bash
pip3.x install requests 
```
and/or
```bash
python3.x -m pip install
```
## To run CommonWords: 
```python
python3 commonWords.py
```

## To run CommonWordsBonus:
```python
python3 commonWordsBonus.py
```
CommonWordsBonus does the same as CommonWords but ignores the top 100
words in the english language
