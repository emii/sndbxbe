Title: Lab Meeting in html
Summary: lab meeting content
Abstract: My lab metting
Date: 2013-04-10
Category: projects
Tags: biology, research, hd dna-fish, master, report, presentation

## The title:

>A glimpse into chromatin organization by HD-DNA FISH~

- - -

>The data analysis pipeline for HD-DNA FISH~

## Outline

* Introduction
* Explain the general analysis pipeline
	* The SpotterUI 
* Interleaved 4-loci spotting
* Combinatorial labeling spotting
* Measuring and correcting the shift
	* projective transform as a first approach
	* a more refined approach
* What would be next

## What is HD DNA-FISH?

* A methodology that allow us to visualize genomic regions between 3 kbps and 10 kbps
* It uses hybridization of ~4 times labeled 200nt amplicons
* Similar to smRNA-FISH, this regions are detected as small fluorescent spots
* Adds some sophistication to smRNA FISH
* Requires higher precision for spot identification
* Exact 3D position matters 

## The spot identification pipeline

1. Segmentation of the ROIs
2. Correct for the shift between channels
3. Increase S/N ratio (filter for particle size - LoG)
4. Select for the intensity threshold
3. Count, assign, and compute spot features
	* Precise position
	* Intensity, volume, FWHM

## The spot identification pipeline

1. __Segmentation of the ROIs__
2. __Correct for the shift between channels__
3. Increase S/N ratio (filter for particle size - LoG)
4. Select for the intensity threshold
3. __Count, assign, and compute spot features__
	* __Precise position__
	* __Intensity, volume, FWHM__

## The SpotterUI is a cub from ImageM

![SpotterUI][spotterUI]

[spotterUI]: /static/images/slides/chromatin-organization/spotterUI_segmentation.png

## The shift is corrected by a linear transformation

![bead selection tool][cps]

[cps]: /static/images/slides/chromatin-organization/CPS.png

## The applied transformation seems to work 

![TMR shift][tmr_shift]

[tmr_shift]: /static/images/slides/chromatin-organization/tmr_calibXY.jpg

## The spots are counted after selecting a threshold value

![SpotterUI2][spotterUI2]

[spotterUI2]: /static/images/slides/chromatin-organization/spotterUI.png


<div class="slide" id="31" style="background-color:#000000;"><p style="text-align:center;"><h3 style="color:#fafafa; text-align:center;">The 4 loci experiment</h3></p><p><img alt="4 loci experiment" src="/static/images/slides/chromatin-organization/OL_008.png"></p></div>

## The 4 loci experiment
![4 loci][4_loci]

[4_loci]: /static/images/slides/chromatin-organization/4_loci.png

* Interleaved probe sets in both A594 and Cy5 are separated each 10 Mbp
* Single chromosomes are observed to be separated in a large fraction of cells
* 1 distance between spots of the same color
* 4 distances between spots of different colors

## The numbers after counting

![4 loci counts][4_loci_counts]

* Counts for both channels are expected to be _almost_ the same
* The total spot counts resembles the cell-cycle-phase distribution

[4_loci_counts]: /static/images/slides/chromatin-organization/4_loci_counts.png

##
### 37 out of 324 nuclei have a 4:4 spots configuration

![4 loci counts][4_loci_conf1]

[4_loci_conf1]: /static/images/slides/chromatin-organization/configurations_of_dots1.png

## K-means clustering is applied and certain configuration selected

![4 loci conf][4_loci_conf]

[4_loci_conf]: /static/images/slides/chromatin-organization/4_loci_conf.png

##

![4 loci counts][4_loci_hists]

[4_loci_hists]: /static/images/slides/chromatin-organization/counts3_hists.png

##

![4 loci counts][4_loci_dists]

[4_loci_dists]: /static/images/slides/chromatin-organization/more_counts1.png

##
### 61 out of 324 nuclei have 4:4,3:4,4:3,4:5,5:4 spots configurations
![4 loci counts][4_loci_conf2]

[4_loci_conf2]: /static/images/slides/chromatin-organization/configurations_of_dots2.png


##

![4 loci counts][4_loci_dists1]

[4_loci_dists1]: /static/images/slides/chromatin-organization/more_counts.png

##
### A leveling-off of physical distances > 20 Mbp is observed

![4 loci counts][4_loci_level]

<pre style="text-align:right;">Mateos-Langerak et al. 2009 PNAS</pre>

[4_loci_level]: /static/images/slides/chromatin-organization/level-off.png

## Combinatorial labeling setup

![Combinatorial labeling][comb_label]

[comb_label]: /static/images/slides/chromatin-organization/comb-label.png

* When observing to the data, I found no major co-localization of the probes
* I then went back to do a more detailed assessment of the shift calibration

## Summary I

* Some improvements to ImageM were made: auto-segmentation, interaction with single nuclei, etc.
* The linear transformation for the correction of the shift was fine as a first approach, however not enough for the multi-labeling scenario
* A refined method for correcting the shift is necessary

## Chromatic Aberrations

Dispersion: When different colors of light propagate at different speeds in a medium, the refractive index is __wavelength dependent__. Chromatic aberrations are those __departures__ from __perfect imaging__ that are due to dispersion.

- - -

<p style="text-align:center;">Axial chromatic aberration</p>
![ Axial chromatic aberration ][axial] 
<p style="text-align:center;">the shift is in the z direction</p>

- - -

<p style="text-align:center;">Transverse chromatic aberration</p>
![ Transverse chromatic aberration ][transverse] 
<p style="text-align:center;">the shift is in the xy plane</p>

[axial]: /static/images/slides/chromatin-organization/long_color.gif
[transverse]: /static/images/slides/chromatin-organization/lat_color.gif

## First approach to correct for the shift

###The projective transformation

![Projective transformation][projective_transformation]

[projective_transformation]: /static/images/slides/chromatin-organization/projective_transform.png

## Drawbacks

* although is position based (XY), it stills linear
* based on manual selection of the beads (variability)
* only performs correction on the XY plane

## Second approach to correct the shift

1. Automatic identification of the  coarse position for all beads in the different channels
2. Refinement of the coarse position by fitting a 2D gaussian for the XY plane and a 1D gaussian for the Z position along the x,y coordinates gotten from the 2D gaussian
3. Fit a plane for each Z-position and interpolate. (Before talking to Stefan)

## 1. Beads are identified by (close) distance relation

* a __clique__ is a complete subgraph (all nodes are conected to each other)

* __Automatic identification of fluorescent beads in different channels__

	* how to know that a given bead position in one channel corresponds to same bead in the other channel?

		1. use of distances to build an adjacency matrix
		2. from the adjacency matrix find the cliques of size(number of channels)

	* possible problems:

		1. misidentification  of debris as beads
		2. movement of beads from one channel to another
		3. beads closer than corresponding shift


## Beads identification

![Beads identification][beads_labeled]

<p style="text-align: center;">
<strong>A.</strong>beads image
<strong>B.</strong> identification of single cliques
<strong>C.</strong> zoom of the identified cliques
</p>

[beads_labeled]: /static/images/slides/chromatin-organization/beads_identification.png

## Dense distribution of beads

![Beads dense][beads_dense]

<p style="text-align: center;">
<strong>A.</strong>beads image
<strong>B.</strong>identification of nearest beads in other channels
<strong>C.</strong>identification of beads' cliques
</p>

[beads_dense]: /static/images/slides/chromatin-organization/beads_dense_panels.png

## Shift measurement

![Shift quantification][shift_quant]

[shift_quant]: /static/images/slides/chromatin-organization/shift_magnitude.png

## Shift measurement
### After calibration using the linear transform

![Shift quantification calib][shift_quant_calib]

[shift_quant_calib]: /static/images/slides/chromatin-organization/shift_magnitude_clalib.png


## 2. Beads are fitted to Gaussian functions

### A bead seen from different planes

![Dot image][dot_image]

[dot_image]: /static/images/slides/chromatin-organization/dot_image.png

## Gaussian function fitting
![Gaussian Fit][gaussian_fit]

[gaussian_fit]: /static/images/slides/chromatin-organization/2D_Gaussian_1D_gaussian.png


## Outlook

### Precise position estimation

* Use automatic identification of the beads together with gaussian fit correction to get the coordinate positioning of the beads and correct the shift. Use the same approach to get the HD-FISH spots features

* From there use Stefan's approach to calculate the shift as a function of the position in x,y, and z of the beads

* Experiment-wise, Magda is preparing a 2-channel single-loci DNA-FISH image acquisition which would help to calculate the shift specific for the medium in which probes are. Also to estimate the shift at different z-planes (no need of 3D experiment with beads) 

### After precise position estimation

* Re-analyze the 4 loci experiment

* Continue the analysis of the multi-labeling experiment

## Aknowledgements

* Magda
* Stefan
* Lennart
* Mauro
* Philipp
* Alexander
