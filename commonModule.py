#!/usr/bin/env python3
import string
import requests
import json
from collections import Counter

top100_eng = {'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us', 'The', 'Be', 'To', 'Of', 'And', 'A', 'In', 'That', 'Have', 'I', 'It', 'For', 'Not', 'On', 'With', 'He', 'As', 'You', 'Do', 'At', 'This', 'But', 'His', 'By', 'From', 'They', 'We', 'Say', 'Her', 'She', 'Or', 'An', 'Will', 'My', 'One', 'All', 'Would', 'There', 'Their', 'What', 'So', 'Up', 'Out', 'If', 'About', 'Who', 'Get', 'Which', 'Go', 'Me', 'When', 'Make', 'Can', 'Like', 'Time', 'No', 'Just', 'Him', 'Know', 'Take', 'People', 'Into', 'Year', 'Your', 'Good', 'Some', 'Could', 'Them', 'See', 'Other', 'Than', 'Then', 'Now', 'Look', 'Only', 'Come', 'Its', 'Over', 'Think', 'Also', 'Back', 'After', 'Use', 'Two', 'How', 'Our', 'Work', 'First', 'Well', 'Way', 'Even', 'New', 'Want', 'Because', 'Any', 'These', 'Give', 'Day', 'Most', 'Us', '<a'}

def wordFrequency(my_str, n):
    split_words = my_str.split()
    count = Counter(split_words)
    top_n = count.most_common(n)
    return top_n

def removeTop100(my_str):
    temp_str = my_str.split()
    new_str = ' '.join([i for i in temp_str if i not in top100_eng])
    return new_str

def createCall(id):
    return 'https://hacker-news.firebaseio.com/v0/item/'+str(id) +'.json?print=pretty'

def getTitle(id):
    response = requests.get(createCall(id))
    idData = json.loads(response.text)
    if idData is not None:
        return idData.get("title")
    else:
        return ""

def getCommentIds(id): 
    response = requests.get(createCall(id))
    idData = json.loads(response.text)
    if idData is not None:
        cmt_Ids = idData.get("kids")
        return cmt_Ids
    else: 
        return ""

def getComment(id):
    response = requests.get(createCall(id))
    idData = json.loads(response.text)
    if idData is not None:
        return idData.get("text")
    else:
        return ""