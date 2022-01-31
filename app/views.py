from django.shortcuts import render
from django.http import HttpResponse
import cgi, cgitb
import pickle


# Create your views here.
def home(request):
    return render(request, 'index.html')
def analyser(request):
    request.method = 'POST'
    a = request.POST['q1']
    if a == 'Yes':
        res1 = 1
    else:
        res1 = 0
    
    a = request.POST['q2']
    if a == 'Yes':
        res2 = 1
    else:
        res2 = 0
    
    a = request.POST['q3']
    if a == 'Yes':
        res3 = 1
    else:
        res3 = 0
    
    a = request.POST['q4']
    if a == 'Yes':
        res4 = 1
    else:
        res4 = 0
    
    a = request.POST['q5']
    if a == 'Yes':
        res5 = 1
    else:
        res5 = 0
    
    a = request.POST['q6']
    if a == 'Yes':
        res6 = 1
    else:
        res6 = 0
    
    a = request.POST['q7']
    if a == 'Yes':
        res7 = 1
    else:
        res7 = 0
    
    a = request.POST['q8']
    if a == 'Yes':
        res8 = 1
    else:
        res8 = 0
    
    responses = [[res1, res2, res3, res4, res5, res6, res7, res8]]
    
    with open('model', 'rb') as f:
        model = pickle.load(f)
   
    rest = model.predict(responses)
   
    if rest ==0:
        prediction = 'According to the information supplied, this patient is "Negative"! He should be diagnose for a different infection'
    else:
        prediction = 'This patient is Schistosomisis "Positive". Therefore, necessary medications is reccomended'
    
    context = {'prediction': prediction}
    return render(request, 'index.html', context)