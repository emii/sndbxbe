Date: 2013-10-26
Title: Image analysis of <em>Organoid</em> primary cell culture
Category: projects
Tags: research, organoid, image processing, HCI
Summary: Analysis and segmentation of tissue culture organoids
Abstract: Primary cell culture of a single LGR5+ cell from the mouse gut is imaged for 48h, segmented and tracked.
References: C:\Users\ozomatliopochtli\Library\Bibtex\Organoid.bib

**Note about figures:** Figures are not displayed. To see the figure please make sure Javascript is enabled, and click on the corresponding link, caption can be unhidden by mouse hover once the image is displayed.

[TOC]

# Introduction
---
Organoids are crypt-villus shaped structures established from long term expansion of self-renewing stems cells from the mouse small-intestine epithelium. In the in-vivo situation for mouse, the small intestine is established from a single layer of cells, and arises from the vigorous proliferation of epithelial tissue around embryonic day 14.5 (E14.5). In later stages, the epithelium is shaped into protrusions (the prospective villi) while cell proliferation is restricted to small compartments which after the third week mature into crypts (E18.5). The native epithelial tissue has a distinctive hierarchical structure where around 15 stem cells reside at the position +4 dividing every 24 hours, other type of cells, the Paneth cells, occupy the positions 1 to 3 from the bottom. Furthermore, stem cells produce rapidly proliferating cells (transit amplifying) which generate 16 to 32 new cell that later stochastically adopt a stem cell fate or differentiate into one mature cell lineage depending on the available space ([Radtke & Clevers 2005](#Radtke2005), [Sato & Clevers 2013](#Sato2013)). Committed cells from neighboring crypts migrate toward one common villus tip, hence, villi origin is said to be polyclonal (Schmidt et al. 1988). In mouse, this tissue is known to have rapid regeneration cycles with a turnover rate of around 5 days where tissue homeostasis is balanced by apoptosis at the tip of the villi. This specific portion of the mouse and also from the human anatomy has been well studied in an effort to understand the process of tissue development and the role of adult stem-cells in regeneration (see <b><a class="fancybox" rel="organoid" data-title-id="caption-1" href="/static/images/organoid/villus-crypt.png" title="click to enlarge">Figure 1</a></b>). 
<div class="img-print"><img src="/static/images/organoid/villus-crypt.png" alt="click to enlarge"/></div>
<div id="caption-1" class="caption-print"><b>Figure 1. Anatomy of the crypt-villus structure in the adult small intestine. </b>Villi are formed from the differentiation (green) and migration of cells proliferating (light blue) in the crypt domain. Cells with stem cell properties (dark blue) reside above Paneth cells (yellow) near the crypt bottom. (image from [Reya & Clevers 2005](#Reya2005))</div>

In recent years, the establishment of advanced culture systems enabling the long term expansion and preservation of the basic physiology of tissues has allowed the isolation of complex 3-dimensional structures like the crypt-villus epithelium. Such an ex-vivo system permits for a more controlled experimental setup while characteristics that resemble the native gut environment are maintained, for example: i) stem-cell hierarchy and self renewal, ii) cell type composition, and iii) multi-domain architecture ([Sato et al. 2009](#Sato2009)). It has been proven that these self-organizing structures arise not only from entire isolated crypts but from single stem cells ([Barker et al. 2007](#Barker2007)). In short, organoids constitute an ideal ex-vivo model for the understanding the key events underlying the tissue development and morphogenesis (see <b><a class="fancybox" rel="organoid" data-title-id="caption-2" href="/static/images/organoid/organoid-growth2.png" title="click to enlarge">Figure 2</a></b>).
<div class="img-print"><img src="/static/images/organoid/organoid-growth2.png"/></div><div id="caption-2" class="caption-print"><b>Figure 2. Organoids basic culture system.</b> **A.** Cells from the mouse crypt are enzymatically segregated and Lgr5$^+$ (fluorescent marker) cells are sorted (FACS) and embedded in _Matrigel_ culture medium containing growth factors: EGF, Noggin, and R-spondin **B.** A single cell grows to initially for a spherical shaped cell layer. Later, the symmetrical shape is broken by the growth of a protrusion. Lgr5$^+$ cells (in yellow) interact with Paneth cells (blue) to initiate the bud formation. (image from [Sato & Clevers 2013](#Sato2013)).</div>

## Developmental phenotypes trough imaging

The process in which a tissue acquires its shape and identity requires knowledge of the dynamical processes in which the behavior of a cell (as a developmental unit) responds to neighboring signals in a controlled manner. Both spatial and temporal events should be recorded to finally achieve an integrated picture of morphogenesis, covering important cues from the single to the tissue level. Both imaging technologies and computational tools currently provide mechanisms in which development up to the single cell resolution can be achieved. 

Relatively new microscopy techniques aiming for live imaging of entire embryos have overcome the limitations of previous imaging methods (as Laser scanning microscopy, LSM). Speed and depth limits are increased as well as photobleaching and phototoxcicity are reduced simply by orthogonal structured illumination and parallel acquisition of entire micrometer thin volumes ([Huisken et al. 2004](#Huizken2004), [Keller et al. 2008](#Keller2008)). The continuous development of platforms based on selective-plane-illumination-microscopy (SPIM), introduced to biology in 2004 ([Huisken et al. 2004](#Huizken2004)) together with fluorescent markers allows the continuous monitoring of the morphogenesis of entire embryos up to several days with minimal disruption.

Great amount of imaging data is generated continuously, likewise algorithms capable of handling that information are improving. The quantitative data analysis of time-lapse recording demands a simple automated, efficient and robust computational solution. While the first efforts for segmentation and tracking of single GFP stained cell-nuclei required more than 4000 cores of computational power ([Keller et al. 2008](#Keller2008)), today's solutions can be boiled down to a single multi-core personal computer ([Kausler et al. 2012](#Kausler2012), [Schiegg et al. 2013](#Schiegg2013)). With the help of these algorithms, a typical 3D + time dataset can thus be segmented, cell identities can be tracked and cell behavior can be systematically analyzed throughout development (see <b><a class="fancybox" rel="organoid" data-title-id="caption-3" href="/static/images/organoid/quantitative-workflow.png" title="click to enlarge">Figure 3</a></b>).
<div class="img-print"><img src="/static/images/organoid/quantitative-workflow.png"/></div>
<div id="caption-3" class="caption-print"><b>Figure 4. Image based study of morphogenesis. </b>**A.** Various kinds of quantitative information can be extracted from time-lapse image data like: **B.** i) Expression from proliferation, cell-death or cell-type specific makers, ii) division events, or iii) spatial arrangements. These measurements are then translated into a description of various biological processes as lineage tree, tissue renewal/proliferation, morphology/shape architecture. **C.** Measurements from multiple experiments can be compared for between each cell. For example, the comparison of mutant vs. the wild-type where measurements above the wild-type mean are in red while measurements below are in blue.  (image from [Moore et al. 2013](#Moore2013)).</div>

Here we employ an updated version of _[ILASTIK](http://ilastik.org)_ &mdash;an interactive learning, segmentation and tracking toolkit&mdash; ([Sommer et al. 2011](#Sommer2011)) to the multidimensional analysis of spinning disc confocal microscopy recordings of the organoid tissue culture (see **FigureX**).

##Motivation

Knowledge acquisition of the mechanical, biochemical and temporal cues of the organoids will provide more insight into the self-organizing principles of development, specially of organogenesis and tissue morphogenesis. The standardization of a pipeline for temporally tracking spatial arrangements of cells while capturing proliferation events will eventually serve as a platform for functional analysis and further ex-vivo experiments in an isolated setup. In the future the analysis could be applied to knock-out/knock-in mouse strains, as well as to assays in which stimulation with a signaling molecule is induced. For example, the morphogenic response to induction of known developmental signaling pathways as Wnt-$\beta$-Catenin, bone morphogenic protein and Notch pathways ([Reya & Clevers 2005](#Reya2005)).

##Objectives

1. Use _ILASTIK_ for tracking fluorescently stained nuclei of the organoid tissue culture.

## System under investigation

In culture, the organoid (100-250 μm in diameter) three dimensional structure arises from single sorted/selected Lgr5$^+$ cells which by multiple division events, self-organize into an ordered crypt-villus domains ([Barker et al. 2007](#Barker2007)).This architecture is compared to the native small intestine epithelium by the formation of analogous domains (see <b><a class="fancybox" rel="organoid" data-title-id="caption-4" href="/static/images/organoid/organoid-structure.png" title="click to enlarge">Figure 4</a></b>). The complexity of the organization not only encompasses the spatial arrangement but also the cell type distribution along space and time.<div class="img-print"><img src="/static/images/organoid/organoid-structure.png" alt="click to enlarge"/></div>
<div id="caption-4" class="caption-print"><b>Figure 3. The organoid. </b> **d.** Lgr5$^+$ cells (green) on the tip of the analogous structures to the mouse small-intestine crypts in a three-dimensional reconstruction of confocal microscopy images. **e.** Schematic representation of the organoid with its analogous domains: the crypt, and the villus-like epithelium facing the internal lumen. (from [Moore et al. 2013](#Moore2013)).</div> 

Organoids were genetically manipulated to incorporate a cassette with _C-terminal tagEGFP-IRES:neo_ flanked by loxP recombination sites, the vector was designed for driving H2A-EGFP fusion and the integration of (neo)mycine resistance marker for selection with G418 ([Schwank et al. 2013](#Schwank2013)). During growth, time-lapse recordings of the organoid fluorescently stained nuclei were performed using a spinning disc microscope.

#Experimetal Approach
---
## Organoid primary culture preparation

_As described in [Sato et al. 2009](#Sato2009) and in [Schwank et al. 2013](#Schwank2013)_, here both culture expansion and imaging were performed by Gerald Schwank

Crypts were released from murine small intestine in PBS/EDTA. Single crypts were mixed and plated in Matrigel(BDBioscience) in 24-well plates. After polymerization, Matrigel was supplemented with crypt culture medium containing growth factors (EGF, R-spondin 1 and Noggin).

Single crypts were cultured for two generations under conditioned medium enriching for stem cells. THe resulting organoids were mechanically dissociated and trypsinized to obtain single cells. Dissociated cells were collected in culture medium and embedded in Matrigel supplemented with growth factors at 1 cell per well (in 96-well plates).

Organoids were directly genetically manipulated by either elctroporation or liposome-mediated transfection. Both methods were used to transfect organoids with the histone H2A-GFP BAC. After two days, stable clones were selected for G814 resistance as well as for ubiquitious expression of H2A-GFP.

## Image acquisition

After selection and conditioned medium removal, sphere-like organoids started to shape into crypt-villus domains. Imaging started 24h upon the first bud event for most of the organoids.

All images were acquired at 40× magnification (high numerical aperture objective) on a confocal PerkinElmer Ultraview VoX spinning disk microscope equipped with a high-resolution charge-coupled device (CCD) camera and controlled by Volocity software.

Each time point (20 minutes interval), we sequentially acquired three-dimensional stacks of fluorescence images for GFP (H2A-EGFP). Our exposure times were roughly 200 ms. The pixel size was 0.32μm, and the spacing between consecutive planes in our stacks was 1.0 μm yielding an anisotropic voxel size. Organoid evolution was followed up to 48 hours.

#Results and discussion
---

## Image analysis

After image acquisition, images were cropped in XY to a bounding box covering the organoid by its totality. Moreover the image stack was further cropped in Z, as depth-dependent intensity and contrast were reduced due to photon scattering and the limited penetration capacity of the confocal system.  

### Segmentation

In our particular case, the main objective was the three dimensional segmentation, hence, to classify each pixel either as foreground (fluorescently labeled nuclei) or as background. For this propose, _ILASTIK_ uses a special kind of decision trees, called random forests. Decision trees are a tool used in machine learning to predict the membership of objects &mdash;in this case pixels&mdash; on a determined class &mdash; in this case foreground or background &mdash;. 

In a tree, a path from the root, to a leaf, represents classification rules learned from categorical dependent variables (i.e.foreground, background) measured from one or more predictor variables (features, like intensity, edge and texture). For our binary partition, measurements of features like intensity, edge and texture descriptors for each class are learned by the manual labeling (brush strokes) of a small set of regions, afterward, a random forest classifier is trained with the input labels (see Figure 5).

Each classification tree in the random forest classifier is built form a bootstrap sample of the training data (sampling with replacement).The prediction for each pixel is then classified given the mode of the collect output of the random forest (100 decision trees).

The features where selected by visual inspection such that each of them reveled or enhanced relevant features which provide informative hints for the segmentation of each class. Likewise, as _ILASTIK_ provides means for interactive learning, the manual classification was fine-tuned until foreground regions resembled in shape that of the nuclei and the regions in between nuclei were classified as background.

For the computation of the features, the parameters for the default algorithm were modified to process anisotropic data. For our voxel size, the settings were adapted to support a scale of 1:1:3 (x:y:z).

From this task we obtained a prediction 

<a class="fancybox" rel="organoid" href="/static/images/organoid/ilastik_main_2.png" title="organoid"><img class="album-item" src="/static/images/organoid/ilastik_main_2.png" style="background-color:#fff; max-width: 210px; margin-left: 5px;" alt="org1" /></a>
<a class="fancybox" rel="organoid" href="/static/images/organoid/ilastik_training.png" title="organoid"><img class="album-item" src="/static/images/organoid/ilastik_training.png" style="background-color:#fff; max-width: 210px; margin-left: 5px;" alt="org1" /></a>
<a class="fancybox" rel="organoid" href="/static/images/organoid/ilastic_predictions.png" title="organoid"><img class="album-item" src="/static/images/organoid/ilastic_predictions.png" style="background-color:#fff; max-width: 210px; margin-left: 5px;" alt="org1" /></a>
<a class="fancybox" rel="organoid" href="/static/images/organoid/ilastik_object_extraction_2.png" title="organoid"><img class="album-item" src="/static/images/organoid/ilastik_object_extraction_2.png" style="background-color:#fff; max-width: 210px; margin-left: 5px;" alt="org1" /></a>
<a class="fancybox" rel="organoid" href="/static/images/organoid/ilastik_cell_class.png" title="organoid"><img class="album-item" src="/static/images/organoid/ilastik_cell_class.png" style="background-color:#fff; max-width: 210px; margin-left: 5px;" alt="org1" /></a>
<p class="caption" style="width: 90%;"><strong>Figure 2. </strong>The organoid segmentation</p>


### Tracking

Tracking means to record the evolution of an object in space and time. Our targets are the cells represented by the fluorescently labeled nuclei. The problem is to find a spatio temporal configuration of cell tracks wich explains better the transitions between frames across the whole time-lapse. Detections (a cell upon assignation across all time steps) is handled simultaneously in an holistic graphical model on which inference is performed globally ([Scheigg et al. 2013](#Schiegg2013)) while object merging is approached with Gaussian mixture models. It is particularly challenging since cell are dividing, additionally, they constantly appear and disappear from the field of view. This variable number of dividing object makes tracking  particularly hard. In _ILASTIK_This problem is approached by probabilistic graphical models which are further restricted to conservation laws for the number of objects in each detection to ensure global consistency of the solution ([Schegg et al. 2013](#Schiegg2013)) 

The method _ILASTIK_ is based in associating to each detected object an assignment variable (tracking by assignment). Thus, the link between objects at t and t+1 overall t yields multiple possible configuration for each object.

As cells might move at with different velocities and/or cells can undergo collective movement, object movement is adjusted in a preprocessing step using patch-wise cross correlation in order to prevent bias towards slow moving objects, additionally tis also accounts for small variations in imaging due to the microscope stage drift.

The model takes into account appearance and disappearance of objects in the segmented image and integrates them in _detection variables_. Both events are penalized with an unary potential calculated with a random forest trained on local features like size of the connected component.

Here we additionally replaced the design parameters for the appearance and disappearance penalty. From the natural observation that objects that are closer to the edge of the _field-of-view_ (FOV) appear and vanish frequently we decided to penalize them softer. We replaced the constant parameters with a function aware of the distance of the objects to the edge after a given margin. The function we used is designed such that it returns values between 0 and 1, thus, we can scale a penalty value as a function of the object distance to the edge. In this case we selected a logistic functions which can be further parametrized (B<sub>o</sub>) and yield a function from a family of curves between a line and a step function (see Figure X).


## Edge-aware appereance/disappereance penalty



## Adapting ILASTIK for anisotropic data

-segmentation features
-cell classification features

## 

Once this was done, b

We proved that Ilastik is capable of segmenting and tracking the organoid dataset, and that the framework implementation can be specifically fine-tuned to meet the requirements of a particular dataset. However further improvements on the time-lapse image acquisition are required to improve the tracking results. Both time-resolution and the possibility of imaging the whole organoid by light sheet microscopy will set  the basis for subsequent quantitative analysis. This approach would make possible the comparison of wild-type vs perturbation experiments, further shedding light into the mechanisms of tissue regeneration and organization.


#Concluding remarks
Both the Chaingraph tracking and the Conservation tracking methods were performed. The task proved to be difficult, as the results were visually assessed and both approaches failed to assign correct trajectories throughout the totality of the time-lapse. Apart that the organoid moves erratically within the field-of-view, we link these misassignments to the fact that the organoid was not imaged as a whole, furthermore, as the contrast decreased along the z-axis, the number of mergers increased. Despite we reduced the number of possible mergers by further cropping the stack, and keeping the high contrast planes, the capacity to prove the consistency of the model was diminished (information was lost). This resulted in some actual cell nuclei were detected as misdetections. To reduce misdetection of actual nuclei and  to improve the tracking, we then tried to fine-tune the algorithm by differently penalizing the appearance and disappearance of cells in/out the field-of-view. We replaced a constant penalty value with a sigmoid function from which steepness parameter can be provided, thus the penalty can be tuned from a smooth to a step function penalty regime. Finally this function was integrated into Ilastik both in the implementation and in the graphical user interface. The implementation of the new penalty regime for dis/appearances reduced the number of actual nuclei to be assigned as misidentifications, which also improved the tracking capabilities for this specific dataset, however further evaluation should be performed as is a time consuming manual tracking.
see [Radke & Clevers 2005](#Radke2005)
#Aknowledgements

<a class="fancybox" rel="organoid" href="/static/images/organoid/tracking-hypotesis.png" title="organoid"><img src="/static/images/organoid/tracking-hypotesis.png" style="background-color:#fff; max-width: 60%; max-height: 400px;" alt="org14" /></a>
<p class="caption" style="width: 60%;"><strong>Figure 2. </strong>Organoid stinings ([Barker et al. 2007](#Barker2007))</p>

<a class="fancybox" rel="organoid" href="/static/images/organoid/image-analysis_workflow.png" title="organoid"><img src="/static/images/organoid/image-analysis_workflow.png" style="background-color:#fff; max-width: 60%; max-height: 400px;" alt="org9" /></a>
<p class="caption" style="width: 60%;"><strong>Figure 2. </strong>Organoid stinings ([Barker et al. 2007](#Barker2007))</p>

<a class="fancybox" rel="organoid" href="/static/images/organoid/edge_penalty.png" title="organoid"><img src="/static/images/organoid/edge_penalty.png" style="background-color:#fff; max-width: 60%; max-height: 400px;" alt="org10" /></a>
<p class="caption" style="width: 60%;"><strong>Figure 2. </strong>Edge Penalty</p>

## Logistic function
\\begin{equation}
f(x) = \frac{1}{1 + e^{-B_{o}x}}
\\end{equation}



**An organoid is the followig:**

<a class="fancybox" rel="organoid" href="/static/images/organoid/organoid_01.gif" title="organoid"><img src="/static/images/organoid/organoid_01.gif" style="background-color:#fff; max-width: 60%;" alt="org11" /></a>
<p class="caption" style="width: 60%;"><strong>Figure 1. </strong>The organoid</p>

**A timelapse segmented organoid looks like this:**

<a class="fancybox" rel="organoid" href="/static/images/organoid/organoid_segmentation.gif" title="organoid"><img src="/static/images/organoid/organoid_segmentation.gif" style="background-color:#fff; max-width: 60%;" alt="org12" /></a>
<p class="caption" style="width: 60%;"><strong>Figure 2. </strong>The organoid segmentation</p>

**Screenshots**










