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

fn = ("https://archive.stsci.edu/missions/kepler/lightcurves/"
      "0084/008462852/kplr008462852-2011073133259_llc.fits")

cbv = KeplerCBVCorrector(fn)
best_list_of_cbvs = cbv.get_cbvs_list()
print(best_list_of_cbvs)

list_of_cbvs = []
for n in range(1, 15):
    list_of_cbvs.append(range(1, n+1))

print(list_of_cbvs)

n_cbvs = [len(list(list_of_cbvs[i])) for i in range(len(list_of_cbvs))]

plt.plot(n_cbvs, cbv.bayes_factor, 'ko-.', markersize=5)
plt.xlabel('Number of CBVs')
plt.ylabel(r'Bayes Factor')

plt.savefig('cbv-grid-search.eps', bbox_inches='tight', pad_inches=.1)
