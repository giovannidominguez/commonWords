#!/usr/bin/env python3
import requests
import json
from commonModule import wordFrequency, removeTop100, createCall, getTitle, getCommentIds, getComment

##### Beginning of program ######

#retrieve top 30 stories IDs
r = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
data = json.loads(r.text)
del data[30:]

#store values of all top stories and comment IDs in a dictionary
topIds = {}
commentDict = {}
setRange = range(30) 

#string where we concatenate all text
data_str = ""
#collect comment ids for each story and limit to 10
for i in setRange:
    topIds[i] = str(data[i])
    temp = getCommentIds(topIds[i])
    #case for when there are none
    if temp is None:
        temp = []
        commentDict[i] = temp
    else:
        del temp[10:]
        commentDict[i] = temp

#add titles and comments to our string literal
for j in setRange:
    data_str += getTitle(topIds[j]) + " " 
    length = range(len(commentDict[j]))
    if length == 0:
        data_str += ""
    else:
        for k in length:
            temp = getComment(commentDict[j][k])
            if temp is None:
                data_str += ""
            else:
                data_str += temp + " "

#remove ascii &#x27; 
data_final = data_str.replace("&#x27;", "'") 

noTop100 = removeTop100(data_final)
frequencies = wordFrequency(noTop100, 100)

#run frequency method on string and output to console
freq_length = range(len(frequencies))
for i in freq_length:
    print(f'{frequencies[i][0]:15} {frequencies[i][1]:3}')