from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    #return HttpResponse("Hello welcome to home page")
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist=fulltext.split()
    wordcount={}

    for i in wordlist:
        if i in wordcount:
            wordcount[i]+=1
        else:
            wordcount[i]=1

    sortedlist=sorted(wordcount.items(),key=operator.itemgetter(1),reverse=True)


    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedlist':sortedlist})

def about(request):
    return render(request,'about.html')
