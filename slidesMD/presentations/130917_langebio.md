## Chromatin topology plays an important role in gene regulation
![slide1](/static/images/slides/chromatin-organization/slide1_2.png)

## Chromatin organization is approached theoretically by polymer models
One characteristic feature of a polymer model is the mean-squared spatial end-to-end distance $\\langle R^{2}\\rangle$ which as a function of its genomic distance $g$ scales $\\langle R^{2}\\rangle \\sim g^{2\\nu}$, the exponent $\\nu$ varies given the dynamics of each polymer representation, such as random walk, self-avoiding walk, or globular state ([Tark-Dame et al. 2012](#Tark-dame2012))

* _Fractal globule_ ([Lieberman-Aiden et al. 2009](#Lieberman-Aiden2009a))
* _Random loop_ ([Mateos-Langerak et al. 2009](#Mateos-Langerak2009))
* _String and binders switch_ ([Barbieri et al. 2013](#Barbieri2012))

## Nuclear Topology is experimentally addressed by 3C and FISH

* __3C__ formaldehyde crosslinking snapshots on the bulk to quantify distance between genomic loci, interpreted from contact probabilities
* __FISH__ fluorescently labeled probes are designed to target specific genomic loci. 

## Distance between chromatin regions are measured from 3D positions of fluorescent spots
![slide2](/static/images/slides/chromatin-organization/slide2.png)

</div><div class="slide" id="30" style="background-color:#000000;"><img alt="4 loci experiment" src="/static/images/slides/chromatin-organization/OL_008.png">

## Spots are identified for singles cells
![spotterUI2](/static/images/slides/chromatin-organization/spotterUI.png)

## Precise localization of the spots is estimated with Gaussian functions
![Dot image](/static/images/slides/chromatin-organization/dot_image.png)

\\begin{equation}
	f(x,y) = A \exp\left(- \left(\frac{(x-x_o)^2}{2\sigma_x^2} + \frac{(y-y_o)^2}{2\sigma_y^2} \right)\right) + b
\\end{equation}

\\begin{equation}
	f(z) = A \exp \left( -\frac{(z-z_o)^2}{2\sigma_z^2}\right)
\\end{equation}

## 
![gaussian_fit](/static/images/slides/chromatin-organization/2D_Gaussian_1D_gaussian.png)


## Chromatic aberrations are corrected after registering fiduciary markers

![Beads identification][beads_labeled]

[beads_labeled]: /static/images/slides/chromatin-organization/beads_identification.png

![Beads dense][beads_dense]

[beads_dense]: /static/images/slides/chromatin-organization/beads_dense_panels.png

##

\\begin{equation\*}
\Delta^{ch}\_{xi} = x^{ch}_i - x^{ref}_i \\\\
\Delta^{ch}\_{yi} = y^{ch}_i - y^{ref}_i \\\\
\Delta^{ch}\_{zi} = z^{ch}_i - z^{ref}_i \\\\
\\end{equation\*}

Then for each channel we formulated the shift $\\Delta$ as a function of the three-dimesional localization:

\\begin{equation\*}
\Delta^{ch}\_{x}= f(x,y,z)\\\\
\Delta^{ch}\_{y} = f(x,y,z)\\\\
\Delta^{ch}\_{z} = f(x,y,z)
\\end{equation\*}

## Distortions are wavelength dependent

![uncorrected](/static/images/slides/chromatin-organization/uncorrected.png)

## Shift is modeled as a higher degree polynomial

\\begin{equation}
	\Delta^{ch}\_{dim}(x,y,z) = a_{n,n,n}x^ny^nz^n + a_{n,,n,n-1}x^ny^nz^{n-1} + a_{n,n-1,n}x^ny^{n-1}z^n + \ldots + a_{1,0,0}x + a_{0,1,0}y + + a_{0,0,1}z + a_{0,0,0}
\\end{equation}

##

![shiftw](/static/images/slides/chromatin-organization/shoftw.png)

## Shift is notably reduced 

![corrected](/static/images/slides/chromatin-organization/corrected.png)

##

!![TMR shift][tmr_shift]

[tmr_shift]: /static/images/slides/chromatin-organization/tmr_calibXY.jpg

## Distances within single chromosomes are measured
![distances](/static/images/slides/chromatin-organization/slide5.png)

## Our results are in agreement with previous observations
![4 loci counts][4_loci_level]

<pre style="text-align:right;">Mateos-Langerak et al. 2009 PNAS</pre>

[4_loci_level]:/static/images/slides/chromatin-organization/slide6.png
### Outlook
#### Combinatorial labeling provides identifiers for unique regions
![distances](/static/images/slides/chromatin-organization/comb-label.png)
## Concluding remarks

* A major question in understanding spatial genome organization is how patterns of chromosome or loci organization are established and maintained

* Better resolution and perhaps multiplexing for the precise estimation of the localization of chromosome regions can be acheived by using our methodology 

* These measurements will provide insight in understanding the formation of patterns in chromatin organization

## Aknowledgements

### Group van Oudenaarden

#### at MIT:
* Magda Bienko
* Stefan Semrau

#### at the Hubrecht Institute:
* Alexander van Oudenaarden

## try come code:

	::latex::
	begin{equation}
	   E = mc^2
	   e^{\pi i}+1 = 0 \frac{x}{y}
	end{equation}
### is translated into:

\begin{equation}
E = mc^2 \\
e^{\pi i}+1 = 0 \frac{x}{y}
\end{equation}

</div><div class="slide" id="30" style="background-color:#000000;"><h1 style="color:#fafafa;">Thank you!</h1>

