import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .models import RecommendModel

def recommed(theme,gr_list, age_list):
    item = RecommendModel.objects.values('location','theme','score','group','age',)
    data = pd.DataFrame(item)
    data['theme'] = data['theme'].str.replace(',', ' ')
    data['location'] = data['location'].str.replace(' ', '') 
    data['group'] = data['group'].str.replace(',', ' ')
    data['age'] = data['age'].str.replace(',', ' ')
    

    count_vector = CountVectorizer(ngram_range=(1, 3))
    c_vector_theme = count_vector.fit_transform(data['theme'].values.astype('U'))
    theme_c_sim = cosine_similarity(c_vector_theme, c_vector_theme).argsort()[:,::-1]
    
    def get_recommend_traval_list(df, traval_list, top=60):
        target_traval_index = df[df['location'] == traval_list].index.values
        sin_index = theme_c_sim[target_traval_index,:top].reshape(-1)
        sin_index = sin_index[sin_index != target_traval_index]
        result = data.iloc[sin_index].sort_values('score', ascending=False)#[:4]
        return result
 
    location = data.query('theme.str.contains("{}")'.format(theme), engine='python')

    loc_sam = location.sample(n=1, replace=True, axis=0)
    loc_sam = loc_sam.iloc[0, 0]

    recommend = get_recommend_traval_list(data, loc_sam).reset_index(drop=True)

    count_vector2 = CountVectorizer(ngram_range=(1, 3))
    c_vector_theme2 = count_vector2.fit_transform(recommend['group'].values.astype('U'))
    
    theme_c_sim2 = cosine_similarity(c_vector_theme2, c_vector_theme2).argsort()[:,::-1]
    
    def get_recommend_traval_list2(df2, traval_list2, top=30):
        target_traval_index2 = df2[df2['location'] == traval_list2].index.values
        sin_index2 = theme_c_sim2[target_traval_index2,:top].reshape(-1)

        sin_index2 = sin_index2[sin_index2 != target_traval_index2]

        result2 = recommend.iloc[sin_index2].sort_values('score', ascending=False)  # [:4]


        return result2
    
    location2 = recommend.query('group.str.contains("{}")'.format(gr_list), engine='python')
    
    loc_sam2 = location2.sample(n=1, replace=True, axis=0)
    loc_sam2 = loc_sam2.iloc[0, 0]

    recommend2 = get_recommend_traval_list2(recommend, loc_sam2).reset_index(drop=True)
   
    # 모델3
    count_vector3 = CountVectorizer(ngram_range=(1, 3))
    c_vector_theme3 = count_vector3.fit_transform(recommend2['age'].values.astype('U'))
    
    theme_c_sim3 = cosine_similarity(c_vector_theme3, c_vector_theme3).argsort()[:,::-1]
    
    def get_recommend_traval_list3(df3, traval_list3, top=4):
        target_traval_index3 = df3[df3['location'] == traval_list3].index.values
        sin_index3 = theme_c_sim3[target_traval_index3,:top].reshape(-1)
        sin_index3 = sin_index3[sin_index3 != target_traval_index3]
        result3 = recommend2.iloc[sin_index3].sort_values('score', ascending=False)  # [:4]
        # score는 정렬을 위한 것
        return result3
  
    location3 = recommend2.query('age.str.contains("{}")'.format(age_list), engine='python')

    loc_sam3 = location3.sample(n=1, replace=True, axis=0)
    loc_sam3 = loc_sam3.iloc[0, 0]

    recommend3 = get_recommend_traval_list3(recommend2, loc_sam3).iloc[0:3,0]
    
    return recommend3
