from django.shortcuts import render
from . import titanic_predict


def home(request):
    return render(request, 'index.html')


def result(request):
    pclass = request.POST['pclass']
    sex = request.POST['sex']
    age = request.POST['age']
    sibsp = request.POST['sibsp']
    parch = request.POST['parch']
    fare = request.POST['fare']
    embarked = request.POST['embarked']

    prediction = titanic_predict.make_titanic_prediction(pclass, sex, age, sibsp, parch, fare, embarked)

    if prediction == 0:
        status = 'dead'
    elif prediction == 1:
        status = 'alive'
    return render(request, 'result.html', {'status': status})
