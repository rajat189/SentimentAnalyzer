from django.shortcuts import render
from sentimentAnalyzer.util.sentimentDAO import Analysis


def index(request):
    return render(request, 'sentimentAnalyzer/index.html')


def analyzedData(request):
    if request.method == 'GET':

        req_tag = request.GET.get("searchTag")

        analyzer = Analysis()
        analyzed_data = analyzer.analyzedData(req_tag)
        analyzed_data['tag'] = '#' + req_tag.upper()
        return render(request, 'sentimentAnalyzer/analysis.html', analyzed_data)