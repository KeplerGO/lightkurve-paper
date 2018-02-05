import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
import numpy as np
from pyke import KeplerTargetPixelFile
from pyke.utils import KeplerQualityFlags

matplotlib.rcParams['text.latex.unicode'] = True
rc('text', usetex=True)
font = {'family' : 'serif',
        'size'   : 14,
        'serif'  : 'New Century Schoolbook'}
rc('font', **font)

tpf = KeplerTargetPixelFile('https://archive.stsci.edu/missions/kepler/target_pixel_files/'
                            '0084/008462852/kplr008462852-2011073133259_lpd-targ.fits.gz',
                            quality_mask=KeplerQualityFlags.HARDEST_BITMASK)

tpf.plot()
plt.savefig('tpf-plot.pdf', bbox_inches='tight', pad_inches=.1)

tpf.plot(aperture_mask=tpf.flux[0] > np.nanmean(tpf.flux[0]))
plt.savefig('tpf-plot-aperture.pdf', bbox_inches='tight', pad_inches=.1)

