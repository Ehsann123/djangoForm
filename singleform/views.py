from django.shortcuts import render, redirect
from .forms import StepOneForm, StepTwoForm, StepThreeForm

def step_one_view(request):
    if request.method == 'POST':
        form = StepOneForm(request.POST)
        if form.is_valid():
            request.session['step_one_data'] = form.cleaned_data
            return redirect('step_two')
    else:
        form = StepOneForm()
    return render(request, 'singleform/step_one.html', {'form': form})

def step_two_view(request):
    if request.method == 'POST':
        form = StepTwoForm(request.POST)
        if form.is_valid():
            step_one_data = request.session.get('step_one_data')
            step_two_data = form.cleaned_data
            complete_data = {**step_one_data, **step_two_data}
            request.session['step_two_data'] = complete_data
            return redirect('step_three')
    else:
        form = StepTwoForm()
    return render(request, 'singleform/step_two.html', {'form': form})

def step_three_view(request):
    if request.method == 'POST':
        form = StepThreeForm(request.POST)
        if form.is_valid():
            step_one_data = request.session.get('step_one_data')
            step_two_data = request.session.get('step_two_data')
            if not step_one_data or not step_two_data:
                return redirect('step_one')  
            step_three_data = form.cleaned_data
            complete_data = {**step_one_data, **step_two_data, **step_three_data}
            request.session['complete_data'] = complete_data
            print("complete_data:", complete_data) 
            return redirect('success')  
    else:
        form = StepThreeForm()
    return render(request, 'singleform/step_three.html', {'form': form})

def success_view(request):
    complete_data = request.session.get('complete_data')
    print("complete_data:", complete_data)

    return render(request, 'singleform/success.html', {'complete_data': complete_data})