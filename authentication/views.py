from django.shortcuts import render

from authentication.forms import SignupForm

# Create your views here.
def signup(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        print(form.errors)

    return render(request, 'signup.html', {'form': SignupForm()})