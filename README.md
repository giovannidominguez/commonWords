# CommonWords
CommonWords is a script written in Python3 that pulls from Hackernews
API and returns to the console the top 100 most frequent words ranked
along with their occurences from the top 30 stories and first 10
comments from each Hackernews post

Below is a preview of the output on the console

![Preview of output of top words on HackerNews](https://github.com/giovannidominguez/commonWords/blob/master/previewCommonWords.png)




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

## TESTING
Right now there are a few minor tests but will continue to add.
Current tests check for correct output upon expected input.
TODO: Add more edge cases for unexpected parameters 

To run the tests: 
```bash
python3 -m unittest common_tests.py 
```
