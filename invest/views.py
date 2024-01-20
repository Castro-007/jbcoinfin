from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm, DepositForm, EditUserForm, EditProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Deposit, Profile
# Create your views here.


def index(request):

    return render(request, 'index.html')

def about(request):

    return render(request, 'abtpage.html')
@login_required(login_url='/login/')
def dashboard(request):
    user = request.user
    deposits = Deposit.objects.filter(user=user)
    total_deposits = get_total_invest(list(deposits.values()))
    successful_deposits = Deposit.objects.filter(user=user, status='successful')
    total_profits = get_total_profit(list(successful_deposits))
    total_successful_deposits = get_total_invest(list(successful_deposits.values()))
    return render(request, 'dashboard/index.html', {'user': user,
                                                    'total_deposits': total_deposits,
                                                    'total_profits': total_profits,
                                                    'total_successful_deposits': total_successful_deposits})


def register_request(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect('dashboard')

    form = NewUserForm()
    return render(request, 'register.html', {'form': form})

def login_request(request):

    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, "Login Successful")
                return redirect('dashboard')
            else:
                messages.error(request, "invalid username or password")

        else:
            messages.error(request, "invalid username or password")

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form}) 


@login_required(login_url='/login/')
def logout_request(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def deposit_init(request):
    user = request.user
    deposits = Deposit.objects.filter(user=user)
    total_deposits = get_total_invest(list(deposits.values()))
    successful_deposits = Deposit.objects.filter(user=user, status='successful')
    total_successful_deposits = get_total_invest(list(successful_deposits.values()))
    total_profits = get_total_profit(list(successful_deposits))

    if request.method == "POST":
        form = DepositForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            
            print(user)
            form.user = user
            form.save()
            print(form.id)
            return redirect(reverse('deposit', kwargs={'deposit_id': form.id}))

        else:
            print("is Invalid")
            messages.error(request, "Invalid inputs")
    form = DepositForm()
    return render(request, 'dashboard/deposit.html', {'form': form,
                                            'user': user,
                                            'total_deposits': total_deposits,
                                            'total_profits': total_profits,
                                            'total_successful_deposits': total_successful_deposits,
                                            })


def dep_confirm(request, deposit_id):
    user = request.user
    deposits = Deposit.objects.filter(user=user)
    total_deposits = get_total_invest(list(deposits.values()))
    successful_deposits = Deposit.objects.filter(user=user, status='successful')
    total_successful_deposits = get_total_invest(list(successful_deposits.values()))
    total_profits = get_total_profit(list(successful_deposits))

    deposit = get_object_or_404(Deposit, id=deposit_id)
    return render(request, 'dashboard/depo-ethereum.html', {
        'deposit': deposit,
        'total_deposits': total_deposits,
        'total_profits': total_profits,
        'total_successful_deposits': total_successful_deposits,
        })

@login_required(login_url='/login/')
def dep_success(request, id):
    user = request.user
    deposit = get_object_or_404(Deposit, id=id)

    return render(request, 'dashboard/successful.html', {'user': user,
                                                         'deposit': deposit})

def get_total_invest(deposits):
    total_invest = 0
    for deposit in deposits:
        deposit_amount = deposit['deposit']
        total_invest += deposit_amount

    return total_invest

def get_total_profit(deposits):
    total_profits = 0
    total_deposits = 0
    for deposit in deposits:
        profit_amount = deposit.profit
        total_profits += profit_amount
        deposit_amount = deposit.deposit
        total_deposits += deposit_amount

    total_profits += int(total_deposits)
    return round(total_profits)

@login_required(login_url='/login/')
def investment_stats(request):
    user = request.user
    
    deposits = Deposit.objects.filter(user=user)
    total_deposits = get_total_invest(list(deposits.values()))
    successful_deposits = Deposit.objects.filter(user=user, status='successful')
    total_successful_deposits = get_total_invest(list(successful_deposits.values()))
    total_profits = get_total_profit(list(successful_deposits))
    total_deposits = get_total_invest(list(deposits.values()))
    return render(request, 'dashboard/investments.html', {'deposits': deposits,
                                                          'total_deposits': total_deposits,
                                                          'user': user,
                                                          'total_deposits': total_deposits,
                                                          'total_profits': total_profits,
                                                            'total_successful_deposits': total_successful_deposits,
                                                          })


@login_required(login_url='/login/')
def profile(request):
    user = request.user
    deposits = Deposit.objects.filter(user=user)
    total_deposits = get_total_invest(list(deposits.values()))
    successful_deposits = Deposit.objects.filter(user=user, status='successful')
    total_successful_deposits = get_total_invest(list(successful_deposits.values()))
    total_profits = get_total_profit(list(successful_deposits))
    total_deposits = get_total_invest(list(deposits.values()))

    try:
        profileInstance = Profile.objects.get(user=user)

    except:
        profileInstance = Profile.objects.create(user=user)
    
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        form1 = EditProfileForm(request.POST, instance=profileInstance)

        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            return redirect('profile')

        else:
            messages.error(request, "please fill in input properly")
            

    form = EditUserForm(instance=user)
    form1 = EditProfileForm(instance=profileInstance)
    return render(request, 'dashboard/profile.html', {'user': user,
                                                      'profile': profileInstance,
                                                      'form': form,
                                                      'form1': form1,
                                                      'total_deposits': total_deposits,
                                                      'total_profits': total_profits,
                                                        'total_successful_deposits': total_successful_deposits,
                                                      })


def password_change(request):

    user = request.user
    deposits = Deposit.objects.filter(user=user)
    total_deposits = get_total_invest(list(deposits.values()))
    successful_deposits = Deposit.objects.filter(user=user, status='successful')
    total_profits = get_total_profit(list(successful_deposits))

    total_successful_deposits = get_total_invest(list(successful_deposits.values()))
    total_deposits = get_total_invest(list(deposits.values()))

    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    
    form = PasswordChangeForm(user=user)
    return render(request, 'dashboard/password.html', {'user': user,
                                                       'form': form,
                                                       'total_deposits': total_deposits,
                                                       'total_profits': total_profits,
                                                        'total_successful_deposits': total_successful_deposits,
                                                       })