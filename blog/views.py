from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
import datetime
from .models import Post
# Create your views here.

articles = [
    {
        'slug': 'post-1',
        'author': 'John Doe',
        'date': datetime.date(2024, 1, 28),
        'image': "coding.jpg",
        'title': 'First Post',
        "excerpt": "Extract specific key values from a list of dictionaries in Python",
        "content": "This article explains how to get a list of specific key values from a list of dictionaries with common keys in Python. Lists of dictionaries are frequently encountered when reading JSON; see the following article on reading and writing JSON in Python. Note that a list of dictionaries can be converted to pandas.DataFrame. Extract specific key values using list comprehension and the get() method. Use list comprehension in combination with the get() method of dictionaries."
    },
    {
        'slug': 'post-2',
        'author': 'Jane Smith',
        'date': datetime.date(2024, 3, 27),
        'image': "woods.jpg",
        'title': 'Second Post',
        "excerpt": "Building a Dictionary Incrementally",
        "content": "Defining a dictionary using curly braces and a list of key-value pairs, as shown above, is fine if you know all the keys and values in advance. But what if you want to build a dictionary on the fly? You can start by creating an empty dictionary, which is specified by empty curly braces. Then you can add new keys and values one at a time."
    },
    {
        'slug': 'post-3',
        'author': 'Alex Johnson',
        'date': datetime.date(2024, 2, 26),
        'image': "mountains.jpg",
        'title': 'Third Post',
        "excerpt": "Can build up a dict by starting with the empty dict {} and storing key/value pairs into the dict like this",
        "content": "By default, iterating over a dict iterates over its keys. A for loop on a dictionary iterates over its keys by default. The keys will appear in an arbitrary order. The methods dict.keys() and dict.values() return lists of the keys or values explicitly. There's also an items() which returns a list of (key, value) tuples, which is the most efficient way to examine all the key value data in the dictionary. All of these lists can be passed to the sorted() function."
    },  {
        'slug': 'post-4',
        'author': 'Mona pop',
        'date': datetime.date(2024, 3, 28),
        'image': "mountains.jpg",
        'title': 'Fourth Post',
        'excerpt': 'This is the third post. buold your own application for the first',
        'content': 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...'
    }
]


def index(request):
    all_posts = Post.objects.all()
    latest_articles = sorted(all_posts, key=lambda x: x.date, reverse=True)
    return render(request, "blog/index.html", {"articles": latest_articles[-3:]})


def posts(request):
    all_posts = Post.objects.all()
    return render(request, "blog/posts.html", {"articles": all_posts})


def post_detail(request, slug):
    all_posts = Post.objects.all()
    post = next(x for x in all_posts if x.slug == slug)
    return render(request, "blog/post_detail.html", {"post": post})
