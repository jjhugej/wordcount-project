from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def eggs(request):
    return HttpResponse('eggs baby')


def count(request):
    fulltext = request.GET['fulltext']
    print (fulltext)
    wordList = fulltext. split(' ')

    wordDictionary = {}

    for i in wordList:
        if i in wordDictionary:
           wordDictionary[i] += 1
        else:
            wordDictionary[i] =1

    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse = True)
    

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordList), 'wordDictionary': sortedWords})