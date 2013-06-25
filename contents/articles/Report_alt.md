Title: HD-FISH, a glimpse into chromatin organization (alt)
Date: 2013-03-29
Summary: The written report after finishing my internship at the van Oudenaarden lab about HD-FISH and the data analysis
Category: projects
Tags: biology, research, hd dna-fish, master, report
Abstract: Abstract (placeholder) Chromosomes change their  topology throughout the cell cycle varing its position and degree of compaction. This features have been observed to influence gene expression, as mutations perturbing the overall topology of the nuclear envelope have deleterious effects (see progeria syndrome). Previous methodologies have addressed chomatin conformation in different ways (see Hi-C, Paint probes 3D DNA FISH). However either their resolution is limited or, frquent error rate.

[TOC]

# Introduction 

The control of gene expression in eukaryotes can be viewed as the integrated response of mechanisms working at different hierarchical levels. Gene transcription is regulated from the sequence level to chromatin level, to the nuclear level (van Driel et al. 2003). At this top-most layer, the higher order topology of the genome in the nucleus has proven to play an important role, as meaningful patterns of organization have been identified; gene-poor chromosomes are generally more frequently positioned in the outer regions of the nucleus, whereas gene-rich chromosomes adopt a more internal localization (Croft et al. 1999). Moreover, motion of genes along the radial axis of the nucleus have been observed upon gene activation, either toward the nuclear interior or toward the nuclear periphery being the former not exclusively a repressive location (Andrulis et al. 1998, Boyle et al. 2001, Casolari et al. 2005, Mesiter et al. 2010). Alongside, distributed throughout the nucleus, sets of activated genes are spatially arranged into discrete foci called transcription factories dedicated to the expression of specific combinations of genes even from distinct chromosomes (Spilianakis et al. 2005, Osborne et al. 2007, Schoenfelder et al. 2009 and 2010). This indicates that the associations at the transcriptional hot spots does not happen at random, but genes have preferential partners, commonly in a tissue specific manner. In addition, significant changes in spatial organization of genomes are triggered during cellular differentiation reflecting a dramatic change in gene expression (Kim et al. 2004).

Currently the chromosome is viewed as an organelle consisting of non-random, differentially and tissue specific positioned arrangement of chromosomes into functionally distinct sub-domains called chromosome territories (Cremer et al. 2006). The spatial context of a gene within the nucleus as well as within a chromosome appears to have an important role on transcriptional control.Various cell-types may possess different chromatin arrangements accounting for variability in multicellular organisms, The impact of higher order nuclear architecture on these patterns in yet unknown.()

chromatin organization requires a comprehensive measurement of the landscape of interacting genomic regions.

# Plagio:

chromatin organization is linked to function, gene expression, can be divided in euchromartin and heterochromatin , gene-rich (internally )and gene-poor (envelope associated) regions, actively transcribed and inactive regions respectively, chromosome territory which is not randomly positioned and might be cell-type specific

Chromatin is formed by interactions between dna and proteins, this might hold together specific regions ether for long time or just transiently which might be or not sequence specific.

chromatin can be described at diferent levels, starting from the beads on a string model of the dna helix rapped around the nucleosome; the arrangment of nucleosomes together in either a 10nm or a 30 nm fiber, into a chromosome territory or into a tightly packed mitotic chromosome. It is for the higher order structures for which we know the less.

Two main approaches are used to stablish the relationship between the genomic distance with the physical distance, the firts is the 3C and its variants, and the second is DNA FISH. The first one tell us about the average configuration of molecules, the conformation that is more prevalent among others so to say the prevalence of one configuration indicates that this process is non-random

Examples of long range interactions: trans activation, enhancer elements

The geometric arrangement of chromatin fibers is conceptualized as an arrangement of nucleosomes in different configuration of compaction, from the 10 nm fiber offering a 1000 fold compaction to the classical 30 nm fiber offering a 10000 fold compaction. This is highly dynamic and varies throughout the cell cycle. Having a relatively stable period during interphase?

The current view of the dynamics of chromatin organization holds that after mitosis, the chromosomes decondense into fibers which remain confined into chromosome territories during G0 or G1 interphase (G1,S,G2) G1 is characterized by growth, increase in volume

structure:The arrangement of and relations between the parts or elements of something complex.

topology: The study of geometric properties and spatial relations unaffected by the continuous change of shape or size of figures.

architecture: The conceptual structure and logical organization of something

geometric arrangement of chromatin

architecture, topological features, structure, arrangement, etc

Chomatin is arranged in chomosomal domains, gloular regions where a chomosome is positioned and isolated from other chromosomal domains, and are thought to limit the interaction between different chomosomes.

Chromatin architecture offers an extra level of epigenetic regulatory mechanism.
Although the relative positioning between chromosomes might be cell-type specific, the degree at which chromosomes interact with one another stills to be assessed. Models for the chromatin conformation during interphase predict a higher frequency of intermingling than it is observed with the current methodologies. 

##Motivation

##Objectives

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


