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

The overall nuclear structure can be characterized by a set of features that range from spatial compartimentalization, degree of compaction, radial positioning within the nucleus, extent of intermingling, genomic to physical distance scaling, among others. These characteristics, together with the view of the chromatin fiber as an ensamble of nucleosomes &mdash;assuming a non-random spatial configuration &mdash; are suitable to be approached with polymer models, a unifying quantitative framework ([Tark-Dame et al. 2011](#Tark-Dame2011)). These models represent chromosome fibers made up of monomer units connected by a flexible connector, this _beads-on-a-string_ representation is coarse-grained at the three-dimensional level, where descriptions for the small scale details are eliminated in favor of the overall structure ([Heermann et al. 2012](#Heermann2012)).

Computer simulations from polymer models demonstrate that some features of organization can be reproduced, such as the organization into chromosome territories ([Lieberman-Aiden et al. 2009](#Lieberman-Aiden2009a)). However, other model predictions deviate from experimental observations (as the leveling-off of the linear to spatial scaling or the different scaling regimes at varing genomic lengths), later providing evidence for additional molecular mechanisms contributing to chromating folding. These particularities can be taken into account by accordingly extending the model assumptions.

<! here I emphasize the concept of scailing and then itroduce experimental approaches to quantify the distance, then remark fish as better since it also captures cell-to-cell variability, esential to bed-hedging or diferences in gene expression?>

One characteristic feature of a polymer model is the mean-squared spatial end-to-end distance $\\langle R^{2}\\rangle$ which as a function of its genomic distance $g$ scales $\\langle R^{2}\\rangle \\sim g^{2\\nu}$, the exponent $\\nu$ varies given the dynamics of each polymer representation, such as random walk, self-avoiding walk, or globular state ([Tark-Dame et al. 2012](#Tark-dame2012)); $R$ is the spatial distance between two genomic regions linearly separated by $g$ (**see Figure 2a.**). For example, in the most simple random-walk model, the physical distance scales monotonically with increasing genomic separation, thus, this model is unable to predict any of the observed nuclear patterns of organization (**see Figure 2b.**). More recent polymer models already started to integrate further improvements to extend rather basic models as are the _swollen coil_ or the _equilibrium globule_ (**see Figure 2c.**). Models like the _fractal globule_ ([Lieberman-Aiden et al. 2009](#Lieberman-Aiden2009a)), the _random loop_ model ([Mateos-Langerak et al. 2009](#Mateos-Langerak2009)), and the recent _string and binders switch_ model ([Barbieri et al. 2013](#Barbieri2012)) are able to reproduce different aspects of the observed nuclear organization. 

To be tested for prediction accuracy, all these approximations require precise measurements of the relationship between the genomic and the physical distance. Thus, it is worth stressing out the importance of better and more extensive experimental techniques to acquire quantitative data to supply support and to adapt the previosly mentioned theoretical representations.

<!After talking about the chromatin structure I would start talking about the current methods to study it, a brief intro to C3 and DNA FISH>

## Experimental techniques capturing chromatin structure

Recently, the development and refinement of techniques that allow the mapping of genomic regions onto the spatial context of the nucleus &mdash;both in bulk and up to the single cell level&mdash; has allowed to have quantitative measures to describe the principles of chromatin organization. High-coverage methods derivated from 3C (Chromatin Conformation Capture, Dekker et al. 2003) use formaldehyde crosslinking snapshots on the bulk to quantify distance between genomic loci, interpreted from contact probabilities; closely localized regions are found to be crosslinked more frequently.

In a more direct strategy, single-cell distance measurements can be acquired from the imaging of DNA-FISH experiments (DNA fluorescensce _in situ_ hybridization), where fluorescently labeled probes are designed to target specific genomic loci. Their positions are identified by means of 3D fluorescensce-based microscopy, and subsequently, the distances between loci are measured (**see Figure 2 bottom panel.**). 

Both approaches are complementary, and both provide useful information in terms of nuclear topology which can be unified and reconciled with theoretical models. One advantadge of DNA-FISH experiments is that cell-to-cell variability can be captured in a population of fixed cells as snapshots of different chromatin configurations crucial for characterizing the differences in chromosomal conformations and locations. 

![techniques](/static/images/slides/chromatin-organization/slide2.png)
<p class="caption"><strong>Figure 2.</strong> In FISH experiments, chromatin folding is often measured by the mean-square spatial distance, $\\langle R^{2}\\rangle$, between two genomic regions as a function of their linear genomic distance, $g$, _[...]_ Although the behavior of $\\langle R^{2}\\rangle$ appears to depend on the genomic regions and cell types assessed, in general, at large genomic distances, $\\langle R^{2}\\rangle$ reaches a plateau that reflects the folding of chromosomes into territories. &mdash; Barbieri et al. 2013</p>

<!here use info from fudenberg & mirny	gen dev 2012 and from Bickmore and van steensel 2013, and Tark-Dame 2011>

<!Then i will finish with a short summary, sort of a motivation >

## Motivation

Model ensembles of polymer conformations together with DNA-FISH experimental measues, provide a natural framework for understanding the nature of the emerging link between structure, composition, and function; they also serve as a starting point for understanding cell-to-cell variability in gene expression (Obduzak et al. 2002, Elowitz et al. 2002), (i.e. enhancer-dependent gene activation would be promoted from transient spatial proximity of two genomically distant loci). To this end, DNA-FISH provides the required scope by capturing variations within chromatin conformations by the measurments in single cells.

In a recent advancement, Bienko and collaborators (Bienko et al. 2013) incremented by one order of magnitude the effective target size of DNA-FISH probes up to a resolution close to the difraction limit, allowing the distance measurement to be estimated with higher accuracy. 

Here we propose the refinement of the current high-resolution DNA-FISH techniques and its extension by Bienko and collaboratiors with the accurate localization of single genomic regions up to the sub-pixel resolution. This comprehensive measurements of the landscape of interacting genomic regions  will further help us to gain deeper insight into the heterogeniety and functional organizing principles of the genome.

<!Finishing with the especific objectives.>

## Objectives

* main objective
	* alternate objective no 1
	* alternate objective no 2

##System under investigation

#Experimetal Approach

##Experimental model 

#Methodology

##Image acquisition

##Image analysis

###Nuclei segmentation

Using DAPI staining fluorecence signal, two criteria were used for segmentation. First the nuclei were segmented using a otsu´s method for tfinding the optimal hreshold which minimizes the intra-class variance for intensity pixel values (under the assumption of a bimodal distribution), resulting in a binnary image were most of the nuclei were correctly segmented. Following this step, a second  criteria was taken into account for regions with an area above the average nuclei area (close nuclei segmented as one) covering more than one nuclei,for these regions, a subsequent segmentation using the watershed method was applyied, thus recovering the nuclei close to each other. Furthermore, nuclei adjacent to the edges of the field-of-view were discarded. Each of the resulting regions was dilated, thus preventing segmentation beneath the nuclei edges. The resulting binnary mask served to extract the following nuclei features: area, mean intensity, perimeter. This binary mask provided the 

#Results and discussion

#Concluding remarks

##Some Definitions

* **Structure:** The arrangement of and relations between the parts or elements of something complex.
* **Topology:** The study of geometric properties and spatial relations unaffected by the continuous change of shape or size of figures.
* **Architecture:** The conceptual structure and logical organization of something.

#References