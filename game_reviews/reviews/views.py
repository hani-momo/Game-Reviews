from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, GameForm, ReviewForm, UserProfileForm
from .models import User, Game, Review, UserProfile

'''
Home - Game list
'''
def home(request):
    games = Game.objects.all()
    return render(request, 'home.html', {'games': games})

'''
Registration
'''
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login') 
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

'''
Authentication
'''
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login') 

'''
User Profile
'''
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    reviews = Review.objects.filter(author=user)
    created_games = Game.objects.filter(developer=user)

    context = {
        'user': user,
        'reviews': reviews,
        'created_games': created_games,
    }
    
    return render(request, 'user_profile.html', context)

'''
Edit User profile
'''
def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})

'''
Creating game profile
'''
@login_required
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = GameForm()
    return render(request, 'add_game.html', {'form': form})

'''
Game profile
'''
def game_profile(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    reviews = Review.objects.filter(game=game)

    total_reviews = reviews.count()
    if total_reviews > 0:
        positive_reviews = reviews.filter(rating__gte=6).count()
        negative_reviews = reviews.filter(rating__lt=6).count()
        positive_percentage = (positive_reviews / total_reviews) * 100
        negative_percentage = (negative_reviews / total_reviews) * 100
    else:
        positive_percentage = 0
        negative_percentage = 0

    context = {
        'game': game,
        'reviews': reviews,
        'total_reviews': total_reviews,
        'positive_percentage': positive_percentage,
        'negative_percentage': negative_percentage,
    }
    return render(request, 'game_profile.html', context)

'''
Add review
'''
@login_required
def add_review(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.game = game
            review.save()
            return redirect('game_profile', game_id=game.id) 
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form, 'game': game})