import pandas as pd

PRODUK = pd.read_csv('data/bodycares.csv',sep=';')
RATINGS = pd.read_csv('data/ratings1.csv',sep=';')

def is_active(user_id, item_id, data):
    df = pd.DataFrame(data)
    used_produk = df[df['userId'] == user_id]
    if item_id in used_produk["itemId"]:
        return False
    else:
        return True

def active_data(user_id, data):
    df = pd.DataFrame(data)
    used_produk = df[df["userId"] == user_id]
    if used_produk.shape[0] != 0:
        produk_list = PRODUK["itemId"].tolist()
        active_produk = [i for i in produk_list if i not in used_produk["itemId"].tolist()]
        products = PRODUK.copy()
        products.index = products["itemId"]
        available_produk = products.loc[active_produk].to_dict("records")

        del products
        del produk_list
        del used_produk
        del active_produk
    else:
        available_produk = PRODUK.to_dict("records")

    return available_produk

# def add_data(user_id, item_id, rating):
#     if is_active(user_id, item_id):
#         new_data = pd.DataFrame({
#             "userId":user_id,
#             "itemId": item_id,
#             "rating": rating
#         })

#         rate = RATINGS.append(new_data, ignore_index=True)
#         rate.to_csv("data/ratings.csv", index=False, sep=";")


def dump_data():
    return RATINGS.to_dict("records")




