from pyke.lightcurve import KeplerLightCurveFile

from matplotlib import rc, pyplot as plt
import matplotlib
matplotlib.rcParams['text.latex.unicode'] = True
rc('text', usetex=True)
font = {'size'   : 16}
rc('font', **font)

lc_file = KeplerLightCurveFile("https://archive.stsci.edu/missions/kepler/lightcurves/"
                               "0119/011904151/kplr011904151-2009350155506_llc.fits")

klc = lc_file.PDCSAP_FLUX.flatten().fold(period=0.837495, phase=131.574858)
plt.plot(klc.time, klc.flux, 'ko', markersize=3)
plt.plot(klc.time, klc.flux, 'o', color='#ff3366', markersize=2)
plt.ylabel(r"Normalized Flux $(e^{-}s^{-1})$")
plt.xlabel(r"Phase (\textrm{Time from Transit Epoch})")
plt.savefig('fold-lc.eps', bbox_inches='tight', pad_inches=.1)
