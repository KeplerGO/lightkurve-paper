from pyke.lightcurve import KeplerLightCurveFile

from matplotlib import rc, pyplot as plt
import matplotlib
matplotlib.rcParams['text.latex.unicode'] = True
rc('text', usetex=True)
font = {'family' : 'serif',
        'size'   : 14,
        'serif'  : 'New Century Schoolbook'}
rc('font', **font)

lc_file = KeplerLightCurveFile("https://archive.stsci.edu/missions/kepler/lightcurves/"
                               "0119/011904151/kplr011904151-2009350155506_llc.fits")

klc = lc_file.get_lightcurve("PDCSAP_FLUX").fold(period=0.837495)
plt.plot(klc.time, klc.flux/1e5, 'ko', markersize=3)
plt.plot(klc.time, klc.flux/1e5, 'o', color='#ff3366', markersize=2)
plt.ylabel(r"Flux $(10^5e^{-}s^{-1})$")
plt.xlabel(r"Phase")
plt.savefig('fold-lc.eps', bbox_inches='tight', pad_inches=.1)
