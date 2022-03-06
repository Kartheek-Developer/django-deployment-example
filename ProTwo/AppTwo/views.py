from django.shortcuts import render
from AppTwo.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html')

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'AppTwo/users.html', {'form': form})

def help(request):
    my_dict = {'insert_me': 'Help Page'}
    return render(request, 'AppTwo/help.html', context=my_dict)
