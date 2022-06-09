from django.shortcuts import render

# 폴더 위치
def home_view(request):
    return render(request, "HomePage.html") # 첫화면 홈페이지

def login_view(request):
    return render(request, "Log_inPage.html") # 로그인 페이지

def Mypage_view(request):
    return render(request, "Mypage.html") # 마이 페이지

def Sign_upPage_view(request):
    return render(request, "Sign_upPage.html") # 가입 페이지

def Recommand_selectPage_view(request):
    return render(request, "Recommand_selectPage.html") # 설문조사 페이지

def bcommunity_view(request):
    return render(request, "bcommunity.html") # 커뮤니티 페이지

def bcommunitydetail_view(request):
    return render(request, "bcommunitydetail.html") # 커뮤니티 상세 페이지

def bcommunityinsertform_view(request):
    return render(request, "bcommunityinsertform.html") # 커뮤니티 작성 페이지

def bcourse_view(request):
    return render(request, "bcourse.html") # 그냥 여행 페이지

def bfavorites_view(request): 
    return render(request, "bfavorites.html") # 그냥 여행 페이지

def btourlistspot_view(request):
    return render(request, "btourlistspot.html") # 그냥 여행 페이지

def btourlistspotdetail_view(request):
    return render(request, "btourlistspotdetail.html") # 부산시 관광 명소

def Recommand_resultPage_view(request):
    return render(request, "Recommand_resultPage.html") # 선택한 정보에 따른 추천 여행지입니다



