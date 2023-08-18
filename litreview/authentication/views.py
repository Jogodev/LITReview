from authentication.models import User, UserFollows
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect

from . import forms


def logout_user(request):
    """logout_user"""
    logout(request)
    return redirect("login")


def signup_page(request):
    """Register"""
    form = forms.SignUpForm()
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "authentication/signup.html", context={"form": form})


def login_page(request):
    """login_page"""
    form = forms.LoginForm()
    message = ""
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, "Vous êtes connécté")
                return redirect("home")
            else:
                message = "Identifiants invalides."
    return render(
        request, "authentication/login.html", context={"form": form, "message": message}
    )


@login_required
def subscriptions_page(request):
    """Subscriptions"""
    subscribe_form = forms.SubscribeForm()
    followed_user = UserFollows.objects.filter(user=request.user).order_by(
        "followed_user"
    )
    followed_by = UserFollows.objects.filter(followed_user=request.user).order_by("followed_user")

    if request.method == "POST":
        subscribe_form = forms.SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            pass
        else:
            subscribe_form = forms.SubscribeForm()
    context = {
        "subscribe_form": subscribe_form,
        "followed_user": followed_user,
        "followed_by": followed_by,
    }
    return render(request, "authentication/subscriptions.html", context)


@login_required
def follow(request):
    """Follow"""
    if request.method == "POST":
        subscribe_form = forms.SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            try:
                followed_user = User.objects.get(username=request.POST['followed_user'])
                if request.user == followed_user:
                    messages.error(request, f'Vous ne pouvez pas vous suivre vous même')
                else:
                    try:
                        UserFollows.objects.create(user=request.user, followed_user=followed_user)
                        messages.success(request, f'Vous suivez {followed_user}')
                    except IntegrityError:
                        messages.error(request, f"Vous suivez déjà {followed_user}")
            except User.DoesNotExist:
                messages.error(request, "Cet utilisateur n'existe pas")
        return redirect('subscriptions')


@login_required
def unfollow(request, id):
    """Unfollow"""
    if request.method == "POST":
        unfollow = UserFollows.objects.get(id=id)
        followed_user = unfollow.followed_user
        unfollow.delete()
        messages.warning(request, f'Vous ne suivez plus {followed_user}')
    return redirect('subscriptions')
