from django.urls import path
from .import views

urlpatterns = [ # 웹페이지 위치
    path("", views.home_view),  # 첫화면 홈페이지
    path("login", views.login_view), # 로그인 페이지
    path("Mypage", views.Mypage_view), # 마이 페이지
    path("Sign_upPage", views.Sign_upPage_view), # 가입 페이지
    path("Recommand_selectPage", views.Recommand_selectPage_view), # 설문조사 페이지

    # path("bcommunity", views.bcommunity_view), # 커뮤니티 페이지
    # path("bcommunitydetail", views.bcommunitydetail_view), # 커뮤니티 상세 페이지
    # path("bcommunityinsertform", views.bcommunityinsertform_view), # 커뮤니티 작성 페이지

    path("bcourse", views.bcourse_view), # 그냥 여행 페이지
    path("bfavorites", views.bfavorites_view), # 그냥 여행 페이지
    path("btourlistspot", views.btourlistspot_view), # 그냥 여행 페이지

    path("btourlistspotdetail", views.btourlistspotdetail_view), # 부산시 관광 명소
    path("Recommand_resultPage", views.Recommand_resultPage_view), # 선택한 정보에 따른 추천 여행지입니다
    
    
]