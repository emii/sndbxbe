Title: HD-FISH, a glimpse into chromatin organization_
Date: 2013-06-27
Summary: The written report after finishing my internship at the van Oudenaarden lab about HD-FISH and the data analysis
Category: projects
References: contents/bibtex/dna-fish.bib
Tags: biology, research, hd dna-fish, master, report
Abstract: <strong>Abstract:</strong> Chromosomes change their  topology throughout the cell cycle varing its position and degree of compaction. This features have been observed to influence gene expression, as mutations perturbing the overall topology of the nuclear envelope have deleterious effects (see progeria syndrome). Previous methodologies have addressed chomatin conformation in different ways (see Hi-C, Paint probes 3D DNA FISH). However either their resolution is limited or, frquent error rate.

[TOC]

# Introduction

<!First we try to emphasize the idea of chromosome organization by connecting it to gene expression, hence to funciton>

The control of gene expression in eukaryotes can be viewed as the integrated response of mechanisms working at different hierarchical levels. Gene transcription is regulated from the sequence level to chromatin level, to the nuclear level ([van Driel et al. 2003](#VanDriel2003)) (see figure 1a). At this top-most layer, the higher order topology of the genome has proven to play an important role, as meaningful patterns of organization have been identified; after mitosis, chromosomes decondense into fibers which remain confined into well defined and isolated compartments called _chromosome territories_ (Cremer et al. 2010), generally gene-poor chromosomes are more frequently positioned in the outer regions of the nucleus, whereas gene-rich chromosomes adopt a more internal localization (Croft et al. 1999, **see figure1b**). Moreover, motion of genes along the radial axis of the nucleus has been observed upon gene activation, either toward the nuclear interior or toward the nuclear periphery, being the former not exclusively a repressive location (Andrulis et al. 1998, Boyle et al. 2001, Casolari et al. 2005, Mesiter et al. 2010). Alongside, distributed throughout the nucleus, sets of activated genes are spatially arranged into discrete foci termed _transcription factories_ &mdash;dedicated to the expression of specific combinations of genes, even from distinct chromosomes&mdash; (Spilianakis et al. 2005, Osborne et al. 2007, Schoenfelder et al. 2009 and 2010). This indicates that the associations at the transcriptional hot spots does not happen at random, but genes have preferential partners, commonly in a tissue specific manner (Osborne et al. 2007, **see figure 1c**). In addition, significant changes in spatial organization of genomes are triggered during cellular differentiation reflecting a dramatic change in gene expression (Kim et al. 2004).

![figure 1][fig1]
[fig1]: /static/images/slides/chromatin-organization/slide1_2.png
<p class="caption"><strong>Figure 1.</strong> Eschematic illustration of the nucleus with its chromosome territories</p> 

<!Once I make the point of the importance of chromatin organization, I start talking about how is it organized, from structure, and the features that can be abstacted into biophysical models>

The higher-order structure of chromatin offers an extra level of epigenetic regulation. Many factors may be involved in the modulation of nuclear conformations. Both local and long-range biochemical interactions between specific genomic regions, aswell as the anchoring of chromatin domains to the nuclear lamina, shape and constrain the available topologies for the fiber to fold into, emphasizing the link between the linear structure and the spatial chromatin arrangement (Marshall et al. 1997, Chubb et al. 2002, Bickmore & van Steensel 2013).

## Theoretical approaches to chromatin organization

<!then I will introduce a bit of the polymer models to approach and answer physical properties of chromatin structure>

The overall nuclear structure can be characterized by a set of features that range from cell cycle satge, spatial compartimentalization, degree of compaction, radial positioning within the nucleus, extent of intermingling, genomic to physical distance scaling, among others. These characteristics, together with the view of the chromatin fiber as an ensamble of nucleosomes &mdash;assuming a non-random spatial configuration &mdash; are suitable to be approached with polymer models, a unifying quantitative framework ([Tark-Dame et al. 2011](#Tark-Dame2011)). These models represent chromosome fibers made up of monomer units connected by a flexible connector, this _beads-on-a-string_ representation is coarse-grained at the three-dimensional level, where descriptions for the small scale details are eliminated in favor of the overall structure ([Heermann et al. 2012](#Heermann2012)).

Computer simulations from polymer models demonstrate that some features of organization can be reproduced, such as the organization into chromosome territories ([Lieberman-Aiden et al. 2009](#Lieberman-Aiden2009a)). However, other model predictions deviate from experimental observations (as the leveling-off of the linear to spatial scaling or the different scaling regimes at varing genomic lengths), later providing evidence for additional molecular mechanisms contributing to chromating folding. These particularities can be taken into account by accordingly extending the model assumptions.

<! here I emphasize the concept of scailing and then itroduce experimental approaches to quantify the distance, then remark fish as better since it also captures cell-to-cell variability, esential to bed-hedging or diferences in gene expression?>

One characteristic feature of a polymer model is the mean-squared spatial end-to-end distance $\\langle R^{2}\\rangle$ which as a function of its genomic distance $g$ scales $\\langle R^{2}\\rangle \\sim g^{2\\nu}$, the exponent $\\nu$ varies given the dynamics of each polymer representation, such as random walk, self-avoiding walk, or globular state ([Tark-Dame et al. 2012](#Tark-dame2012)); $R$ is the spatial distance between two genomic regions linearly separated by $g$ (**see Figure 2a.**). For example, in the most simple random-walk model, the physical distance scales monotonically with increasing genomic separation, thus, this model is unable to predict any of the observed nuclear patterns of organization (**see Figure 2b.**). More recent polymer models already started to integrate further improvements to extend rather basic models as are the _swollen coil_ or the _equilibrium globule_ (**see Figure 2c.**). Models like the _fractal globule_ ([Lieberman-Aiden et al. 2009](#Lieberman-Aiden2009a)), the _random loop_ model ([Mateos-Langerak et al. 2009](#Mateos-Langerak2009)), and the recent _string and binders switch_ model ([Barbieri et al. 2013](#Barbieri2012)) are able to reproduce different aspects of the observed nuclear organization. 

To be tested for prediction accuracy, all these approximations require precise measurements of the relationship between the genomic and the physical distance. Thus, it is worth stressing out the importance of better and more extensive experimental techniques to acquire quantitative data to supply support and to adapt the previosly mentioned theoretical representations.

<!After talking about the chromatin structure I would start talking about the current methods to study it, a brief intro to C3 and DNA FISH>

## Experimental techniques capturing chromatin structure

Recently, the development and refinement of techniques that allow the mapping of genomic regions onto the spatial context of the nucleus &mdash;both in bulk and up to the single cell level&mdash; has allowed to have quantitative measures to describe the principles of chromatin organization. High-coverage methods derived from 3C (Chromatin Conformation Capture, Dekker et al. 2003) use formaldehyde crosslinking snapshots on the bulk to quantify distance between genomic loci, interpreted from contact probabilities; closely localized regions are found to be crosslinked more frequently.

In a more direct strategy, single-cell distance measurements can be acquired from the imaging of DNA-FISH experiments (DNA fluorescensce _in situ_ hybridization), where fluorescently labeled probes are designed to target specific genomic loci. Their positions are identified by means of 3D fluorescensce-based microscopy, and subsequently, the distances between loci are measured (**see Figure 2 bottom panel.**). 

Both approaches are complementary, and both provide useful information in terms of nuclear topology which can be unified and reconciled with theoretical models. One advantadge of DNA-FISH experiments is that cell-to-cell variability can be captured in a population of fixed cells as snapshots of different chromatin configurations crucial for characterizing the differences in chromosomal conformations and locations. 

![techniques](/static/images/slides/chromatin-organization/slide2.png)
<p class="caption"><strong>Figure 2.</strong> In FISH experiments, chromatin folding is often measured by the mean-square spatial distance, $\\langle R^{2}\\rangle$, between two genomic regions as a function of their linear genomic distance, $g$, _[...]_ Although the behavior of $\\langle R^{2}\\rangle$ appears to depend on the genomic regions and cell types assessed, in general, at large genomic distances, $\\langle R^{2}\\rangle$ reaches a plateau that reflects the folding of chromosomes into territories. &mdash; Barbieri et al. 2013</p>

<!here use info from fudenberg & mirny	gen dev 2012 and from Bickmore and van steensel 2013, and Tark-Dame 2011>

<!Then i will finish with a short summary, sort of a motivation >

## Motivation

Model ensembles of polymer conformations together with DNA-FISH experimental measues, provide a natural framework for understanding the nature of the emerging link between structure, composition, and function; they also serve as a starting point for understanding cell-to-cell variability in gene expression (Obduzak et al. 2002, Elowitz et al. 2002), (i.e. enhancer-dependent gene activation would be promoted from transient spatial proximity of two genomically distant loci). To this end, DNA-FISH provides the required scope by capturing variations within chromatin conformations by the measurments in single cells.

In a recent advancement, named _HD-FISH_, Bienko and collaborators (Bienko et al. 2013) reduced by one order of magnitude the effective target size of DNA-FISH probes for an increase in resolution close to the difraction limit, this _"spotting"_ strategy allows the position localization to be estimated with higher accuracy. 

Here we propose the refinement of the current 3D DNA-FISH techniques and its extension by Bienko and collaboratiors with the accurate localization of single genomic regions up to the sub-pixel resolution. This comprehensive measurements of the landscape of interacting genomic regions  will further help us to gain deeper insight into the heterogeniety and functional organizing principles of the genome.

<!Finishing with the especific objectives.>

## Objectives

The main objective of this study was to use images generated from _HD-FISH_ experiments to precisely mesaure the distance between various genomically separated loci up to the sub-pixel resolution. More specifically:

1. Generate a data analysis pipeline in MATLAB for feature localization and image processing of _HD-FISH_ experiments
1. Once the coarse localization of the  loci is identified, the effect of chromatic aberration should be corrected and the precise localization of the loci should be estimated
1. Distances are then calculated from corrected loci positions

<!System under investigation is a section which would describe the problem you want to resolve in the context of the experimenyal setup  or the especific experimental subject, in this case it would be the type of tissue and why is it this specific model selected, meaning advantages or special features and limitations>

## System under investigation

DNA has to be optimally folded to fit in the reduced volume of the nucleus conserving functional three-dimensional structure. This arrangement of chromosomes shows to be highly dynamic, changes arrangement throughout the cell cycle but despite the variability in organization among cells, chromatin  preserves common spatial patterns at some layers of organization. The chromosomes change from a highly condensed structures during mitosis, to form the more or less condensed _chromosome territories_ during interphase.

Here we approached the distribution of distances between genomic regions during interphase regardless of the cell type, thus obviating tissue specific differences.

For a population of cells we performed _HD-FISH_, image acquisition of several _fields-of-view_ and carried out image and statistical data analysis.

#Experimetal Approach

## Cell culture and fluorescence in situ hybridization.

We grew both _human mammary ephitelial cells_ (hTERT-HME1 mammary) and _primary human foreskin fibroblasts_ (ATCC CRL 2097) in Dulbecco's modified Eagle's medium with Glutamax (DMEM, Life Technologies) supplemented with penicillin/streptomycin and 10% FBS. To fix the cells, we followed the protocol of [Raj et al. 2008](#Raj2008). We fixed the cells for 10 min at room temperature using 4% formaldehyde/10% formalin in 1× phosphate buffered saline solution (PBS) and followed the fixation by two rinses in 1× PBS, after which we permeabilized the cells with 70% EtOH and stored them at 4 °C overnight.

The _HD-FISH_ probes sets used here were generated by real-time PCR reactions from genomic DNA with primers designed as previously described  by [Bienko et al. 2013](#Bienko2013), delimiting amplicons of length 200–220 nucleotides. The resulting  total of 50 to 80 unique fragments per region were subsequently labeled with the fluorophore of interest with the _Universal Linkage System_.

To perform DNA-FISH, 20 ng of _HD-FISH_ probe were ethanol precipitated using 20 µg of glycogen as carrier and dissolved in 20 µl of 1.7× SSC, 70% formamide, 50 mM Na<sub>2</sub>HPO<sub>4</sub>/NaH<sub>2</sub>PO<sub>4</sub>, 10% dextran sulfate and 5× Denhardt’s solution, pH 7.5. The three-dimensional _HD-FISH_ procedure on nuclei was adapted from [Solovei et al. 2010](#Solovei2010) preserving the three-dimensional nuclear structure. After hibridization, cover glasses were washed twice at 30 °C for 30 min in wash buffer, additionally 20 ng/ml DAPI were added to the second wash. After washes, the cover glasses were rinsed with 2× SSC.

For microscopy, samples were covered with a mounting solution containing 2× SSC buffer, 10 mM Tris, 0.4% glucose, 100 µg/ml catalase, 37 µg/ml glucose oxidase and 2 mM Trolox.

##Image acquisition

All images were acquired at 100× magnification (oil immersion, high numerical aperture Nikon objective) on an inverted epi-fluorescence microscope (Nikon) equipped with a high-resolution charge-coupled device (CCD) camera (Pixis, Princeton Instruments) and controlled by MetaMorph software.

We sequentially acquired three-dimensional stacks of fluorescence images in four different fluorescence channels using filter sets for DAPI, TMR, Cy5, and Alexa 594. Our exposure times were roughly 2–3 s for most of the dyes except for DAPI (which we exposed for ~100 ms). The pixel size was 0.125μm, and the spacing between consecutive planes in our stacks was 0.25 μm.

##Image analysis

Custom MATLAB software was implemented for the serial semi-automated identification of _HD-FISH_ fluorescent spots (see [Results and discussion](#results-and-discussion)), the general pipeline included the below described steps.

**Nuclei segmentation**

Using DAPI staining fluorecence signal, two criteria were used for segmentation. First the nuclei were segmented using Otsu´s method for finding the optimal threshold which minimizes the intra-class variance for intensity pixel values (under the assumption of a bimodal distribution), resulting in a binnary image were most of the nuclei were correctly segmented (**see figure 3**). Following this step, a second criterium was taken into account for regions with an area above the average nuclei area (undersegmentation). For these regions, a subsequent segmentation using the watershed method was applyied, thus recovering the nuclei close to each other. Furthermore, nuclei adjacent to the edges of the _field-of-view_ were discarded. Each of the resulting regions was dilated, thus preventing segmentation beneath the nuclei edges. The resulting binnary mask served to extract different nuclear features: area, mean intensity, perimeter, center of mass, etc.

**Spot identification**

Non-uniform background was removed, and signal-to-noise ratio was enhanced by applying 3D Laplacian of Gaussian convolution. The optimal size of this filter (corresponding to the width of the Gaussian) depends on the size of the observed particle and was empirically adjusted to maximize the signal of the particles. 

Due to recidual uniform noise, further use of a threshold is needed. First the number of spots is calculated as a function of monotonically increasing thresholds, then a single threshold is manually chosen from a normally observed plateau corresponding to a range of thresholds over which the total number of detected spots in the field-of-view does not vary.Thresholds chosen in this plateau yielded spot detections that matched the spots identified by eye (**see figure 3b**). Finally, the volume, mean intensity and _coarse position_ was determined for single spots.  

#Results and discussion

**Spotter UI**

A pipeline and Graphical User Interface (GUI) which help to analyze multi-channel fluorescence microscopy images. The aim of this work is to assess chromosomal organization by High-resolution DNA fluorescence in situ hybridization (HD-DNA FISH). Using a fluorescence microscope Magda acquired about XXX from both 3F3 human fibroblasts and Human Mammary Epithelial cells (HME). Both, chromosomes 1 and 17 were visualized by genomically-equidistant set of fluorescently-labeld DNA-FISH probes. In this study a GUI was developed to analyze the generated three-channel 3D microscopy images to extract information about position and colocalization of the spotter chromosomal regions.


_HD-FISH_ slides where imaged and the probes' spots detected in different channels. For each channel, the acquired image stack of 15 planes in depth was filtered and thresholded to automatically detect the coarse position of the single beads in a 3D space (1024px × 1024px × 15 planes). The threshold was set automatically for a reference channel as the intensity value for which the inverse of the coefficient of variation was the highest. The threshold for the remaining channels was selected for the detected beads to be close if not the same in number to the ones detected on the reference channel. For each channel, the detected coarse positions (x,y) where enhanced for precision by fitting a 2D Gaussian function to the original image intensity distribution in a window of a 6px radius from the calculated coarse position. For the z coordinate position, the intensity profile along the z-depth was calculated in the (x,y) coordinates previously calculated, then, a 1D Gaussian function was fitted, and the

<img src="/static/images/slides/chromatin-organization/spotterUI.png" style="background-color:#fafafa; border: none;">
<p class="caption"><strong>Figure 3.</strong> SpotterUI GUI</p>


* The one loci multi FOV experiment
	* coarse localization
	* precise spot localizationgaussian fitting
	All Gaussian para- meters were obtained by maximum likelihood estimation. Three
	* shift correction
		2D approach
		3D approach
* 4 loci experiment
We simultaneously targeted multiple loci separated evenly on chromosomes 1 and 17 using probes labeled with two alternating fluoreophores
	* application of the pipeline and correction and everythign
	* clustering and data analysis

#Concluding remarks

#Aknowledgements

##Some Definitions

* **Structure:** The arrangement of and relations between the parts or elements of something complex.
* **Topology:** The study of geometric properties and spatial relations unaffected by the continuous change of shape or size of figures.
* **Architecture:** The conceptual structure and logical organization of something.

#References