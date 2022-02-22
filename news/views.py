from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import News
# Create your views here.
def home(request):
    news = News.objects.all().exclude(ad=True).order_by("-created")
    Ads = News.objects.all().exclude(ad=False).order_by("-created")[:5]
    paginator = Paginator(news, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if "get_page" in request.GET:
        return render(request, "news/news_card.html", context={"news": page_obj, })
    
    
    context={
        "title": "معهد السويس لنظم المعلومات الإدارية",
        "news": page_obj,
        "Ads":Ads,
    }
    return render(request,"news/home.html",context)

def post_details(request,id):
    post=get_object_or_404(News,id=id)
    context={
        "title": f"{post.title}",
        "post": post,
        
    }
    return render(request,"news/post_details.html",context)


def about(request):
    context = {
        "title": "عن المعهد",
    }
    return render(request,"news/about.html",context)


def brigadier(request):
    context = {
        "title": "كلمة العميد",
    }
    return render(request,"news/brigadier.html",context)