import numpy as np
import pandas as pd
from itertools import product

card_num = [5, 2, 4, 6, np.NaN, np.NaN, np.NaN, np.NaN,
            np.NaN, np.NaN, np.NaN, np.NaN, 5, 8, 8]

check = 6

first = np.array([5, 2, 4, 6])
end = np.array([5, 8, 8])

card_checked = []
card_true = []
count = 0
a, b, c, d, e, f, g, h = [0, 0, 0, 0, 0, 0, 0, 0]
while __name__ == "__main__":
    count += 1
    a = count
    for i in list(product('0123456789', repeat=8))[0:10]:
        H0 = np.concatenate([first, np.array(i).astype(int), end]).reshape(-1, 1)
        df = pd.DataFrame(H0)
        df.index = df.index + 1
        ev = df.loc[df.index.__divmod__(2)[1] == 0]
        odd = df.loc[df.index.__divmod__(2)[1] != 0] * 2
        odd.loc[odd[0] >= 9] = odd.loc[odd[0] >= 9] - 9
        # print(df.values.reshape(1,-1))
        print(divmod(int(sum(ev.values)) + int(sum(odd.values)) + check, 10)[1])
        if divmod(int(sum(ev.values)) + int(sum(odd.values)) + check, 10)[1] == 0:

            card_checked.append(df.values.reshape(1, -1))
            card_true.append(df.values.reshape(1, -1))
            print('Hey, {} is real!'.format(len(card_true)))
            with open('true_card.txt', 'a+') as f:
                f.write(card_true)
        else:
            card_checked.append(df.values.reshape(1, -1))
            #print(df)
