from django.shortcuts import render, redirect
import random

values = ['apple', 'pear', 'banana', 'watermelon', 'plum', 'pineapple', 'orange', 'kiwi', 'mango', 'grapes', 'strawberry']

def index(request):
    return render(request, "items_list/index.html")

def results(request):
    if request.method == "POST":
        if request.POST['number']:
            try:
                if int(request.POST['number']) > len(values):
                    context = {
                        'error': "Number to big. Don't have that many surprises. Try something less or equal to " + str(len(values)) +"."
                    }
                    return render(request, "items_list/index.html", context)
                else:
                    request.session['number'] = request.POST['number']
                    random.shuffle(values)
                    print ('*'*50)
                    print (values)
                    print (request.session['number'])
                    print ('*'*50)
                    return redirect("/results" )
            except:
                context = {
                    'error': "Don't be stupid. I said pick a number))!!!"
                }
                return render(request, "items_list/index.html", context)
        else:
            context = {
                'error': "Please choose a number. No empty fields allowed."
            }
            return render(request, "items_list/index.html", context)
    else:
        return redirect('/')

def showList(request):
    surprise_list = []
    for i in range(int(request.session['number'])):
        surprise_list.append(values[i])
    context = {
        'my_list': surprise_list
    }
    print ('#$'*20)
    print (surprise_list)
    print ('#$'*20)
    return render(request, 'items_list/results.html', context)

def back(request):
    return redirect('/')
# Create your views here.
