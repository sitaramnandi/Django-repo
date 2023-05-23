from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,"BBC_TESTAPP/index.html")
def movie_info(request):
    head_msg="Movie_information"
    sub_msg1="Yesterday DASAR was released"
    sub_msg2="Planning for Aashiui-3 with Mashesh Sir & Sunny"
    sub_msg3="Do not Go for Movive..... Pratics Django...."
    type = "movies"
    my_dict={"head_msg":head_msg,"sub_msg1":sub_msg1,"sub_msg2":sub_msg2,"sub_msg3":sub_msg3,"type":type}
    return render(request,"BBC_TESTAPP/news.html",context=my_dict)
def sport_info(request):
    head_msg="Sport Information"
    sub_msg1="IPL Was Started"
    sub_msg2="Hockey Is One of the famous Game"
    sub_msg3="Cricket is Most Popular Game "
    type="sports"
    my_dict={"head_msg":head_msg,"sub_msg1":sub_msg1,"sub_msg2":sub_msg2,"sub_msg3":sub_msg3,"type":type}
    return render(request,"BBC_TESTAPP/news.html",context=my_dict)
def poltics_info(request):
    head_msg="Politics Information"
    sub_msg1="India Prime Minister Is Nendera Modi"
    sub_msg2="April Buget Is Reled"
    sub_msg3="Odisha CM is Nabin Patanik "
    type="politics"
    my_dict={"head_msg":head_msg,"sub_msg1":sub_msg1,"sub_msg2":sub_msg2,"sub_msg3":sub_msg3,"type":type}
    return render(request,"BBC_TESTAPP/news.html",my_dict)
