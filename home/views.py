from django.shortcuts import render, redirect
from home.models import Person, Admin, Message , Message2
from django.contrib import messages
from twilio.rest import Client


#srvsms  ps- Avinash$$123
# admin section
def adminlogin(request):
    if request.method == 'POST':
        print ('check')
        try:
            data=Admin.objects.get(username = request.POST['uname'],password = request.POST['psw'] )
            print("Username= ",data)
            request.session['username']=data.username
            return redirect('adminindex')
        except Admin.DoesNotExist as e:
            messages.success(request,'username / Password Invalid..!')
            return redirect('admin')
    else:
        return render(request, 'signin.html')

def adminindex(request):
   
    return render(request, 'adminindex.html')

def adminlogout(request):
    try:
        del request.session['username']
        return redirect('admin')
    except:
        return render(request, 'signin.html') 

def contact(request):
    user = Person.objects.all()  
    return render(request, 'contact.html',{'users':user})

#end admin section
#user section
def login(request):
    if request.method == 'POST':
        print ('check')
        try:
            data=Person.objects.get(username = request.POST['uname'],password = request.POST['psw'] )
            print("Username= ",data)
            request.session['username']=data.username
            return redirect('home')
        except Person.DoesNotExist as e:
            messages.success(request,'username / Password Invalid..!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def index(request):
   
    return render(request, 'index.html')    

def signup(request):
    if request.method == 'POST':
        data = Person()
        data.f_name = request.POST['fname']
        data.l_name = request.POST['lname']
        data.username = request.POST['uname']
        data.ph_number = request.POST['number']
        data.email = request.POST['email']
        data.password = request.POST['pass']
        data.address = request.POST['add']
        data.city = request.POST['city']
        data.pin = request.POST['pin']
        data.save()
        messages.success(request,"New contact Registered Sucessfully")

        return redirect('contact')
    else:
        return render(request, 'contact.html')

def msg_single(request):
    if request.method == 'POST':
        data = Message()
        data.msg_from = request.POST['twilio_number']
        data.msg_to = request.POST['number']
        data.account_type = request.POST['ac_type']
        data.msg = request.POST['message']
        data.save()

        account_sid = 'ACf69a4020e336cb159bd4cebda28965b6'
        auth_token = '37fdeed5c116469ea817085552775ea4'
        client = Client(account_sid, auth_token)
 
        message = client.messages.create(
                                    body=request.POST['message'],
                                    from_= request.POST['twilio_number'],
                                    media_url=['https://demo.twilio.com/owl.png'],
                                    to= request.POST['number']
                                )

        print(message.sid)
        messages.success(request,"Message Sent Succesfully")

        return redirect('msg_single')
    else:
        admin_data = Admin.objects.all()
        return render(request, 'message_single.html',{'record':admin_data})

def msg_bulk(request):
    if request.method == 'POST':
        data = Message()
        data.msg_from = request.POST['twilio_number']
        data.msg_to = request.POST['number']
        data.account_type = request.POST['ac_type']
        data.msg = request.POST['message']
        data.save()

        account_sid = 'ACf69a4020e336cb159bd4cebda28965b6'
        auth_token = '37fdeed5c116469ea817085552775ea4'
        client = Client(account_sid, auth_token)
 
        message = client.messages.create(
                                    body=request.POST['message'],
                                    from_= request.POST['twilio_number'],
                                    media_url=['https://demo.twilio.com/owl.png'],
                                    to= request.POST['number']
                                )

        print(message.sid)
        messages.success(request,"Message Sent Succesfully")

        return redirect('msg_bulk')
    else:
        admin_data = Admin.objects.all()
        return render(request, 'message_bulk.html',{'record':admin_data})



def logout(request):
    try:
        del request.session['username']
        return redirect('login')
    except:
        return render(request, 'login.html')
        




    