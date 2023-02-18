from django.shortcuts import render, redirect
from cine_app.models import Genre, Movie_list, book3, timeslots, book2
from cinema_proj.settings import MEDIA_ROOT, MEDIA_URL
from cine_app.forms import UserForm, UserProfileInfoForm
from cine_app.forms import bookForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from cine_app.forms import SignUpForm

# Create your views here.
def index(request):
    popular_list = Movie_list.objects.order_by('-rating')
    popular1 = popular_list[2]
    popular2 = popular_list[1]
    popular3 = popular_list[0]
    all_movies = Movie_list.objects.all()

    #for movie in all_movies:
    #    movie_id = movie.id
    #top_movies = Movie_list.objects.filter(id=id)


    Slide_dict = {'movie_title_1': popular1, 'movie_title_2': popular2, 'movie_title_3': popular3, 
    'movie_wallpaper_1': popular1.wallpaper.url , 'movie_wallpaper_2': popular2.wallpaper.url, 'movie_wallpaper_3': popular3.wallpaper.url,
    'movie1_plot': popular1.plot, 'movie2_plot': popular2.plot, 'movie3_plot': popular3.plot, 'popular_list': popular_list, 'all_movies': all_movies, 
     } 
    return render(request, 'cine_app/index.html', context=Slide_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def browse(request):
    popular_list = Movie_list.objects.order_by('-rating')

    if request.method == "POST":
        searched = request.POST['searched']
        search_results = Movie_list.objects.filter(movie_title__contains=searched)
        return render(request, 'cine_app/browse.html', {'searched': searched, 'popular_list': popular_list, 'search_results' : search_results, } )
    else:
        return render(request, 'cine_app/browse.html', {'popular_list': popular_list, })

def show_movie(request, movie_id):
    movie = Movie_list.objects.get(pk=movie_id)
    times = timeslots.objects.all()

    return render(request, 'cine_app/show_movie.html', {'movie': movie, 'times':times})

@login_required
def book_movie(request, movie_id):
    movie = Movie_list.objects.get(pk=movie_id)
    times = timeslots.objects.all()

    initial_data = {
        'seats':1,
        'user' : request.user
    }

    if request.method == 'POST':
        form = bookForm(request.POST)
        form.user = request.user

        #reser = book(movie_title=movie)
        #reser.save()
        
        #form.movie_title = request.POST.get(movie_id)
        #note = form.save(commit=False)
        #note.user = request.user
        #note.movie_title = movie
        #note.save()
        form.save(commit=False)

        if form.is_valid():
            form.save()
            return redirect('booklist') 
            
        else:
            print("error")
            form = bookForm()
    else:
        form = bookForm(initial=initial_data)

    return render(request, 'cine_app/book_movie.html', {'movie': movie, 'times':times, 'form' : form})

class BookDetailsView(DetailView):
    model = book3

class BookListView(ListView):
    model = book3

    def get_queryset(self):
        return book3.objects.all()

class DeleteBookView(DeleteView):
    model = book3
    success_url = reverse_lazy("booklist")

#def showBook(request):
#    return render(request, 'cine_app/show_book.html', {})


#class CreateBookView(CreateView):
#    model = book2
#    form_class = bookForm
#    success_url = reverse_lazy("index")

#    def form_valid(self, form):
#        form.instance.movie_title = self.kwargs['pk']
#        return super().form_valid(form)

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user 

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

                profile.save()

                registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'cine_app/register.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'cine_app/register.html'
    success_url = reverse_lazy('user_login')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone tried to login and failed")
            print("username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'cine_app/login.html' , {})