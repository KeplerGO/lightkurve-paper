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

list_of_cbvs = []
for n in range(1, 16):
    list_of_cbvs.append(range(1, n+1))

neg_log_likelihood = []
for cbvs in tqdm(list_of_cbvs):
    cbv.correct(list(cbvs), options={'xtol': 1e-6, 'ftol':1e-6, 'maxfev': 2000})
    print(cbv._coeffs)
    neg_log_likelihood.append(cbv.opt_result.fun)

n_cbvs = [len(list(list_of_cbvs[i])) for i in range(len(list_of_cbvs))]

plt.plot(n_cbvs, neg_log_likelihood, 'ko-.', markersize=5)
plt.xlabel('Number of CBVs')
plt.ylabel(r'Cost function, $p=1$')

plt.savefig('cbv-grid-search.eps', bbox_inches='tight', pad_inches=.1)
