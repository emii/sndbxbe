Title: Compensation for transversal chromatic aberration
Summary: Analysis and correction for the spectral 
Abstract: The wavelength-dependency of the refraction indices in optical systems involves chromatic aberrations: one object point is not projected on exactly one image point on the sensor plane, but dispersed depending on its wavelengths in a rainbow-like manner due to the wavelength-dependency. When precise estimation of the three-dimensional position of a point is necessary &mdash;as in HD DNA&ndash;FISH experiments&mdash; the distortions have to be compensated. Here, I describe the measurement of these distortions, as well as their compensation and further evaluation.
Tags: matlab, research, microscopy, image processing, dna-fish
Category: research


## Fluorescent beads position detection and enhancement

Commercial fluorescent beads where imaged and detected in different channels. For each channel, the acquired image stack of 15 planes in depth was filtered and thresholded to automatically detect the coarse position of the single beads in a 3D space (1024px $\times$ 1024px $\times$ 15 planes). The threshold was set automatically for a reference channel as the intensity value for which the inverse of the coefficient of variation was the highest. The threshold for the remaining channels was selected for the detected beads to be close if not the same in number to the ones detected on the reference channel. For each channel, the detected coarse positions $(x,y)$ where enhanced for precision by fitting a 2D Gaussian function to the original image intensity distribution in a window of a 6px radius from the calculated coarse position. For the $z$ coordinate position, the intensity profile along the z-depth was calculated in the $(x,y)$ coordinates previously calculated, then, a 1D Gaussian function was fitted, and the 

### The 2D Gaussian function model

I used this model to fit the intensity distribution in 2D:

\\begin{equation}
f(x,y) = a e^ {- \left(\frac{(x-x_o)^2}{2\sigma_x^2} + \frac{(y-y_o)^2}{2\sigma_y^2} \right)} + b
\\end{equation}

### The 1D Gaussian function model:

After getting the $(x,y)$ position, the intensity profile of this position along the z-axis was used to fit the following 1D gaussian function:

\\begin{equation}
f(x,y) = a e^ {-\frac{(z-z_o)^2}{2\sigma_z^2}} + b
\\end{equation}

After enhancement of 3D position, the corrected values were observed to look pretty much like the coarse positions for most of the fluorescent beads.

## Beads registration and shift measurement

Since the corresponding signals of a bead in different channel do not co-localize, first we had to find the signals corresponding to the same single bead. This might be trivial for low density beads in the FOV, however it proved to be difficult on high density number of beads or mis-assignment due to other factors as debris and bead movement. To do this, for each channel, we assigned a connection between the selected bead and its closest neighboring bead signals regardless of the channel, under the assumption that the shift difference between channels is minimal and the closest signals correspond to the same bead. Then we used this information to build an undirected adjacency matrix where an edge was assigned every time we found a mutual connection between two bead signals. This criteria allowed us to build independent and completely connected graphs called _cliques_, which correspond to single beads.

With this method we achieved the correct identification of most of the beads. Once the beads where "registered", the shift in each direction was calculated as a function of its position in the $xy$ plane since we only have information for the plane:

\\begin{equation\*}
\Delta_x = f(x,y)\\\\
\Delta_y = f(x,y)\\\\
\Delta_z = f(x,y)
\\end{equation\*}

where for each channel:

\\begin{equation\*}
\Delta^{ch}\_{xi} = x^{ch}_i - x^{ref}_i \\\\
\Delta^{ch}\_{yi} = y^{ch}_i - y^{ref}_i \\\\
\Delta^{ch}\_{zi} = z^{ch}_i - z^{ref}_i \\\\
\\end{equation\*}


\\begin{equation\*}
	\Delta(x,y) = a_{n,n}x^ny^n + a_{n,n-1}x^ny^{n-1} + a_{n-1,n}x^{n-1}y^n + \ldots + a_{1,0}x + a_{0,1}y + a_{0,0}
\\end{equation\*}


Alternatively, and more optimally, we would like to have information of the $xy$ plane, also at different z-depths, thus to calculate the shift as a function of a volume, as follows:

\\begin{equation\*}
\Delta_x = f(x,y,z)\\\\
\Delta_y = f(x,y,z)\\\\
\Delta_z = f(x,y,z)
\\end{equation\*}

This would require an experiment in which the beads are distributed both in the $xy$ plane, as well as at different z-depths. However, Stefan made a remark on this, in the sense that the experiment would require to embed the beads in a medium, thus changing the propagation of light since its refractive properties my vary. This would made the measurments incompatible with the actual experimental setup. 

In the first scenario, to interpolate the shift in positions not covered by the beads, fifth order polynomials were fitted for each of the directions. The smoothness of the function is what makes them atractive to fit the shift, as we expect it to be very smooth.














