from django.shortcuts import render

# Create your views here.
def home(request) :
    return render(request, "home.html")

def result(request):
    sentence = request.GET['sentence']
    wordList = sentence.split() # 공백자 기준 구분
    wordDict = {} #empty dict

    for word in wordList :
        if word in wordDict :
            wordDict[word] += 1 #단어 있으면 개수 +1
        else :
            wordDict[word] = 1

    return render(request, "result.html", {'fulltext':sentence, 'count':len(wordList), "wordDict":wordDict.items})