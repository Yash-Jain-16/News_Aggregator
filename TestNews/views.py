from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from newsapi import NewsApiClient
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from TestNews.models import Bookmark 

# Create your views here.


def home(request):
    newsapi = NewsApiClient(api_key='bb456701776c49a383d06ff36aceb6c8')
    top= newsapi.get_top_headlines(country="in")
    top_business=newsapi.get_top_headlines(country="in",category="business")
    json=top['articles']
    desc=[]
    img=[]
    title=[]
    mylist=[]
    readmore=[]
    for i in range(len(json)):
        desc.append(json[i]['description'])
        title.append(json[i]['title'])
        img.append(json[i]['urlToImage'])
        readmore.append(json[i]['url'])
    mylist=list(zip(title,desc,img,readmore))
    json1 = top_business['articles']
    desc1 = []
    img1 = []
    title1 = []
    mylist1 = []
    readmore1 = []
    for i in range(len(json1)):
        desc1.append(json1[i]['description'])
        title1.append(json1[i]['title'])
        img1.append(json1[i]['urlToImage'])
        readmore1.append(json1[i]['url'])
    mylist1 = list(zip(title1, desc1, img1, readmore1))
    top_sports = newsapi.get_top_headlines(country="in", category="sports")
    json2 = top_sports['articles']
    desc2 = []
    img2 = []
    title2 = []
    mylist2 = []
    readmore2 = []
    for i in range(len(json2)):
        desc2.append(json2[i]['description'])
        title2.append(json2[i]['title'])
        img2.append(json2[i]['urlToImage'])
        readmore2.append(json2[i]['url'])
    mylist2 = list(zip(title2, desc2, img2, readmore2))
    top_entertainment = newsapi.get_top_headlines(country="in", category="entertainment")
    json3 = top_entertainment['articles']
    desc3 = []
    img3 = []
    title3 = []
    mylist3 = []
    readmore3 = []
    for i in range(len(json3)):
        desc3.append(json3[i]['description'])
        title3.append(json3[i]['title'])
        img3.append(json3[i]['urlToImage'])
        readmore3.append(json3[i]['url'])
    mylist3 = list(zip(title3, desc3, img3, readmore3))
    top_health = newsapi.get_top_headlines(country="in", category="health")
    json4 = top_health['articles']
    desc4 = []
    img4 = []
    title4 = []
    mylist4 = []
    readmore4 = []
    for i in range(len(json4)):
        desc4.append(json4[i]['description'])
        title4.append(json4[i]['title'])
        img4.append(json4[i]['urlToImage'])
        readmore4.append(json4[i]['url'])
    mylist4 = list(zip(title4, desc4, img4, readmore4))
    top_science = newsapi.get_top_headlines(country="in", category="science")
    json5 = top_science['articles']
    desc5 = []
    img5 = []
    title5 = []
    mylist5 = []
    readmore5 = []
    for i in range(len(json5)):
        desc5.append(json5[i]['description'])
        title5.append(json5[i]['title'])
        img5.append(json5[i]['urlToImage'])
        readmore5.append(json5[i]['url'])
    mylist5 = list(zip(title5, desc5, img5, readmore5))
    top_technology = newsapi.get_top_headlines(country="in", category="technology")
    json6 = top_technology['articles']
    desc6 = []
    img6 = []
    title6 = []
    mylist6 = []
    readmore6 = []
    for i in range(len(json6)):
        desc6.append(json6[i]['description'])
        title6.append(json6[i]['title'])
        img6.append(json6[i]['urlToImage'])
        readmore6.append(json6[i]['url'])
    mylist6 = list(zip(title6, desc6, img6, readmore6))
    return render(request,"index.html",{'row':mylist,'row1':mylist[:4],'business':mylist1,'sports':mylist2,'entertainment':mylist3,'health':mylist4,'science':mylist4,'technology':mylist4})

def business(request):
    newsapi = NewsApiClient(api_key='bb456701776c49a383d06ff36aceb6c8')
    top=  newsapi.get_top_headlines(country="in",category="business")
    json=top['articles']
    desc=[]
    img=[]
    title=[]
    mylist=[]
    readmore=[]
    description=[]
    for i in range(len(json)):
        desc.append(json[i]['description'])
        title.append(json[i]['title'])
        img.append(json[i]['urlToImage'])
        readmore.append(json[i]['url'])
        description.append(json[i]["description"])
    mylist=list(zip(title,desc,img,readmore,description))
    top_business = newsapi.get_top_headlines(category="business")
    json6 = top_business['articles']
    desc6 = []
    img6 = []
    title6 = []
    mylist6 = []
    readmore6 = []
    for i in range(len(json6)):
        desc6.append(json6[i]['description'])
        title6.append(json6[i]['title'])
        img6.append(json6[i]['urlToImage'])
        readmore6.append(json6[i]['url'])
    mylist6 = list(zip(title6, desc6, img6, readmore6))
    top_corporate = newsapi.get_top_headlines(q="corporate", category="business")
    json5 = top_corporate['articles']
    desc5 = []
    img5 = []
    title5 = []
    mylist5 = []
    readmore5 = []
    for i in range(len(json5)):
        desc5.append(json5[i]['description'])
        title5.append(json5[i]['title'])
        img5.append(json5[i]['urlToImage'])
        readmore5.append(json5[i]['url'])
    mylist5 = list(zip(title5, desc5, img5, readmore5))
    top_economy = newsapi.get_top_headlines(q="economy",category="business")
    json4 = top_economy['articles']
    desc4 = []
    img4 = []
    title4 = []
    mylist4 = []
    readmore4 = []
    for i in range(len(json4)):
        desc4.append(json4[i]['description'])
        title4.append(json4[i]['title'])
        img4.append(json4[i]['urlToImage'])
        readmore4.append(json4[i]['url'])
    mylist4 = list(zip(title4, desc4, img4, readmore4))
    top_startups = newsapi.get_top_headlines(q="startup", category="business")
    json2 = top_startups['articles']
    desc2 = []
    img2 = []
    title2 = []
    mylist2 = []
    readmore2 = []
    for i in range(len(json2)):
        desc2.append(json2[i]['description'])
        title2.append(json2[i]['title'])
        img2.append(json2[i]['urlToImage'])
        readmore2.append(json2[i]['url'])
    mylist2 = list(zip(title2, desc2, img2, readmore2))
    return render(request,"Business.html",{'row':mylist[:1],'business':mylist,'business1':mylist[1:8],'interbusi':mylist6,'corporate':mylist5[:6],'economy':mylist4[:5],'startups':mylist2[:5]})

def entertainment(request):
    newsapi = NewsApiClient(api_key='bb456701776c49a383d06ff36aceb6c8')
    top=  newsapi.get_top_headlines(country="in",category="entertainment")
    json=top['articles']
    desc=[]
    img=[]
    title=[]
    mylist=[]
    readmore=[]
    description=[]
    for i in range(len(json)):
        desc.append(json[i]['description'])
        title.append(json[i]['title'])
        img.append(json[i]['urlToImage'])
        readmore.append(json[i]['url'])
        description.append(json[i]["description"])
    mylist=list(zip(title,desc,img,readmore,description))
    top_business = newsapi.get_top_headlines(category="entertainment")
    json6 = top_business['articles']
    desc6 = []
    img6 = []
    title6 = []
    mylist6 = []
    readmore6 = []
    for i in range(len(json6)):
        desc6.append(json6[i]['description'])
        title6.append(json6[i]['title'])
        img6.append(json6[i]['urlToImage'])
        readmore6.append(json6[i]['url'])
    mylist6 = list(zip(title6, desc6, img6, readmore6))
    top_corporate = newsapi.get_top_headlines(q="movie", category="entertainment")
    json5 = top_corporate['articles']
    desc5 = []
    img5 = []
    title5 = []
    mylist5 = []
    readmore5 = []
    for i in range(len(json5)):
        desc5.append(json5[i]['description'])
        title5.append(json5[i]['title'])
        img5.append(json5[i]['urlToImage'])
        readmore5.append(json5[i]['url'])
    mylist5 = list(zip(title5, desc5, img5, readmore5))
    top_economy = newsapi.get_top_headlines(q="television",category="entertainment")
    json4 = top_economy['articles']
    desc4 = []
    img4 = []
    title4 = []
    mylist4 = []
    readmore4 = []
    for i in range(len(json4)):
        desc4.append(json4[i]['description'])
        title4.append(json4[i]['title'])
        img4.append(json4[i]['urlToImage'])
        readmore4.append(json4[i]['url'])
    mylist4 = list(zip(title4, desc4, img4, readmore4))
    top_startups = newsapi.get_top_headlines(q="fashion", category="entertainment")
    json2 = top_startups['articles']
    desc2 = []
    img2 = []
    title2 = []
    mylist2 = []
    readmore2 = []
    for i in range(len(json2)):
        desc2.append(json2[i]['description'])
        title2.append(json2[i]['title'])
        img2.append(json2[i]['urlToImage'])
        readmore2.append(json2[i]['url'])
    mylist2 = list(zip(title2, desc2, img2, readmore2))
    return render(request,"Entertaiment.html",{'row':mylist[:1],'business':mylist,'business1':mylist[1:8],'interbusi':mylist6,'corporate':mylist5[:6],'economy':mylist4[:5],'startups':mylist2[:5]})


def health(request):
    newsapi = NewsApiClient(api_key='bb456701776c49a383d06ff36aceb6c8')
    top=  newsapi.get_top_headlines(country="in",category="health")
    json=top['articles']
    desc=[]
    img=[]
    title=[]
    mylist=[]
    readmore=[]
    description=[]
    for i in range(len(json)):
        desc.append(json[i]['description'])
        title.append(json[i]['title'])
        img.append(json[i]['urlToImage'])
        readmore.append(json[i]['url'])
        description.append(json[i]["description"])
    mylist=list(zip(title,desc,img,readmore,description))
    top_business = newsapi.get_top_headlines(category="health")
    json6 = top_business['articles']
    desc6 = []
    img6 = []
    title6 = []
    mylist6 = []
    readmore6 = []
    for i in range(len(json6)):
        desc6.append(json6[i]['description'])
        title6.append(json6[i]['title'])
        img6.append(json6[i]['urlToImage'])
        readmore6.append(json6[i]['url'])
    mylist6 = list(zip(title6, desc6, img6, readmore6))
    top_corporate = newsapi.get_top_headlines(q="corona", category="health")
    json5 = top_corporate['articles']
    desc5 = []
    img5 = []
    title5 = []
    mylist5 = []
    readmore5 = []
    for i in range(len(json5)):
        desc5.append(json5[i]['description'])
        title5.append(json5[i]['title'])
        img5.append(json5[i]['urlToImage'])
        readmore5.append(json5[i]['url'])
    mylist5 = list(zip(title5, desc5, img5, readmore5))
    top_economy = newsapi.get_top_headlines(q="disease",category="health")
    json4 = top_economy['articles']
    desc4 = []
    img4 = []
    title4 = []
    mylist4 = []
    readmore4 = []
    for i in range(len(json4)):
        desc4.append(json4[i]['description'])
        title4.append(json4[i]['title'])
        img4.append(json4[i]['urlToImage'])
        readmore4.append(json4[i]['url'])
    mylist4 = list(zip(title4, desc4, img4, readmore4))
    top_startups = newsapi.get_top_headlines(q="diabetes", category="health")
    json2 = top_startups['articles']
    desc2 = []
    img2 = []
    title2 = []
    mylist2 = []
    readmore2 = []
    for i in range(len(json2)):
        desc2.append(json2[i]['description'])
        title2.append(json2[i]['title'])
        img2.append(json2[i]['urlToImage'])
        readmore2.append(json2[i]['url'])
    mylist2 = list(zip(title2, desc2, img2, readmore2))
    return render(request,"Health.html",{'row':mylist[:1],'business':mylist,'business1':mylist[1:8],'interbusi':mylist6,'corporate':mylist5[:6],'economy':mylist4[:5],'startups':mylist2[:5]})


def science(request):
    newsapi = NewsApiClient(api_key='bb456701776c49a383d06ff36aceb6c8')
    top=  newsapi.get_top_headlines(country="in",category="science")
    json=top['articles']
    desc=[]
    img=[]
    title=[]
    mylist=[]
    readmore=[]
    description=[]
    for i in range(len(json)):
        desc.append(json[i]['description'])
        title.append(json[i]['title'])
        img.append(json[i]['urlToImage'])
        readmore.append(json[i]['url'])
        description.append(json[i]["description"])
    mylist=list(zip(title,desc,img,readmore,description))
    top_business = newsapi.get_top_headlines(category="science")
    json6 = top_business['articles']
    desc6 = []
    img6 = []
    title6 = []
    mylist6 = []
    readmore6 = []
    for i in range(len(json6)):
        desc6.append(json6[i]['description'])
        title6.append(json6[i]['title'])
        img6.append(json6[i]['urlToImage'])
        readmore6.append(json6[i]['url'])
    mylist6 = list(zip(title6, desc6, img6, readmore6))
    top_corporate = newsapi.get_top_headlines(q="space", category="science")
    json5 = top_corporate['articles']
    desc5 = []
    img5 = []
    title5 = []
    mylist5 = []
    readmore5 = []
    for i in range(len(json5)):
        desc5.append(json5[i]['description'])
        title5.append(json5[i]['title'])
        img5.append(json5[i]['urlToImage'])
        readmore5.append(json5[i]['url'])
    mylist5 = list(zip(title5, desc5, img5, readmore5))
    top_economy = newsapi.get_top_headlines(q="earth",category="science")
    json4 = top_economy['articles']
    desc4 = []
    img4 = []
    title4 = []
    mylist4 = []
    readmore4 = []
    for i in range(len(json4)):
        desc4.append(json4[i]['description'])
        title4.append(json4[i]['title'])
        img4.append(json4[i]['urlToImage'])
        readmore4.append(json4[i]['url'])
    mylist4 = list(zip(title4, desc4, img4, readmore4))
    top_startups = newsapi.get_top_headlines(q="humans", category="science")
    json2 = top_startups['articles']
    desc2 = []
    img2 = []
    title2 = []
    mylist2 = []
    readmore2 = []
    for i in range(len(json2)):
        desc2.append(json2[i]['description'])
        title2.append(json2[i]['title'])
        img2.append(json2[i]['urlToImage'])
        readmore2.append(json2[i]['url'])
    mylist2 = list(zip(title2, desc2, img2, readmore2))
    return render(request,"Science.html",{'row':mylist[:1],'business':mylist,'business1':mylist[1:8],'interbusi':mylist6,'corporate':mylist5[:6],'economy':mylist4[:5],'startups':mylist2[:5]})



def sports(request):
    newsapi = NewsApiClient(api_key='680381b7da6f46a8833923dbc433f2c8')
    top=  newsapi.get_top_headlines(country="in",category="sports")
    json=top['articles']
    desc=[]
    img=[]
    title=[]
    mylist=[]
    readmore=[]
    description=[]
    for i in range(len(json)):
        desc.append(json[i]['description'])
        title.append(json[i]['title'])
        img.append(json[i]['urlToImage'])
        readmore.append(json[i]['url'])
        description.append(json[i]["description"])
    mylist=list(zip(title,desc,img,readmore,description))
    top_business = newsapi.get_top_headlines(category="sports")
    json6 = top_business['articles']
    desc6 = []
    img6 = []
    title6 = []
    mylist6 = []
    readmore6 = []
    for i in range(len(json6)):
        desc6.append(json6[i]['description'])
        title6.append(json6[i]['title'])
        img6.append(json6[i]['urlToImage'])
        readmore6.append(json6[i]['url'])
    mylist6 = list(zip(title6, desc6, img6, readmore6))
    top_corporate = newsapi.get_top_headlines(q="cricket", category="sports")
    json5 = top_corporate['articles']
    desc5 = []
    img5 = []
    title5 = []
    mylist5 = []
    readmore5 = []
    for i in range(len(json5)):
        desc5.append(json5[i]['description'])
        title5.append(json5[i]['title'])
        img5.append(json5[i]['urlToImage'])
        readmore5.append(json5[i]['url'])
    mylist5 = list(zip(title5, desc5, img5, readmore5))
    top_economy = newsapi.get_top_headlines(q="football",category="sports")
    json4 = top_economy['articles']
    desc4 = []
    img4 = []
    title4 = []
    mylist4 = []
    readmore4 = []
    for i in range(len(json4)):
        desc4.append(json4[i]['description'])
        title4.append(json4[i]['title'])
        img4.append(json4[i]['urlToImage'])
        readmore4.append(json4[i]['url'])
    mylist4 = list(zip(title4, desc4, img4, readmore4))
    top_startups = newsapi.get_top_headlines(q="hockey", category="sports")
    json2 = top_startups['articles']
    desc2 = []
    img2 = []
    title2 = []
    mylist2 = []
    readmore2 = []
    for i in range(len(json2)):
        desc2.append(json2[i]['description'])
        title2.append(json2[i]['title'])
        img2.append(json2[i]['urlToImage'])
        readmore2.append(json2[i]['url'])
    mylist2 = list(zip(title2, desc2, img2, readmore2))
    return render(request,"Sports.html",{'row':mylist[:1],'business':mylist,'business1':mylist[1:8],'interbusi':mylist6,'corporate':mylist5[:6],'economy':mylist4[:5],'startups':mylist2[:5]})

def technology(request):
    newsapi = NewsApiClient(api_key='680381b7da6f46a8833923dbc433f2c8')
    top=  newsapi.get_top_headlines(country="in",category="technology")
    json=top['articles']
    desc=[]
    img=[]
    title=[]
    mylist=[]
    readmore=[]
    description=[]
    for i in range(len(json)):
        desc.append(json[i]['description'])
        title.append(json[i]['title'])
        img.append(json[i]['urlToImage'])
        readmore.append(json[i]['url'])
        description.append(json[i]["description"])
    mylist=list(zip(title,desc,img,readmore,description))
    top_business = newsapi.get_top_headlines(category="technology")
    json6 = top_business['articles']
    desc6 = []
    img6 = []
    title6 = []
    mylist6 = []
    readmore6 = []
    for i in range(len(json6)):
        desc6.append(json6[i]['description'])
        title6.append(json6[i]['title'])
        img6.append(json6[i]['urlToImage'])
        readmore6.append(json6[i]['url'])
    mylist6 = list(zip(title6, desc6, img6, readmore6))
    top_corporate = newsapi.get_top_headlines(q="brand", category="technology")
    json5 = top_corporate['articles']
    desc5 = []
    img5 = []
    title5 = []
    mylist5 = []
    readmore5 = []
    for i in range(len(json5)):
        desc5.append(json5[i]['description'])
        title5.append(json5[i]['title'])
        img5.append(json5[i]['urlToImage'])
        readmore5.append(json5[i]['url'])
    mylist5 = list(zip(title5, desc5, img5, readmore5))
    top_economy = newsapi.get_top_headlines(q="mobiles",category="technology")
    json4 = top_economy['articles']
    desc4 = []
    img4 = []
    title4 = []
    mylist4 = []
    readmore4 = []
    for i in range(len(json4)):
        desc4.append(json4[i]['description'])
        title4.append(json4[i]['title'])
        img4.append(json4[i]['urlToImage'])
        readmore4.append(json4[i]['url'])
    mylist4 = list(zip(title4, desc4, img4, readmore4))
    top_startups = newsapi.get_top_headlines(q="products", category="technology")
    json2 = top_startups['articles']
    desc2 = []
    img2 = []
    title2 = []
    mylist2 = []
    readmore2 = []
    for i in range(len(json2)):
        desc2.append(json2[i]['description'])
        title2.append(json2[i]['title'])
        img2.append(json2[i]['urlToImage'])
        readmore2.append(json2[i]['url'])
    mylist2 = list(zip(title2, desc2, img2, readmore2))
    return render(request,"Technology.html",{'row':mylist[:1],'business':mylist,'business1':mylist[1:8],'interbusi':mylist6,'corporate':mylist5[:6],'economy':mylist4[:5],'startups':mylist2[:5]})








def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) < 5:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('home')


        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Successfully Registered")
        return redirect('home')
    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        print(loginusername," ",loginpassword)
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

def contact(request):
    return render(request,"contact.html")

def myfeed(request):
    return render(request,"MyFeed.html",{"check":""})

def myfeedreply(request):
    d={"India":"in","United States":"us","Russia":"ru","China":"cn","United Kingdom":"gb"}
    if request.method=="POST":
        country=request.POST["country"]
        category=request.POST["category"]
        newsapi = NewsApiClient(api_key='680381b7da6f46a8833923dbc433f2c8')
        top=  newsapi.get_top_headlines(country=d[country],category=category)
        json=top['articles']
        desc=[]
        img=[]
        title=[]
        mylist=[]
        readmore=[]
        for i in range(len(json)):
            desc.append(json[i]['description'])
            title.append(json[i]['title'])
            img.append(json[i]['urlToImage'])
            readmore.append(json[i]['url'])
        mylist=list(zip(title,desc,img,readmore))
        print(mylist)
        return render(request,"MyFeed.html",{"check":"Yes","myfeed":mylist})
    
def prompt(request):
    messages.success(request, "Please Log in to view full content")
    return redirect('home')


def display(request):
    user_bookmark = Bookmark.objects.filter(user_id=request.user.id)
    return render(request,"Display.html",{"user_bookmark":user_bookmark})


def SaveBookmark(request):
    if request.method=="POST":
        img=request.POST["image"]
        title=request.POST["title"]
        user=request.user.id
        bmrk=Bookmark(title=title,image=img,user_id=user)
        bmrk.save()
        messages.success(request, "Your bookmark has been added successfully") 
        return redirect('home')


def deletebookmark(request):
    if request.method=="POST":
        no=request.POST["sno"]
        Bookmark.objects.filter(sno=no).delete()
        messages.success(request, "Your bookmark has been deleted successfully") 
        user_bookmark = Bookmark.objects.filter(user_id=request.user.id)
        return render(request,"Display.html",{"user_bookmark":user_bookmark})
