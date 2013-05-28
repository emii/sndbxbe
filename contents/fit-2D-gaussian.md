Title: 2D gaussian fit
Summary: check this to see how to find parameters for 2D gaussian fit or else
Abstract: From an image of fluorescent beads I want to find an accurate position of a diffraction limited spot, the first approach is to fit a 2D gaussian function of a window of 12 px around the centroid of a filtered and thresholded spot
Category: projects
Tags: biology, research, hd dna-fish, MATLAB, visualization, 2D, 3D, graphs, plotting, fitting
Date: 2013-03-28

##Some useful functions in MATLAB

* [Anonymous Function](http://www.mathworks.nl/help/matlab/matlab_prog/anonymous-functions.html?s_tid=doc_12b)
* [Curve Fitting - Surface](http://www.mathworks.nl/help/curvefit/surface-fitting.html)
	* [Library of Models for Surface Fitting](http://www.mathworks.nl/help/curvefit/list-of-library-models-for-curve-and-surface-fitting.html)
* [Multivariate Gaussian Functions](http://en.wikipedia.org/wiki/Multivariate_normal_distribution)
* [Fit 2D gaussian to data](http://www.mathworks.com/matlabcentral/fileexchange/37087-fit-2d-gaussian-function-to-data/content/D2GaussFunction.m)
* [2D rotated gaussian fit](http://www.mathworks.com/matlabcentral/fileexchange/39448-2d-rotated-gaussian-fit)
* [Representing Data as a Surface](http://www.mathworks.nl/help/matlab/visualize/representing-a-matrix-as-a-surface.html)
* [Coloring surface Data!](http://www.mathworks.nl/help/matlab/visualize/coloring-mesh-and-surface-plots.html)
* [Matlab surf plot](http://www.mathworks.nl/help/matlab/ref/surf.html)
* [surface plus image plot](http://www.peteryu.ca/tutorials/matlab/image_in_3d_surface_plot_with_multiple_colormaps)
* [Max Likelihood estimation](http://www.mathworks.nl/help/stats/gmdistribution.fit.html)
* [Multivariate modeling](http://www.mathworks.nl/help/stats/probability-distributions-used-for-multivariate-modeling.html)
* [how fit multivariate gaussian to data](http://www.mathworks.nl/support/solutions/en/data/1-85ZP9G/?product=ST&solution=1-85ZP9G)
* [multivariate pdf](http://www.mathworks.nl/help/stats/mvnpdf.html)
* [mixture models tutorial](http://www.mathworks.com/matlabcentral/fileexchange/13493-linstats-2006b/content/linstats/tutorials/html/mmvn_tutorial.html#1)
* [calculate PSF](http://www.johnloomis.org/eop601/notes/matlab/psf/fft_psf.html)
* [deblurring by deconv pfs](http://blogs.mathworks.com/steve/2007/08/13/image-deblurring-introduction/)
* [generate PSF](http://www.mathworks.com/matlabcentral/fileexchange/35612-create-a-non-isotropic-3d-gaussian-point-spread-function-psf/content/nonIsotropicGaussianPSF.m)
* [generate PSF 2](http://www.mathworks.com/matlabcentral/fileexchange/31945-widefield-fluorescence-microscope-point-spread-function)
* [Fluorescence microscopy](http://en.wikipedia.org/wiki/Fluorescence_microscope)

## other important concepts

### Optical aberrations

[optical aberration](http://en.wikipedia.org/wiki/Optical_aberration)

* [wavefront aberration](http://en.wikipedia.org/wiki/Wavefront)
* [spherical aberration](http://en.wikipedia.org/wiki/Spherical_aberration)
* [coma](http://en.wikipedia.org/wiki/Coma_(optics))
* [huygens principle](http://en.wikipedia.org/wiki/Huygens%27_principle)
* [paper on this](http://www.sciencedirect.com/science/article/pii/S0042698911003099)
* [difraction limited systems:wiki](http://en.wikipedia.org/wiki/Diffraction_limited)
* [Point Spread Function](http://en.wikipedia.org/wiki/Point_spread_function)
* [Airy Disk](http://en.wikipedia.org/wiki/Airy_disk)
* [chromatic aberration](http://en.wikipedia.org/wiki/Chromatic_aberration)

'a + b*exp(-(((x-c1)/w1)^2 + ((y-c2)/w2)^2))'
'a*exp(-x-c)'



### model latex:
		
	:::latex	
	f(x,y) = A \exp\left(- \left(\frac{(x-x_o)^2}{2\sigma_x^2} + \frac{(y-y_o)^2}{2\sigma_y^2} \right)\right)

### The equation:

\\begin{equation}
f(x,y) = A \exp\left(- \left(\frac{(x-x_o)^2}{2\sigma_x^2} + \frac{(y-y_o)^2}{2\sigma_y^2} \right)\right)
\\end{equation}

model matlab:

a*exp(-(x.*x/2/sig(1)^2 + y.*y/2/sig(2)^2))



