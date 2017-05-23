import numpy as np
from ligtfm.datasets import fetch_movielens
from lightfm import LightFM

#fetch data & format it
data = fetch_movielens(min_rating=4.0)

print(repr(data['train']))
print(repr(data['test']))

model = LightFM(loss='warp')
model.fit(data['train'],epochs=30,num_threads=2)

def sample_recommendation(model,data,user_ids):
    n_users, n_items = data['train'].shape

    # gen reco for each user we input
    for user_id in user_ids:
        known_postitves = data['item_labels'][data['train'].tocsr()[user_id].indices]

        # movies our model predicts they like
        scores = model.predict(user_id,np.arange(n_items))
        # rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        print("User %s" % user_id)
        print("         Known Postitves : ")

        for x in known_postitves[:3]:
            print("         %s" % x)
        
        print("         Recommended : ")

        for x in top_items[:3]
            print("         %s" % x)


sample_recommendation(model,data,[3,25,450])