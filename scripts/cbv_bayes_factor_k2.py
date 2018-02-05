import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
import matplotlib
matplotlib.rcParams['text.latex.unicode'] = True
rc('text', usetex=True)
font = {'family' : 'serif',
        'size'   : 14,
        'serif'  : 'New Century Schoolbook'}
rc('font', **font)

import matplotlib.pyplot as plt
from tqdm import tqdm
from pyke import KeplerCBVCorrector

fn = ("https://archive.stsci.edu/missions/k2/lightcurves/"
      "c14/201500000/43000/ktwo201543306-c14_llc.fits")

fn = ("https://archive.stsci.edu/missions/k2/lightcurves/"
      "c14/201400000/32000/ktwo201432493-c14_llc.fits")

cbv = KeplerCBVCorrector(fn)
best_list_of_cbvs = cbv.get_cbvs_list()

list_of_cbvs = []
for n in range(1, 16):
    list_of_cbvs.append(range(1, n+1))

n_cbvs = [len(list(list_of_cbvs[i])) for i in range(len(list_of_cbvs))]

print(len(cbv.bayes_factor))

plt.plot(n_cbvs, cbv.bayes_factor, 'ko-.', markersize=5)
plt.xlabel('Number of CBVs')
plt.ylabel(r'Bayes Factor')

plt.savefig('cbv-bayes-factor.eps', bbox_inches='tight', pad_inches=.1)
