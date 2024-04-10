from django.shortcuts import render, redirect
from .models import Book, Category
from .forms import CategoryForm, BookForm
from django.contrib import messages

# Create your views here.

def listcategory(request):
    if request.user.is_authenticated:
        categories = Category.objects.all
        return render(request, 'book/listcategory.html', {'categories':categories})
    else:
        messages.success(request, "Must be logged in to do that!")
        return redirect('home')


def addcategory(request):
    form = CategoryForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                addcategory = form.save()
                return redirect('listcategory')
        return render(request, 'book/addcategory.html', {'form': form})
    else:
        messages.success(request, "Must be logged in to do that!")
        return redirect('home')


def updatecategory(request, pk):
    if request.user.is_authenticated:
        category = Category.objects.get(id=pk)
        form = CategoryForm(request.POST or None, instance=category)
        if form.is_valid():
            form.save()
            return redirect('listcategory')
        return render(request, 'book/updatecategory.html', {'category': category, 'form': form})
    else:
        messages.success(request, "Must be logged in to do that!")
        return redirect('home')


def deletecategory(request, pk):
    if request.user.is_authenticated:
        category = Category.objects.get(id=pk)
        if request.method == 'POST':
            category.delete()
            return redirect('listcategory')
        return render(request, 'book/deletecategory.html', {'category': category})     
    else:
        messages.success(request, "Must be logged in to do that!")
        return redirect('home')


def addbook(request):
    form = BookForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                addrecord = form.save()
                messages.success(request, "Record saved!")
                return redirect('home')
        return render(request, 'book/addbook.html', {"form": form})
    else:
        messages.success(request, "Must be logged in to do that!")
        return redirect('home')


def updatebook(request, pk):
    if request.user.is_authenticated:
        book = Book.objects.get(id=pk)
        form = BookForm(request.POST or None, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated!")
            return redirect('home')
        return render(request, 'book/updatebook.html', {"book": book, "form": form})       
    else:
        messages.success(request, "Must be logged in to do that!")
        return redirect('home')
    

def deletebook(request, pk):
    if request.user.is_authenticated:
        book = Book.objects.get(id=pk)
        if request.method == "POST":
            book.delete()
            messages.success(request, "Record deleted!")
            return redirect('home')
        return render(request, 'book/deletebook.html', {'book': book})
    else:
        messages.success(request, "Must be logged in to do that!")
        return redirect('home')


def searchbook(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            searched = request.POST['searched']
            booktitles = Book.objects.filter(title__contains=searched)
            return render (request, 'book/searchbook.html',
                            {'searched':searched,
                             'booktitles': booktitles,})
        else:
            return render (request, 'book/searchbook.html', {})
    else:
        messages.success(request, "Must be logged in to do that!")
        return redirect('home')


def searchbycategory(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            searchedbycategory = request.POST['searchedbycategory']
            cats = Book.objects.filter(category__in=Category.objects.filter(category=searchedbycategory))
            return render (request, 'book/searchbycategory.html',
                           {'searchedbycategory': searchedbycategory,
                            'cats': cats})
        else:
            return render (request, 'book/searchbycategory.html', {})
    else:
        messages.success(request, "Must be logged in to do that!")
        return redirect('home')


def showexpenseView(request):
    if request.user.is_authenticated:
        BA = DE = DS = DL = Ma = NLP = Py = RS = SQL = St = V = 0.0
        cat_list = []
        for categ in Category.objects.values_list('category', flat=True):
            num_of_book = Book.objects.filter(category__in=Category.objects.filter(category=categ))
            cat_list.append(categ)
            for book in num_of_book:
                if categ == 'Business Analytics':
                    BA += book.distribution_expense
                if categ == 'Data Ethics':
                    DE += book.distribution_expense
                if categ == 'Data Science':
                    DS += book.distribution_expense
                if categ == 'Deep Learning':
                    DL += book.distribution_expense
                if categ == 'Maths':
                    Ma += book.distribution_expense
                if categ == 'NLP':
                    NLP += book.distribution_expense
                if categ == 'Python':
                    Py += book.distribution_expense
                if categ == 'R Studio':
                    RS += book.distribution_expense
                if categ == 'SQL':
                    SQL += book.distribution_expense
                if categ == 'Statistics':
                    St += book.distribution_expense
                if categ == 'Visualization':
                    V += book.distribution_expense

        return render(request, 'book/showexpense.html', {'BA': round(BA, 2),
                                                         'DE': round(DE, 2),
                                                         'DS': round(DS, 2),
                                                         'DL': round(DL, 2),
                                                         'Ma': round(Ma, 2),
                                                         'NLP': round(NLP, 2),
                                                         'Py': round(Py, 2),
                                                         'RS': round(RS, 2),
                                                         'SQL': round(SQL, 2),
                                                         'St': round(St, 2),
                                                         'V': round(V, 2),
                                                         'cat_list': cat_list})
    
    else:
        messages.success(request, "Must be logged in to do that!")
        return redirect('home')



