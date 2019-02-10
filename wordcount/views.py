from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')


def count(request):
	fulltext = request.GET['fulltext']
	wordList = fulltext.split()
	textLength = len(wordList)
	wordDict = {}
	for word in wordList:
		if word in wordDict:
			#increase
			wordDict[word] += 1
		else:
			#add to the dictionary
			wordDict[word] = 1
	sortedWords = sorted(wordDict.items(), key = operator.itemgetter(1), reverse = True)
	return render(request, 'count.html',{
		'textLength' : textLength,
		'fulltext' : fulltext,
		'sortedWords' : sortedWords
		})

def about(request):

	return render(request, 'about.html')