Title: HD-FISH, a glimpse into chromatin organization_
Date: 2013-06-27
Summary: The written report after finishing my internship at the van Oudenaarden lab about HD-FISH and the data analysis
Category: projects
Tags: biology, research, hd dna-fish, master, report
Abstract: <strong>Abstract:</strong> Chromosomes change their  topology throughout the cell cycle varing its position and degree of compaction. This features have been observed to influence gene expression, as mutations perturbing the overall topology of the nuclear envelope have deleterious effects (see progeria syndrome). Previous methodologies have addressed chomatin conformation in different ways (see Hi-C, Paint probes 3D DNA FISH). However either their resolution is limited or, frquent error rate.

[TOC]

# Introduction

<!First we try to emphasize the idea of chromosome organization by connecting it to gene expression, hence to funciton>

The control of gene expression in eukaryotes can be viewed as the integrated response of mechanisms working at different hierarchical levels. Gene transcription is regulated from the sequence level to chromatin level, to the nuclear level (van Driel et al. 2003) **(see figure 1a)**. At this top-most layer, the higher order topology of the genome has proven to play an important role, as meaningful patterns of organization have been identified; after mitosis, chromosomes decondense into fibers which remain confined into well defined and isolated compartments called _chromosome territories_ (Cremer et al. 2010), gene-poor chromosomes are generally more frequently positioned in the outer regions of the nucleus, whereas gene-rich chromosomes adopt a more internal localization (Croft et al. 1999, **see figure1b**). Moreover, motion of genes along the radial axis of the nucleus has been observed upon gene activation, either toward the nuclear interior or toward the nuclear periphery, being the former not exclusively a repressive location (Andrulis et al. 1998, Boyle et al. 2001, Casolari et al. 2005, Mesiter et al. 2010). Alongside, distributed throughout the nucleus, sets of activated genes are spatially arranged into discrete foci termed _transcription factories_ &mdash;dedicated to the expression of specific combinations of genes, even from distinct chromosomes&mdash; (Spilianakis et al. 2005, Osborne et al. 2007, Schoenfelder et al. 2009 and 2010). This indicates that the associations at the transcriptional hot spots does not happen at random, but genes have preferential partners, commonly in a tissue specific manner (Osborne et al. 2007, **see figure 1c**). In addition, significant changes in spatial organization of genomes are triggered during cellular differentiation reflecting a dramatic change in gene expression (Kim et al. 2004).

![figure 1](/static/images/slides/chromatin-organization/slide1_2.png)
<p class="caption"><strong>Figure 1.</strong> Eschematic illustration of the nucleus with its chromosome territories</p> 

<!Once I make the point of the importance of chromatin organization, I start talking about how is it organized, from structure, and the features that can be abstacted in biophysical models>

The higher-order structure of chromatin offers an extra level of epigenetic regulation. Many factors may be involved in the modulation of nuclear conformations. Both local and long-range biochemical interactions between specific genomic regions, aswell as the anchoring of chromatin domains to the nuclear lamina, shape and constrain the available topologies for the fiber to fold into, emphasizing the link between the linear structure and the spatial chromatin arrangement (Marshall et al. 1997, Chubb et al. 2002, Bickmore & van Steensel 2013).

The overall nuclear structure can be characterized by a set of features that range from spatial compartimentalization, degree of compaction, radial positioning within the nucleus, extent of intermingling, genomic to physical distance scaling, among others. These characteristics, together with the view of the chromatin fiber as an ensamble of _beads-on-a-string_ &mdash;assuming a non-random configuration on the three-dimensional space&mdash; is suitable to be approached with biophysics of polymers, a unifying quantitative framework (Tark-Dame et al. 2011).

Computer simulations from polymer models demonstrate that some features of organization can be reproduced, such as the organization into chromosome territories and the leveling-off of the linear to spatial scaling (Lieberman-aiden et al. XXXX, MAteos-Langerak 2009, Barbieri et al. 2013). However, other model predictions deviate from experimental observations, later providing evidence for additional molecular mechanisms contributing to chromating folding. These particularities can be taken into account by accordingly extending the model. Thus is worht stressing out the importance of better and more extensive experimental techinies to  acqire quantitative data to supply support and adapt theoretical models. 

Recently, the development and refinement of thechniques that allow the mapping of genomic regions onto the spatial context of the nucleus &mdash;both in bulk and up to the single cell level&mdash; has allowed to have quantitative measures to describe the principles of chromatin organization. Methods derivated from 3C (Chromatin Conformation Capture, **see figure 2a**, Dekker et al. 2003) use formaldehyde crosslinking snapshots on the bulk to quantify the distance between two genomic loci, interpreted from contact probabilities; closely localized regions are found to be crosslinked more frequently.

In a more direct strategy, single-cell distance measurements can be acquired from imaging of DNA-FISH (DNA fluorescensce _in situ_ hybridization) experiments, where fluorescently labeled probes are designed to target specific genomic regions whoch are later identified by means of 3D fluorescensce-based microscopy. In a recent advancement, Bienko and collaborators (Bienko et al. 2013) incremented by one order of magnitude the effective target size of DNA-FISH probes up to a resolution close to the difraction limit, allowing the distance measurement to be estimated with higher accuracy. One advantadge of DNA-FISH experiments is that cell-to-cell variability can be captured in a population of fixed cells as snapshots of different chromatin configurations.

One characteristic feature of a polymer model is the mean squared end-to-end distance which scales differently given the dynamics of each polymer representaton. For example in a randomw walk model the physical distance scales monotonically with increasing genomic separation, thus being unable to predict the fact that the physical distance levels-off at larger lenght scales (**see Figure 2.**).


>In FISH experiments, chromatin folding is often measured by the mean-square spatial distance, $\\langle R^{2}\\rangle$, between two genomic regions as a function of their linear genomic distance, $g$, _[...]_ Although the behavior of $\\langle R^{2}\\rangle$ appears to depend on the genomic regions and cell types assessed, in general, at large genomic distances, $\\langle R^{2}\\rangle$ reaches a plateau that reflects the folding of chromosomes into territories. <br><p style="text-align:right">&mdash; <em>Barbieri et al. 2013</em></p> 

![techniques](/static/images/slides/chromatin-organization/slide2.png)
<p class="caption"><strong>Figure 2.</strong> Eschematic illustration of the techniques</p> 

experimental evidence can later be unified and reconciled with polymer models

<!here use info from fudenberg & mirny	gen dev 2012 and from Bickmore and van steensel 2013, and Tark-Dame 2011>

Biophysical models like the fractal and equilibrion model, or the random loop and the recent string and binders switch models require precise measurements of the relationship between the genomic and the physical distance

Both approaches are complementary and bpth provide useful information for the interpretation of the link between 1d and 3d and the integration of the sonceptualization of deistances can be integrated in models that account for the polymer properties of the chromatin fiber which will help us to gain fiurther insight in the organizing principles of the genome.

Both approaches can be reconciled with 

>All polymer models that address chromatin folding assume a linear unbranched polymer that represents the chromatin fibre. Necessarily, such models are coarse-grained in that they do not describe all details of the fibre (Fig. 1). Rather, they assume that polymers are made up of monomer units connected by a flexible connector (Paul et al., 1991). [...] &mdash; Tark-Dame et al. 2011

>ensembles of polymer conformations provide a natural framework for understanding chromatin organization
>ensembles are characterized by various relationships between their observable measures, or scalings, and in- clude: the characteristic size of the whole polymer R(N) (i.e. its root mean squared end-to-end distance hR2
a mean radius of gyration) as a function of its length N, the mean spatial distance between loci (subchain size) R(s) as a function of distance s between these loci along the polymer (genomic distance), and the contact probability between loci P(s)


* Here we propose the refinement of current DNA-FISH techniques and its extension for precise localization of single genomic regions ranging from 3 to 10 Kbp, thus incrmenting the resolution of current comercially available approaches as chromosome painting.  



apparently the current general view of the nuclear organization explained as the sum of all functional features dictating preferential associations then constraining the topologies of the chromatin fiber modeled as a polymer. 

integrates i) the explanation of the folding by polymer models then constrained by biochemical interactions.
 
Finally, as both model and experimental data are integrated, the gain of understandig the nature of the emerging link between structure, composition, and function

Physical distance R can be estimated by FISH, providing the most direct measure for later be reconciled with model prediction. By extensive measurments for different genomic distances 

>As will become clear below, the nonrandom distributionof DNA-sequence features is closely linked to chromatin-domain organization, although it is unknown how the former helps to establish the latter... &mdash; **Bickmore & van Steensel**


FINALLY...thus the organization of the nucleus is a determinant factor of genome funcion and regulation, hence it is important to gain further insight to understand the link between chromatin topology, genome organization, and gene expression.  

Examples of long range interactions: trans activation, enhancer elements

structure:The arrangement of and relations between the parts or elements of something complex.

topology: The study of geometric properties and spatial relations unaffected by the continuous change of shape or size of figures.

architecture: The conceptual structure and logical organization of something

geometric arrangement of chromatin

architecture, topological features, structure, arrangement, etc

Chomatin is arranged in chomosomal domains, gloular regions where a chomosome is positioned and isolated from other chromosomal domains, and are thought to limit the interaction between different chomosomes.

Although the relative positioning between chromosomes might be cell-type specific, the degree at which chromosomes interact with one another stills to be assessed. Models for the chromatin conformation during interphase predict a higher frequency of intermingling than it is observed with the current methodologies. 

<!After talking about the chromatin structure I would start talking about the current methods to study it, a brief intro to C3 and DNA FISH>

Two main approaches are used to stablish the relationship between the genomic distance with the physical distance, the firts is the 3C and its variants, and the second is DNA FISH. The first one tell us about the average configuration of molecules, the conformation that is more prevalent among others so to say the prevalence of one configuration indicates that this process is non-random

Chromatin is formed by interactions between dna and proteins, this might hold together specific regions ether for long time or just transiently which might be or not sequence specific.

<!then I will introduce a bit of the polymer models to approach and answer physical properties of chromatin structure>

chromatin can be described at diferent levels, starting from the beads on a string model of the dna helix rapped around the nucleosome; the arrangment of nucleosomes together in either a 10nm or a 30 nm fiber, into a chromosome territory or into a tightly packed mitotic chromosome. It is for the higher order structures for which we know the less.



The geometric arrangement of chromatin fibers is conceptualized as an arrangement of nucleosomes in different configuration of compaction, from the 10 nm fiber offering a 1000 fold compaction to the classical 30 nm fiber offering a 10000 fold compaction. This is highly dynamic and varies throughout the cell cycle. Having a relatively stable period during interphase?

>with the beads-on-a-string organization of nucleosomes and linker DNA constituting the primary structure, and arrangements resulting from interactions between nucleosomes giving rise to secondary structures

<!Then i will finish with a summary, sort of a motivation >

## Motivation

Currently, the chromosome is viewed as an organelle consisting of non-random, differentially and tissue specific positioned arrangement of chromosomes into functionally distinct sub-domains called chromosome territories (Cremer et al. 2006). The spatial context of a gene within the nucleus as well as within a chromosome appears to have an important role on transcriptional control.Various cell-types may possess different chromatin arrangements accounting for variability in multicellular organisms, The impact of higher order nuclear architecture on these patterns in yet unknown.()

<!Finishing with the especific objectives.>

## Objectives

chromatin organization requires a comprehensive measurement of the landscape of interacting genomic regions.

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

#References