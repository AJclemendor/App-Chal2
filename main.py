import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


pd.options.display.max_columns = 60
pd.options.display.max_colwidth = 50


#businesses_large = pd.read_json('yelp_academic_dataset_business.json', lines=True)

#checkins_large = pd.read_json('yelp_academic_dataset_checkin.json', lines=True)

#reviews_large = pd.read_json('yelp_academic_dataset_review.json', lines=True)

#tips_large = pd.read_json('yelp_academic_dataset_tip.json', lines=True)

#users_large = pd.read_json('yelp_academic_dataset_user.json', lines=True)

businesses = pd.read_json('yelp_business.json', lines=True)
reviews = pd.read_json('yelp_review.json', lines=True)
users = pd.read_json('yelp_user.json', lines=True)
checkins = pd.read_json('yelp_checkin.json', lines=True)
tips = pd.read_json('yelp_tip.json', lines=True)
photos = pd.read_json('yelp_photo.json', lines=True)

print(businesses.head())


total_merge_data = pd.merge(businesses, reviews, how='left', on='business_id')
total_merge_data = pd.merge(total_merge_data, users, how='left', on='business_id')
total_merge_data = pd.merge(total_merge_data, checkins, how='left', on='business_id')
total_merge_data = pd.merge(total_merge_data, tips, how='left', on='business_id')
total_merge_data = pd.merge(total_merge_data, photos, how='left', on='business_id')

print(total_merge_data.columns)

# features_to_remove = ['address','attributes','business_id','categories','city','hours','is_open','latitude','longitude','name','neighborhood','postal_code','state','time']
# total_merge_data.drop(labels=features_to_remove, axis=1, inplace=True)

print(total_merge_data.isna().any())

total_merge_data.fillna({'weekday_checkins':0,
           'weekend_checkins':0,
           'average_tip_length':0,
           'number_tips':0,
           'average_caption_length':0,
           'number_pics':0},
          inplace=True)

print(total_merge_data.isna().any())
