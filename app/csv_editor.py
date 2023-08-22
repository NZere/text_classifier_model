import pandas as pd

import csv


with open('parsing_files/bank_indecies.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    data_temp = list(reader)

print(data_temp)

data_ind = []
for i in data_temp:
    if i[0] == 'index':
        continue
    data_ind.append(i[0])

print(data_ind)

d_frame_old = pd.read_csv(r'parsing_files/1C_banking_comments.csv')
# print(d_frame_old.head())
#
texts_old = d_frame_old["comment_text"]
indexes_old = d_frame_old["comment_type"]
#
#
print(indexes_old)
print(texts_old)

# data_old = {
#     "index": indexes_old,
#     "comment": texts_old
# }

d_frame = pd.read_csv(r'parsing_files/all_prod_query_results-2023-08-18_64255.csv', quotechar='"', quoting=csv.QUOTE_ALL)


# print(d_frame.head())
# print(d_frame["comment"])
# print(d_frame.loc[:, "comment"])
indecies = []
texts = []
for item in d_frame["comment"]:
    index = item.split(" ")[0]
    if index in ["2КОНВ1", "1КОНВ1"]:
        print(index[:-1])
        indecies.append(index[:-1])
    else:
        indecies.append(index)
    texts.append(" ".join(item.split(" ")[1:]))

# print(indexes)
# print(texts)

data = {
    "ids": [i for i in range(len(indecies))],
    "comment_type": indecies,
    "comment_text": texts
}
new_df = pd.DataFrame(data)


concat_df = pd.concat([d_frame_old, new_df], ignore_index=True)


print(concat_df)
print("++++++++++++++++++++++++++++++++++++++++++")
for i, value in enumerate(concat_df["comment_type"]):
    print(i, value)
print("++++++++++++++++++++++++++++++++++++++++++")
# print(new_df)
old_data_ind = []
current_data_ind = []

print("***************************************************")

for i in concat_df.index:
    print(i, concat_df.iloc[i, 1], concat_df.iloc[i, 2])
print("****************************************************")
for ind in range(len(concat_df)):
    index = str(concat_df.iloc[ind, 1]).strip().upper()
    if index == "1Н1" or index == "1H1" or index == "1H1":
        concat_df.iloc[ind, 1] = "1С"
    if index == "1C" or index == "1С":
        concat_df.iloc[ind, 1] = "1Н1"
    if index == "1H2" or index == "1Н2" or index == "1H2":
        concat_df.iloc[ind, 1] = "1Н2"
    if index == "1K1" or index == "1К1":
        concat_df.iloc[ind, 1] = "1К1"
    if index == "2P1" or index == "2Р1":
        concat_df.iloc[ind, 1] = "2Р1"
    if index == "1P" or index == "1Р":
        concat_df.iloc[ind, 1] = "1Р"
    if index == "1Ч":
        concat_df.iloc[ind, 1] = "1ПР"
    if index == "1G1":
        concat_df.iloc[ind, 1] = "1П1"
    if index == "1G2":
        concat_df.iloc[ind, 1] = "1П2"
    if index == "2ВЭД2" or index == "2ВЭД1" or index == "2ВЭД3":
        concat_df.iloc[ind, 1] = "2ВЭД"
    if index == "1ВЭД2" or index == "1ВЭД1" or index == "1ВЭД3":
        concat_df.iloc[ind, 1] = "1ВЭД"
    if index == "2КОНВ1":
        concat_df.iloc[ind, 1] = "2КОНВ"
    if index == "1КОНВ1":
        concat_df.iloc[ind, 1] = "1КОНВ"
    if index == "2GJC":
        concat_df.iloc[ind, 1] = "2ПОС"
    if index == "1G/J":
        concat_df.iloc[ind, 1] = "1П/О"
    if index == "1C":
        concat_df.iloc[ind, 1] = "1С"
    index = str(concat_df.iloc[ind, 1]).strip().upper()
    if index not in data_ind:
        # print(concat_df.iloc[ind, 1])
        old_data_ind.append(ind)
        continue
    else:
        current_data_ind.append(ind)
print("old_data_ind")
print(len(old_data_ind))
print(old_data_ind)

print("current_data_ind")
print(len(current_data_ind))
print(current_data_ind)

old_df = concat_df[concat_df.index.isin(old_data_ind)]
for i in old_df.index:
    print(i, concat_df.iloc[i, 1])
print("================================")
final_df = concat_df[concat_df.index.isin(current_data_ind)]
for i in final_df.index:
    print(i, concat_df.iloc[i, 1])

# for i in final_df.comment_type:
#     print(i)

final_df.to_csv('result_dataset.csv', index=False)

