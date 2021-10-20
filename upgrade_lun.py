from multiprocessing import Pool
from numba import njit, guvectorize, float64, int64
import numpy as np

batch = 10
Card_num = np.array([np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN])
arr_of_cards = np.hstack(list(Card_num) * batch)
arr_of_cards.resize((10, 15))
arr_of_cards.transpose()


@guvectorize([(float64[:], float64[:])], '(n)->(n)')
def g(x, res):
    for i in range(x.shape[::][0]):
        res[i] = x.sum()


@njit()
def gen_num_card(arr):
    arr_of_cards = arr
    arr_of_cards[:, :] = \
        np.random.choice(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                         size=arr_of_cards[:, 6:12].size).reshape(10, 6)
    ev = arr_of_cards[:, ::2] * 2
    ev = np.where(ev < 9, ev, ev - 9)
    odd = arr_of_cards[::, 1::2]
    return ev, odd


@guvectorize([(float64[:], float64[:])], '(n) -> (n)')
def numba_transpose(arr, res):
    res[i] = arr[-i]


@guvectorize([(float64[:, :], float64[:, :], float64[:, :], int64[:])], '(m,n),(m,n),(m,n)->(n)')
def check(ev, odd, check_arr, res):
    res = np.remainder(ev + check_arr + odd, 10)

@njit()
def check_check():
    n=-1
    index=[]
    for i in np.char.find('0', np.remainder(ev[:, 0:1] + check_arr + odd[:, 0:1], 10).astype(str)):
        n+=1
        if i != -1:
            index.append(n)
    re


for i in range(10):
    ev, odd = gen_num_card(arr_of_cards)
    check_arr=np.array([6.]*batch).reshape(-1,1)
    ev = g(ev)
    odd = g(odd)
    numba_transpose(ev)
    #print(numba_transpose(odd))
    #print(odd[:, 0:1], ev[:, 0:1], check_arr)
    #cards = check(ev[:, 0:1], odd[:, 0:1], check_arr)
    check_tmp = np.char.find('0', np.remainder(ev[:, 0:1] + check_arr + odd[:, 0:1], 10).astype(str))
    for i in check_tmp

    #print(cards)
    #if cards is None:
    #    print('No cards...')
    #else:
    #    print('REAL SHIT:' + str(cards))
    #    with open('File', 'a+') as f:
    #        f.write(cards)
