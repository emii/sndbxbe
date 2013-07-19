Title: HD-FISH, a glimpse into chromatin organization
Date: 2013-07-01
Summary: The written report after finishing my internship at the van Oudenaarden lab about HD-FISH and the data analysis
Category: projects
References: contents/bibtex/dna-fish.bib
Tags: biology, research, hd dna-fish, master, report
Abstract: <strong>Abstract:</strong> Chromosomes change their  topology throughout the cell cycle varing its position and degree of compaction. This features have been observed to influence gene expression, as mutations perturbing the overall topology of the nuclear envelope have deleterious effects (see progeria syndrome). Previous methodologies have addressed chomatin conformation in different ways (see Hi-C, Paint probes 3D DNA FISH). However either their resolution is limited or, frquent error rate.

[TOC]

# Introduction

<!First we try to emphasize the idea of chromosome organization by connecting it to gene expression, hence to funciton>

The control of gene expression in eukaryotes can be viewed as the integrated response of mechanisms working at different hierarchical levels. Gene transcription is regulated from the sequence level to the chromatin level, to the nuclear level ([van Driel et al. 2003](#VanDriel2003)) (see **Figure 1. Top**). At this top-most layer, the higher order topology of the genome has proven to play an important role, as meaningful patterns of organization have been identified; after mitosis, chromosomes decondense into fibers which remain confined into well defined and isolated compartments called _chromosome territories_ (Cremer et al. 2010). Generally gene-poor chromosomes are more frequently positioned in the outer regions of the nucleus, where as gene-rich chromosomes adopt a more internal localization (Croft et al. 1999, see **Figure 1-1**). Moreover, motion of genes along the radial axis of the nucleus has been observed upon gene activation, movements either toward the nuclear interior or toward the nuclear periphery, however, other observations show that the former is not exclusively a repressive location (Andrulis et al. 1998, Boyle et al. 2001, Casolari et al. 2005, Mesiter et al. 2010). Alongside, distributed throughout the nucleus, sets of activated genes are spatially arranged into discrete foci termed _transcription factories_ &mdash;dedicated to the expression of specific combinations of genes, even from distinct chromosomes&mdash; (Spilianakis et al. 2005, Osborne et al. 2007, Schoenfelder et al. 2009 and 2010). These particular arrangements indicate that the associations at the transcriptional hot spots does not happen at random, but genes have preferential partners, commonly in a tissue specific manner (Osborne et al. 2007, see **Figure 1-2**). In addition, significant changes in spatial organization of genomes are triggered during cellular differentiation reflecting a dramatic change in gene expression (Kim et al. 2004).

![figure 1][fig1]
[fig1]: /static/images/slides/chromatin-organization/slide1_2.png
<p class="caption"><strong>Figure 1. Top:</strong> Schematic illustration of the different layers of organization in the mammalian nucleus. From left to right: Chromosomes are organized in chromosome territories which are composed of smaller globular structures that intermingle at some extent. These globules are compacted loops of a 30 nm fiber with a solenoid, zigzag or polymer melt configuration. At the lowest level, chromatin is organized in a 10 nm, <em>beads on a string</em> fiber consisting of nucleosomes. <strong>Bottom: 1.</strong> A highly compartmented nucleus with non-random chromatin organization. Chromosomes are organized into territories in the interphase nucleus. They are further arranged such that active regions are more commonly localized towards the nuclear interior whereas inactive portions tend to adopt a more external position <strong>2.</strong> Actively transcribed genes associate at the periphery of chromosome territories. Intra and interchromosomal contacts bridge coregulated genes as well as enhancer and promoter pairs.</p>

<!Once I make the point of the importance of chromatin organization, I start talking about how is it organized, from structure, and the features that can be abstacted into biophysical models>

The higher-order structure of chromatin offers an extra level of epigenetic regulation. Many factors may be involved in the modulation of nuclear conformations. Both local and long-range biochemical interactions between specific genomic regions, as well as the anchoring of chromatin domains to the nuclear lamina, shape and constrain the available topologies for the fiber to fold into, emphasizing the link between the linear structure and the spatial chromatin arrangement (Marshall et al. 1997, Chubb et al. 2002, Bickmore & van Steensel 2013).

## Theoretical approaches to chromatin organization

<!then I will introduce a bit of the polymer models to approach and answer physical properties of chromatin structure>

The overall nuclear structure can be characterized by a set of features that range from cell cycle stage, spatial compartmentalization, degree of compaction, radial positioning within the nucleus, extent of intermingling, genomic to physical distance scaling, among others. These characteristics, together with the view of the chromatin fiber as an ensemble of nucleosomes &mdash;assuming a non-random spatial configuration &mdash; are suitable to be approached with polymer models, a unifying quantitative framework ([Tark-Dame et al. 2011](#Tark-Dame2011)). These models represent chromosome fibers made up of monomer units connected by a flexible connector, this _beads-on-a-string_ representation is _coarse-grained_ at the three-dimensional level, where descriptions for the small scale details are eliminated in favor of an overall structure ([Heermann et al. 2012](#Heermann2012)).

Computer simulations from polymer models demonstrate that some features of organization can be reproduced, such as the organization into chromosome territories ([Lieberman-Aiden et al. 2009](#Lieberman-Aiden2009a)). However, other model predictions deviate from experimental observations (i.e. the leveling-off of the linear to spatial scaling or the different scaling regimes at varying genomic lengths). This discrepancies provide evidence for additional molecular mechanisms contributing to chromatin folding which can be taken into account by accordingly extending the model assumptions.

<! here I emphasize the concept of scailing and then itroduce experimental approaches to quantify the distance, then remark fish as better since it also captures cell-to-cell variability, esential to bed-hedging or diferences in gene expression?>

One characteristic feature of a polymer model is the mean-squared spatial end-to-end distance $\\langle R^{2}\\rangle$ which as a function of its genomic distance $g$ scales $\\langle R^{2}\\rangle \\sim g^{2\\nu}$, the exponent $\\nu$ varies given the dynamics of each polymer representation, such as random walk, self-avoiding walk, or globular state ([Tark-Dame et al. 2012](#Tark-dame2012)); $R$ is the spatial distance between two genomic regions linearly separated by $g$ (see **Figure 2-1. Top**). For example, in the most simple random-walk model, the physical distance scales monotonically with increasing genomic separation, therefore, unable to match any of the experimentally observed nuclear patterns of organization (see **Figure 2-2. Top**). More recent polymer models already started to integrate further improvements to extend rather basic polymer models as are the _swollen coil_ or the _equilibrium globule_ (see **Figure 2-3. Top**). Models like the _fractal globule_ ([Lieberman-Aiden et al. 2009](#Lieberman-Aiden2009a)), the _random loop_ model ([Mateos-Langerak et al. 2009](#Mateos-Langerak2009)), and the recent _string and binders switch_ model ([Barbieri et al. 2013](#Barbieri2012)) are able to reproduce different aspects of the observed nuclear organization. 

To be tested for prediction accuracy, all these approximations require precise measurements of the scaling relation between the genomic and the physical distance. Hence, it is worth stressing out the importance of better and more extensive experimental techniques to acquire quantitative data and to supply support to adapt the previously mentioned theoretical representations.

<!After talking about the chromatin structure I would start talking about the current methods to study it, a brief intro to C3 and DNA FISH>

## Experimental techniques capturing chromatin structure

Recently, the development and refinement of techniques that allow the mapping of genomic regions onto the spatial context of the nucleus &mdash;both in bulk and up to the single cell level&mdash; has allowed to have quantitative measures to describe the principles of chromatin organization. High-coverage methods derived from 3C (Chromatin Conformation Capture, Dekker et al. 2003) use formaldehyde crosslinking snapshots on the bulk to quantify distance between genomic loci, interpreted from contact probabilities; closely localized regions are found to be crosslinked more frequently.

In a more direct strategy, single-cell distance measurements can be acquired from the imaging of DNA-FISH experiments (DNA fluorescensce _in situ_ hybridization), where fluorescently labeled probes are designed to target specific genomic loci. Their positions are identified by means of 3D fluorescensce-based microscopy, and subsequently, the distances between loci are measured (**see Figure 2 bottom panel.**). 

Both approaches are complementary, and both provide useful information in terms of nuclear topology which can be unified and reconciled with theoretical models. One advantadge of DNA-FISH experiments is that cell-to-cell variability can be captured in a population of fixed cells as snapshots of different chromatin configurations crucial for characterizing the differences in chromosomal conformations and locations. 

![techniques](/static/images/slides/chromatin-organization/slide2.png)
<p class="caption"><strong>Figure 2. Top:</strong> Relationship between physical distance and genomic distance for different polymer models. Schematic of the relation between $R$ which is the physical distance between two points on an interphase chromosome, and the genomic distance $g$. Random walk model, predicts that the mean squared distance $\\langle R^{2}\\rangle$ increases linearly with increasing genomic distance $g$. While the looped chromatin model, in contrast, predicts that $\\langle R^{2}\\rangle$ reaches a plateau at large genomic distances. <strong>Bottom:</strong> Light microscopy by fluorescent in situ hybridization; in our approach, <em>HD-FISH</em>, genomic regions are targeted by labeled amplicons of about 200 nt covering a region between 3 and 10 Kbp. In FISH experiments, chromatin folding shows a behavior where $\\langle R^{2}\\rangle$ reaches a plateau indicating the folding of chromosomes into territories.</p>

<!here use info from fudenberg & mirny	gen dev 2012 and from Bickmore and van steensel 2013, and Tark-Dame 2011>

<!Then i will finish with a short summary, sort of a motivation >

## Motivation

In a recent advancement, named _HD-FISH_, Bienko and collaborators (Bienko et al. 2013) reduced by one order of magnitude the effective target size of DNA-FISH probes thereby increasing the resolution up to the diffraction limit, this _spotting_ strategy allows the position localization to be estimated with higher accuracy. 

Here we propose the refinement of the current 3D DNA-FISH techniques and its extension by Bienko and collaborators by accurately localizing single genomic regions up to the sub-pixel resolution. This comprehensive measurements on the landscape of interacting genomic regions  will further help us to gain deeper insight into the heterogeneity and functional organizing principles of the genome.

<!Finishing with the especific objectives.>

## Objectives

The main objective of this study was to use images generated from _HD-FISH_ experiments to precisely mesaure the distance between various genomically separated loci up to the sub-pixel resolution. More specifically:

1. Generate a data analysis pipeline in MATLAB for feature localization and image processing of _HD-FISH_ experiments
1. Once the coarse localization of the  loci is identified, the effect of chromatic aberrations should be corrected, allowing the precise localization of the targeted regions
1. Distances are then calculated from corrected loci positions

<!System under investigation is a section which would describe the problem you want to resolve in the context of the experimenyal setup  or the especific experimental subject, in this case it would be the type of tissue and why is it this specific model selected, meaning advantages or special features and limitations>

## System under investigation

DNA has to be optimally folded to fit in the reduced volume of the nucleus conserving functional three-dimensional structure. This arrangement of chromosomes shows to be highly dynamic, changes arrangement throughout the cell cycle but despite the variability in organization among cells, chromatin  preserves common spatial patterns at some layers of organization. The chromosomes change from a highly condensed structures during mitosis, to form the more or less condensed _chromosome territories_ during interphase.

Here we approached the distribution of distances between genomic regions during interphase regardless of the cell type, in this manner obviating tissue specific differences.

For a population of cells we performed _HD-FISH_, image acquisition of several _fields-of-view_ and carried out image and statistical data analysis. Moreover, we integrated the data analysis workflow in a custom based semi-automated graphical implementation using MATLAB.

#Experimetal Approach
---

## Cell culture and fluorescence in situ hybridization.

We grew both _human mammary ephitelial cells_ (hTERT-HME1 mammary) and _primary human foreskin fibroblasts_ (ATCC CRL 2097) in Dulbecco's modified Eagle's medium with Glutamax (DMEM, Life Technologies) supplemented with penicillin/streptomycin and 10% FBS. To fix the cells, we followed the protocol of [Raj et al. 2008](#Raj2008). We fixed the cells for 10 min at room temperature using 4% formaldehyde/10% formalin in 1× phosphate buffered saline solution (PBS) and followed the fixation by two rinses in 1× PBS, after which we permeabilized the cells with 70% EtOH and stored them at 4 °C overnight.

The _HD-FISH_ probe sets used here were generated by real-time PCR reactions from genomic DNA with primers designed as previously described  by [Bienko et al. 2013](#Bienko2013), delimiting amplicons of length 200–220 nucleotides. The resulting  total of 50 to 80 unique fragments per region were subsequently labeled with the fluorophore of interest with the commercial kit for _Universal Linkage System_.

To perform DNA-FISH, 20 ng of _HD-FISH_ probe were ethanol precipitated using 20 µg of glycogen as carrier and dissolved in 20 µl of 1.7× SSC, 70% formamide, 50 mM Na<sub>2</sub>HPO<sub>4</sub>/NaH<sub>2</sub>PO<sub>4</sub>, 10% dextran sulfate and 5× Denhardt’s solution, pH 7.5. The three-dimensional _HD-FISH_ procedure on nuclei was adapted from [Solovei et al. 2010](#Solovei2010) preserving the three-dimensional nuclear structure. After hibridization, cover glasses were washed twice at 30 °C for 30 min in wash buffer, additionally 20 ng/ml DAPI were added to the second wash. After washes, the cover glasses were rinsed with 2× SSC.

For microscopy, samples were covered with a mounting solution containing 2× SSC buffer, 10 mM Tris, 0.4% glucose, 100 µg/ml catalase, 37 µg/ml glucose oxidase and 2 mM Trolox.

##Image acquisition

All images were acquired at 100× magnification (oil immersion, high numerical aperture Nikon objective) on an inverted epi-fluorescence microscope (Nikon) equipped with a high-resolution charge-coupled device (CCD) camera (Pixis, Princeton Instruments) and controlled by MetaMorph software.

We sequentially acquired three-dimensional stacks of fluorescence images in four different fluorescence channels using filter sets for DAPI, TMR, Cy5, and Alexa 594. Our exposure times were roughly 2–3 s for most of the dyes except for DAPI (which we exposed for ~100 ms). The pixel size was 0.125μm, and the spacing between consecutive planes in our stacks was 0.25 μm.

##Image analysis

Custom MATLAB software was implemented for the serial semi-automated identification of _HD-FISH_ fluorescent spots (see [Results and discussion](#results-and-discussion)), the general pipeline included the below described steps.

**Nuclei segmentation**

Using DAPI staining fluorescence signal, two criteria were used for segmentation. First the nuclei were segmented using Otsu´s method for finding the optimal threshold which minimizes the intra-class variance for intensity pixel values (under the assumption of a bimodal distribution), resulting in a binary image were most of the nuclei were correctly segmented (see **Figure 10.**). Following this step, a second criterium was taken into account for regions with an area above the average nuclei area (undersegmentation). For these regions, a subsequent segmentation using the watershed method was applied, this allowed us to recover the overlapping nuclei. Furthermore, nuclei adjacent to the edges of the _field-of-view_ were discarded. Each of the resulting regions was dilated, suitably preventing segmentation beneath the nuclei edges. The resulting binary mask served to extract different nuclear features: area, mean intensity, perimeter, center of mass, etc. as well as for assigning the spots to cells.

**Spot identification**

For each fluorescence-channel image stack, non-uniform background was removed, and signal-to-noise ratio was enhanced by applying 3D Laplacian of Gaussian convolution. The optimal size of this filter (corresponding to the width of the Gaussian) depends on the size of the observed particle and was empirically adjusted to maximize the signal of the particles. 

Due to residual uniform noise, further use of a threshold is needed. First the number of spots is calculated as a function of monotonically increasing thresholds, then a single threshold was manually chosen from a normally observed plateau corresponding to a range of thresholds over which the total number of detected spots in the field-of-view does not vary.Thresholds chosen in this plateau yielded spot detections that matched the spots identified by eye (see **Figure 10.**). Finally, the volume, mean intensity and _coarse center position_ (as the center of mass of the intensities in the identified connected component) was determined for individual spots.  

# Results and discussion

---

## Precise spot localization

Once the _coarse center position_ of the spots was determined, we proceeded with the estimation of the precise position of the spots. The 2D image intensity $(x,y)$ profile can be well represented by a 2D Gaussian function (**eq. _(1)_**).

![Dot image](/static/images/slides/chromatin-organization/dot_image.png)
<p class="caption"><strong>Figure 3.</strong> Distribution of image intensities can be approached with Gaussian functions. In the figure, a smoothened surface of fluorescence intensities in 2D, and 2D images of maximum projection across the depth axis for different planes</p>

Based on the eq. _(1)_, the 2D intensity model parameters are obtained to fit the $xy$-plane maximum-projection image intensity distribution in a window of a 6 pixels radius from the calculated coarse position (see **Figure 4-A,C**); $A$ is the maximum intensity, $x$ and $y$ are the center of the 2D Gaussian and $\\sigma_*$ is the width of the spots, additionally we can also estimate the intensity background $b$ for which we later get an average and correct for the whole slide.

\\begin{equation}
	f(x,y) = A \exp\left(- \left(\frac{(x-x_o)^2}{2\sigma_x^2} + \frac{(y-y_o)^2}{2\sigma_y^2} \right)\right) + b
\\end{equation}

After getting the precise $(x,y)$ position, the intensity profile of this position along the z-axis was used to fit the following 1D Gaussian function (**see figure 4B**):

\\begin{equation}
	f(z) = A \exp \left( -\frac{(z-z_o)^2}{2\sigma_z^2}\right)
\\end{equation}
 
Both models are fitted using maximum likelihood estimates. The starting values for the model parameters are determined as follows: $A$ as the maximum intensity value in the spot window, $x$, $y$, $z$ from the coarse center positions, $\sigma$ fixed to 1.5. We assume that the spot is spherical in 3D, thus. $\sigma$ is equally initialized in all dimensions. 

![Gaussian Fit][gaussian_fit]
<p class="caption"><strong>Figure 4.</strong> Precise localization is estimated from parametric fitting of 2D and 1D Gaussian functions for individual spots. <strong>A.</strong> Surface fit from the maximum projection over the <em>xy</em>-plane z-depth intensity profile. <strong>B.</strong> Gaussian fit from the maximum projection over the <em>xz</em>-plane <em>y</em>-depth intensity profile. <strong>C.</strong> Overlay of the resulting Gaussian surface over the image. <strong>D.</strong> Precise spot localization is shown in red while the blue circle shows the estimated spot size with a diameter corresponding to the _FWHM_ (full width half maximum) of the Gaussian function; additionally, position of the same bead in other channels is shown.</p>

[gaussian_fit]: /static/images/slides/chromatin-organization/2D_Gaussian_1D_gaussian.png

As a result, we got new coordinates for the precise spot localization, background corrected intensity distribution, and estimated spot size from the _FWHM_ ([full width half maximum](http://en.wikipedia.org/wiki/Full_width_at_half_maximum)). Additionally we used the _goodness of fit_ to infer for the appearance of multiple spots within one 13px $\times$ 13px window; those occurrences were discarded for subsequent analysis; however, further improvement can be achieved by fitting a mixture of multi-variate Gaussians to estimate the localization of multiple spots within a spot window.

Despite that these measurements enhance the accuracy for the target position estimation, due to time constrains, an estimation of the error and extent of precision was not performed. From previous experience we know that the resolution is within 20 and 30 nm ([Semrau et al. XXX](#SemrauXXX)) , however this might vary across microscope setups. The experiment for the precision assessment would be as follows: Iterative imaging and estimation of the precise spot localization should yield a distribution of $x,y,z$ localization coordinates for which the variance would serve as a measure for resolution.

## Chromatic aberration corrections

The wavelength-dependency of the refraction indexes in optical systems involves _chromatic aberrations_: one object point is not projected on exactly one image point on the sensor plane, but dispersed depending on its wavelength. When precise estimation of the three-dimensional position of a point is necessary —as in HD–FISH experiments— the distortions have to be compensated.

To this end, commercial fluorescent beads where imaged and detected in different channels. For each channel, the acquired image stack of 15 planes in depth was filtered and thresholded to automatically detect the _coarse position_ of the single beads in a 3D space (1024px $\times$ 1024px $\times$ 15 planes). The threshold was set automatically for a reference channel as the intensity value for which the inverse of the coefficient of variation was the highest. The threshold for the remaining channels was selected such that the detected beads was close in number, if not the same, to the number of beads detected on the reference channel. For each channel, the detected coarse positions $(x,y,z)$ where enhanced for precision by fitting Gaussian functions as previously described in [precise spot localization](#precise-spot-localization) section.

**Registration and shift measurement**

Since the corresponding intensity signals of a bead in different channels do not co-localize, first we had to find the signals corresponding to the same single bead. This might be trivial for low density of beads in the _field-of-view_, however it proved to be difficult on high density of beads due to mis-assignment and to other factors as debris or bead movement between channel acquisition rounds. We approached this by assigning correspondences between the selected reference bead and its closest neighboring intensity signal regardless of the channel, under the assumption that the distance between channel signals is minimal, thus, the closest signals should correspond to the same bead. Then we used this information to build an undirected adjacency matrix where an edge was assigned every time we found a neighboring connection between two bead signals. This criteria allowed us to build independent and completely connected graphs called _cliques_, which correspond to single beads (see **Figure 5. Top**). High density of beads allowed to better capture the shift distribution within the _field-of-view_.

![Beads identification][beads_labeled]

[beads_labeled]: /static/images/slides/chromatin-organization/beads_identification.png

![Beads dense][beads_dense]

[beads_dense]: /static/images/slides/chromatin-organization/beads_dense_panels.png

<p class="caption"><strong>Figure 5.</strong> Beads registration. <b>Top:</b> Commercial beads are imaged in different channels, and processed for their exact locations, then assigned to a single bead (<em>registration</em>). <b>A.</b> Fluorescence intensity image of one channel for low density of beads within a <em>field-of-view</em>. <b>B.</b> Labeled beads with it corresponding identified signals in different channels. <b>C.</b> Each registered bead is the result of finding complete connected components (<em>cliques</em>) of degree four (corresponding to the number of imaged channels) in a graph. <b>Bottom: A.</b> Fluorescence intensity image of one channel for high density of beads. <b>B.</b> (detail) From a reference channel, neighboring signals are assigned as potential corresponding fluorescent signals for the same bead (blue edges connecting fluorescent signals, in black). Connections are recorded in an adjacency matrix. <b>C.</b> Bead <em>registration</em> is solved by searching <em>cliques</em> in the adjacency matrix.</p>

With this method we achieved the correct identification of most of the beads; outliers for the distance between signals associated with a single bead were discarded for further analysis. Once the beads where _registered_, the shift $\\Delta$ (extent of _chromatic aberration_) from a reference channel $ref$, was calculated in each direction ($x$,$y$ or $z$) for each bead $i$ in each channel $ch$ as follows:

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

As expected, we observed that the extent of distortions was wavelength dependent, and the shift magnitudes vary for distinct fluorescence channel (**se figure 6**)

![uncorrected](/static/images/slides/chromatin-organization/uncorrected.png)
<p class="caption"><strong>Figure 6.</strong> Once the fluorescence intensity signals are registered, (before correction) the shift $\\Delta$ is measured in each direction $x$, $y$, $z$. For visualization proposes, the shift &mdash; y-axis [px] &mdash; for each channel (A594, Cy5, GFP and TMR) from a reference channel (DAPI) is ploted as a function of a single dimension in one of each three directions ($x$, $y$ and $z$) &mdash; x-axis [px] &mdash;. The magnitude of the shift varies from channel to channel at the different dimensions, showing the wavelength dependency of the <em>chromatic aberration</em>.</p>

**Shift correction model fitting**

To interpolate the shift for the whole volume we selected polynomial functions due to their smoothness, thereby reducing the irregularities due to thermal noise which could still be captured by using other interpolating approaches. Along this line, fifth-order polynomials were fit to the measured shifts (separately for each dimension, see eq. 3). The order of the polynomial was empirically selected such that the residual shift was the least.

\\begin{equation}
	\Delta^{ch}\_{dim}(x,y,z) = a_{n,n,n}x^ny^nz^n + a_{n,,n,n-1}x^ny^nz^{n-1} + a_{n,n-1,n}x^ny^{n-1}z^n + \ldots + a_{1,0,0}x + a_{0,1,0}y + + a_{0,0,1}z + a_{0,0,0}
\\end{equation}

The resulting polynomial functions were at some extent similar for different channels. For both $x$ and $y$ directions, the shift magnitudes were mostly in a lateral gradient, being positive on one extreme, and negative on the other (see **Figure 7.**). Meanwhile, the interpolating function corresponding to the $z$ direction was observed to be focal, with a grater displacement at the outer regions of the _field-of-view_. 

![shiftw](/static/images/slides/chromatin-organization/shoftw.png)
<p class="caption"><strong>Figure 7.</strong> Color plots showing the extent of the shift $\\Delta$ interpolated using polynomial functions. For a single plane at $z = 5$, the shift for different positions at $(x,y,z=5)$ is plotted for different channels (A594, Cy5, GFP and TMR) at the different directions ($x$, $y$ and $z$).</p>

By using fluorescent beads, in this first approach for interpolating the shift, we failed to capture the contribution of the distortion along the $z$ dimension since the totality of the beads were localized at the same z-depth (data not shown). Alternatively, and more optimally, we performed a second experiment where we used _primary human foreskin fibroblasts_ to capture the range in z-depth at which the genomic regions could be localized. To this end, interleaved probes distinctively label were designed to target a single genomic region. To achieve a high density of localizations, after hybridization, the coverslip was imaged by moving the _field-of-view_, thus a single region was imaged at different positions throughout one single focal area and afterwards, shift magnitudes were calculated as described on the previous section. The resulting interpolating functions for all channels in the different directions are shown above on **Figure 7.**. 

![corrected](/static/images/slides/chromatin-organization/corrected.png)
<p class="caption"><strong>Figure 8.</strong> Shift measurements after correction with polynomial functions. The magnitude of the shift is corrected to be less than 1px. Some variation is still observed due to slight variations in movement between acquisition rounds, additionally to the fact that it is a projection and the three-dimensional shift is captured in a single dimension.</p>

![TMR shift][tmr_shift]

[tmr_shift]: /static/images/slides/chromatin-organization/tmr_calibXY.jpg

<p class="caption"><strong>Figure 9.</strong> Overlay of fluorescent beads imaged in different channels, before and after correction.</p>

Our approach resulted in a set of polynomial functions which served to correct the shift for each fluorescent channel, in every direction as a function of its three-dimensional position_ (see **Figure 6.**). A reduction in the shift up to less that 1px was achieved. We observed a better result when correcting for shifts in the planar directions than in the depth direction (see **Figure 8.**). 

One drawback of the correction for _chromatic aberrations_ is that they depend on the experimental setup, where small changes in variables, as are the imaging medium and slight movements of the objective are prone to change the shift pattern, accordingly, the measurement of the shift magnitudes have to be performed on an individual experiment basis, as a consequence, increasing the time and labor required for each image acquisition step.

## SpotterUI

The previously described approaches to the precise localization of genomic regions were integrated into a custom Graphical User Interphase (_SpotterUI_) written in MATLAB (see **Figure 10.**). This semi-automated software includes various features that simplify the identification and estimation of the precise spot localizations from _HD-FISH_ experiments. Automatic and manual segmentation, annotations for single nuclei, and overlayed figure creation are some of the general tools featured in the program. Moreover, quantitative measures like nuclei section area, DAPI average intensity measures, background correction and also measurements for individual spots are estimated. Among the few settings that have to be tuned and specified in a configuration file are the width and size of the filters, number of thresholds for finding the threshold plateau, average nuclei sectional area, voxel size, etc. 

Within the same user interface, the shift-interpolating functions can be generated from images with fiducial probes like fluorescent beads or multi-labeled genomic regions. These polynomial functions are stored in a file which can be later used to batch correct actual experiment spot locations.

<a class="fancybox" rel="hdfish" href="/static/images/slides/chromatin-organization/spotterUI.png" title="4 loci experiment" target="_blank"><img src="/static/images/slides/chromatin-organization/spotterUI.png" style="background-color:#fafafa; border: none;" alt="" /></a>
<p class="caption"><strong>Figure 10.</strong> <em>SpotterUI</em> is a Graphical User Interface that integrates the workflow for the analysis of <em>HD-FISH</em> experiments into a software in a semi-automated manner. Configuration settings are given in a configuration file, while a simple user interface allows for the automatic segmentation and the interactive identification of the spots. Interaction with the <em>regions-of-interest</em> allows for selecting and annotating or deleting single cells, the interaction with single spot also allows to correct for misidentification. Polynomial functions can be re-used for batch correction of several <em>fields-of-view</em> as they are included from MATLAB native data files as an input setting. The workflow returns at the end several quantitative measures including the precise position of the <em>HD-FISH</em> spots for further statistical analysis.</p>

## 4 loci experiment

In a proof of concept experiment, _HD-FISH_ probes were designed to evenly target 4 regions within the chromosome 17 of _HME cells_. _Spotted_ regions were visualized by genomically-equidistant set of fluorescently-labeled probes. Both Alexa594 and Cy5 labeled probes were interleaved with a distance of about 10Mb between each other (see **Figure 11.**).

![4 loci](/static/images/slides/chromatin-organization/4_loci.png)
<p class="caption"><strong>Figure 11.</strong> Proof of concept experiment. Chromosome 17 was simultaneously <em>spotted</em> with 4 interleaved sets of <em>HD-FISH</em> probes targeting genomic regions separated by 10 Mb. We can visually identify separate groups of four spots corresponding to separated homolog chromosomes. This feature was later exploited to automatically cluster single chromosomes.</p>

After hybridization, we acquired 21 _fields-of-view_ comprising a total of 324 nuclei in varying cell-cycle stages (see **Figure 12.**). With the help of the _SpotterUI_ we segmented, identified, corrected, and processed the set of acquired image stacks. 

<a class="fancybox" rel="hdfish" href="/static/images/slides/chromatin-organization/OL_008.png" title="4 loci experiment" target="_blank">
<img src="/static/images/slides/chromatin-organization/OL_008.png" style="background-color:#fafafa; border: none;" alt=""/></a>
<p class="caption"><strong>Figure 12.</strong> Sample overlay of the 4 loci experiment. Image of DAPI in the nuclei (blue) of <em>HME</em> cells and the identified spots in both Cy5 (green) and Alexa594 (magenta).</p>

In most of the nuclei, we can visually identify separate groups of spots from which we assumed they belong to single chromosomes (see **Figure 12.**). To exploit this feature of organization, we first filtered for nuclei in which the total number of spots was 8, corresponding to only 2 copies of the chromosome 17 during interphase. Furthermore we used K-means (k=2) clustering algorithm to group the single copies of chromosome 17. Among all the possible spot configurations within a cluster, we selected for those clusters with 4 spots (2 Cy5 spots and 2 Alexa594 spots, each (see **Figure 13.**). Roughly 33% of the nuclei showed to be in interphase, as we found 107 nuclei with interphase spot counts, and 105 satisfying the further required configuration, thus, yielding 105 spot clusters. On these clusters we proceeded to measure the three different euclidean distances between them: i) distance between Alexa594 spots, ii) distance between Cy5 spots and iii) distance between Alexa594 and Cy5 spots (see **Figure 14.**).


<a class="fancybox" rel="hdfish" href="/static/images/slides/chromatin-organization/4_loci_conf.png" title="k-means clustering" target="_blank"><img src="/static/images/slides/chromatin-organization/4_loci_conf.png" style="background-color:#fff; max-width: 50%;" alt="" /></a>
<p class="caption" style="width: 50%;"><strong>Figure 13.</strong> K-means clustering strategy to identify separate groups of spots corresponding to single chromosomes. First we selected interphase nuclei using the spot counts as an indicator, those with 4 spots on each channel. We performed K-means clustering to identify 2 groups of spots, from all possible grouping configurations we selected those corresponding to a single chromosome, meaning 2 spots per channel.</p>

For a single spot cluster there is a single distance between two probes of the same channel, which corresponds to a distance of 20 Mb. However, for the 4 possible distances separating spots of different channels, we cannot directly identify the physical correspondence to the genomic separation, i.e. distance between a genomic separation of 10 Mb and 30 Mb. We approached the estimation of each distance by fitting a mixture of two Gaussians, where each distribution corresponds to one distance at each genomic separation (see **Figure 14. Bottom right**) under the assumption of normally distributed physical distances.

<a class="fancybox" rel="hdfish" href="/static/images/slides/chromatin-organization/distHIST.png" title="distance histograms" target="_blank"><img src="/static/images/slides/chromatin-organization/distHIST.png" style="background-color:#fff; max-width: 70%;" alt="" /></a>
<p class="caption" style="width: 70%;"><strong>Figure 14.</strong> Histograms showing the distribution of calculated physical distances for varying genomic distances. <b>Top left: </b> All measured pairwise distances between spots. <b>Top right/Bottom left:</b> Distances corresponding to 20 Mb (spots from the same channel). <b>Bottom right:</b> Distribution of physical pairwise distances measured between spots from different channels corresponding to a genomic separation of 10 and 30 Mb approached by mixture of Gaussians.</p>

With this proof of concept experiment we were able to estimate the physical distance for three equidistant genomic regions. Likewise, our results meet the previous observations where the leveling-off of the linear to spatial scaling can already be observed for genomic distances of 10Mb ([Mateos-Langerak et al. 2009](#Mateos-Langerak2009), see **Figure 15.**). As a result, we demonstrate the scope of our methodology to capture the chromosome topology. 

![r](/static/images/slides/chromatin-organization/slide6.png)
<p class="caption"><strong>Figure 15.</strong>Leveling-off of the  linear to spatial scaling in the organization of the genome. In agreement with previous experimental measurements, our results also show the leveling-off of the physical distance for genomic regions separated by more then 10Mb.  This observations support the view of interphase chromatin organizing in globular structures termed <em>chromosome territories</em>.</p>

For the sake of simplicity and to demonstrate the applications of our methodology, we limited our probe set to simply target 4 regions interleaved between two fluorophores. However in follow up experiments we are planning to use combinations of fluoreophores to target and identify individual regions without having to struggle with the fitting mixtures of Gaussians. Moreover we can also decrease the separation between regions up to the Kb resolution, thus having a better quantitative measures for the scaling behavior of the mammalian nucleus.

#Concluding remarks
---
Model ensembles of polymer conformations together with DNA-FISH experimental measures, provide a natural framework for understanding the nature of the emerging link between structure, composition, and function; they also serve as a starting point for understanding cell-to-cell variability in gene expression (Obduzak et al. 2002, Elowitz et al. 2002), (i.e. enhancer-dependent gene activation would be promoted from transient spatial proximity of two genomically distant loci). 

To this end, _HD-FISH_ provides the required scope by capturing variations within chromatin conformations by the measurements in single cells. Our developed methodology and tools allow for the rapid and precise quantification of FISH experiments targeted to the understanding of genome organization. Furthermore, _HD-FISH_ can be coupled with _single molecule RNA-FISH_ to gain more insight into the link between structure and function. 

#Aknowledgements

This project was closely and jointly developed with Magda Bienko &mdash; without her enthusiasm, dedication and experimental dexterity, none of the experiments above could have been realized &mdash;. We would like to further acknowledge Stefan Semrau for fruitful discussion for the correction of the _chromatic aberrations_. Moreover we would like to thank Alexander van Oudenaarden for his support and for sharing space, time and expertise in addition to guidance. Finally we thank the van Odenaarden Lab members which suggestions, small talk, and daily interaction made a great deal of addition to the development of this project.

<!##Some Definitions
* **Structure:** The arrangement of and relations between the parts or elements of something complex.
* **Topology:** The study of geometric properties and spatial relations unaffected by the continuous change of shape or size of figures.
* **Architecture:** The conceptual structure and logical organization of something.>

#References and relevant literature