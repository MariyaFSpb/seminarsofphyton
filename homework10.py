# Задача
# В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести
# его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head()

def one_hot(row):
    if row['whoAmI'] == 'robot':
        row['robot'] = 1
        row['human'] = 0
    else:
        row['human'] = 1
        row['robot'] = 0
    return row

data = data.assign(whoAmI=lst).apply(one_hot, axis=1)
data.head()

data.corr()

import seaborn as sns
sns.heatmap(data.corr())

data['participation']=[random.randint(0, 100) for i in range(len(lst))]
data.head(10)

data.describe()

import seaborn
