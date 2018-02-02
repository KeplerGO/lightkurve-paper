# Outline for the paper

1. Introduction
  - (Decide what you want to call PyKE / lightkurve)  Is it a framework?  A tool?  A library? )
  - Lay out the challenges facing data analysis for time series astro data
  - Cite work that has been done on addressing specific aspects of these challenges
  - Motivate the need for a general purpose framework to address practical challenges
  - Lay out the overlying philosophy/goals: simplicity, sane defaults, seemless data access (local or remote), reproducibility, support for multiple complimentary algorithms through keyword arguments, metadata access, performance, extensibility, etc, etc, etc, etc.
2. Lightcurve Basics
  - Intro to lightcurve basics. Which aspects of the design philosophies laid out in the introduction does the lightcurve class address?
  -The `LightCurve` class
  - The `KeplerLightCurveFile` class
  - Note the extensibility to TESS and other missions
3. Target Pixel File Basics
  - The `KeplerTargetPixelFile` class
  - Note the need for metadata access-- can come from FITS header, or elsewhere
  - (Attribute access reduces cognitive load associated in metadata book-keeping)
4. Tools
  - Cotrending basis vectors
  - PSF Photometry
  - Motion dependent Correlated Noise
5. Acknowledgments
6. References

