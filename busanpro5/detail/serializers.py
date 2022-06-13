# json 바뀌줌
# from .models import detail
# from users.serializers import UserSerializer
# from rest_framework import serializers

# class detailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = detail
#         fields = [
#             "Place", # 장소
#             "Theme", # 테마
#             "Address", # 주소
#             "Explanation", # 설명
#             "Image_2", # 이미지2
#         ]

#     author_name = serializers.SerializerMethodField("get_authors_name") # 직렬변환기

#     def get_authors_name(self, obj):
#         return obj.Place