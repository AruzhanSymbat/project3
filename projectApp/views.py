from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .models import Feedback
from .forms import FeedbackCreate
from .forms import UserCreate
from django.core.mail import EmailMessage
def send_message(request):
    email=EmailMessage(
        'Hello',
        'This is automated message. Thank you for leaving feedback. You can also register if you are not registred yet.',
        'lessonacc02@gmail.com', 
        ['200103330@stu.sdu.edu.kz','arusymatkyzy@gmail.com'],
        headers={'Message-ID':'foo'},
    )
    email.send(fail_silently=False)
    return render(request, 'projectApp/message.html')


#def index(request):
    #return HttpResponse('Where to go on holidays?')
def first(request):
    return render(request, 'projectApp/firstpage.html')
def second(request):
    return render(request, 'projectApp/next.html')
def third(request):
    return render(request, 'projectApp/nature.html')
def next(request):
    return render(request, 'projectApp/second.html')
def exml(request):
    posts = Posts.objects.all()
    return render(request, 'projectApp/firstmodel.html',{'posts':posts,'title':'Where to go on this month in Almaty?'})
def exml1(request):
    posts = Nature.objects.all()
    return render(request, 'projectApp/secondmodel.html',{'posts':posts,'title':'Nature beauties of Kazakhstan'})
# Create your views here.
#DataFlair
def index(request):
    shelf = Feedback.objects.all()
    return render(request, 'projectApp/comment.html', {'shelf': shelf})

def upload(request):
    upload = FeedbackCreate()
    if request.method == 'POST':
        upload = FeedbackCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'projectApp/upload_form.html', {'upload_form':upload})

def register(request):
    register = UserCreate()
    if request.method == 'POST':
        register = UserCreate(request.POST, request.FILES)
        if register.is_valid():
            try:
                register.save()
                return redirect('index')
            except:
                register.add_error(None, 'Your form is wrong.')
                #return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        register = UserCreate()
    return render(request, 'projectApp/registration.html', {'registration':register})
        
def update_feedback(request, feedback_id):
    feedback_id = int(feedback_id)
    try:
        feedback_sel = Feedback.objects.get(id = feedback_id)
    except Feedback.DoesNotExist:
        return redirect('index')
    feedback_form = FeedbackCreate(request.POST or None, instance = feedback_sel)
    if feedback_form.is_valid():
       feedback_form.save()
       return redirect('index')
    return render(request, 'projectApp/upload_form.html', {'upload_form':feedback_form})
def delete_feedback(request, feedback_id):
    feedback_id = int(feedback_id)
    try:
        feedback_sel = Feedback.objects.get(id = feedback_id)
    except Feedback.DoesNotExist:
        return redirect('index')
    feedback_sel.delete()
    return redirect('index')
