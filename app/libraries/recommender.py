import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

def rate_product(df, product_list):
    rate = {}
    row_indexes = {}
    for i, _ in df.iterrows():
        selected_product = df.loc[i][df.loc[i].notna()].index.tolist()
        rate[i] = selected_product
        row_indexes[i] = [product_list.index(x) for x in selected_product]

    return {
        "rate": rate,
        "row_indexes": row_indexes
    }

def nearest_neighbors(df, n=5):
    cosine_nn=NearestNeighbors(n_neighbors=n, algorithm='brute', metric='cosine')
    item_cosine_nn_fit=cosine_nn.fit(df.T.values)
    item_distances,item_indices=item_cosine_nn_fit.kneighbors(df.T.values)
    return item_distances,item_indices


def generate_recommendation(item_indices, item_distances, row_indexes, product_list):
    topRecs = {}
    for k,v in row_indexes.items(): # k - user id, v - product id
        item_idx= item_indices[v].flatten()
        item_dist= item_distances[v].flatten()

        combine=list(zip(item_dist,item_idx))
        diction={i:d for d,i in combine if i not in v}
        sort = sorted(diction.items(), key=lambda x: x[1])
        
        recommendations=[(product_list[i],d)for i,d in sort]
        topRecs[k]=recommendations
    
    return topRecs


# ratings = pd.read_csv('data/ratings1.csv',sep=';')
produk = pd.read_csv('data/bodycares.csv',sep=';')

def get_recommendation(user_id, data, n=5):
    ratings = pd.DataFrame(data)
    product_list = produk["Item"].unique().tolist()
    df = pd.merge(ratings, produk, on="itemId", how="inner")
    product_list = [i for i in product_list if i in df["Item"].unique().tolist()]
    
    pivot_table = df.pivot_table(values='rating',index='userId',columns='Item')
    pivot_table = pivot_table[product_list]

    data = rate_product(pivot_table, product_list)
    row_indexes = data["row_indexes"]
    rate = data["rate"]

    pivot_table = pivot_table.fillna(0)
    pivot_table.apply(np.sign)

    item_distances,item_indices = nearest_neighbors(pivot_table, n)
    top_recs = generate_recommendation(item_indices, item_distances, row_indexes, product_list)

    if user_id not in pivot_table.index:
        return "Out of range, user not registered!"
    else:
        last_viewed = rate[user_id]
        recs = [{'produk': i[0], 'similarity': 1-i[1]} for i in  top_recs[user_id][:n]]   
        col_recs = ["produk", "similarity"]
        return last_viewed, recs, col_recs


