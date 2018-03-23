from django.shortcuts import render
from urllib import request
from django.views.generic.edit import CreateView
from .models import Words
from django.db.models import IntegerField
from django.db.models.functions import Cast
import operator


# Create your views here.

class Home(CreateView):
    model = Words
    fields = ['number_of_words']

def result(request1, pk):
    count = Words.objects.filter(id=pk)
    c = int(count)
    print (c)
    url = 'http://terriblytinytales.com/test.txt'
    fr = request.urlopen(url)
    strings = fr.read()
    string = str(strings)
    words = string.split(' ')
    clean_words = []
    symbols = ['(', ')', '?', ',', '. ', ' / ', ' @', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '"']
    for word in words:
        for i in range(0, len(symbols)):
            word = word.replace(r'\n', '')
            word = word.replace('â€“', ',')
            word = word.replace('â€™s', 'is')
            word = word.replace('â€™re', 'are')
            word = word.replace('â€™ve', 'have')
            word = word.replace('nâ€™t', 'not')
            word = word.replace('â€™ll', 'will')
            word = word.replace(symbols[i], '')
        if len(word) > 0:
            clean_words.append(word)
    words_dic = {}
    for word in clean_words:
        if word in words_dic:
            words_dic[word] = words_dic[word] + 1
        else:
            words_dic[word] = 1

    words_dic = [words_dic[k] for k in sorted(words_dic.keys())[:count]]

    #words_dict = sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request1, 'job/result.html',
                  {'words_dic': words_dic,
                   'count': count}
                   )


