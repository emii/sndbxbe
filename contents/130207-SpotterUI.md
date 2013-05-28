Title: SpotterUI
Summary: The non-comprehensive non-end-user documentation for the MATLAB implementation of image processing of DNA-FISH
Abstract: So much struggle with the spot identification of fluorescently labeled probes, now this has to be advanced to the precise positioning and colocalization of multi-labeled regions. Here is what I am thinking and experimenting now.
Category: projects
Tags: biology, research, hd dna-fish, image processing 
Date: 2013-02-07

##Detection of colocalizations in multichannel 3D fluorescence microscopy images  

A pipeline and Graphical User Interface (GUI) which help to analyze multi-channel fluorescence microscopy images. The aim of this work is to assess chromosomal organization by High-resolution DNA fluorescence _in situ_ hybridization (HD-DNA FISH). Using a fluorescence microscope Magda acquired about _XXX_ from both 3F3 human fibroblasts and Human Mammary Epithelial cells (HME). Both, chromosomes 1 and 17 were visualized by genomically-equidistant set of fluorescently-labeld DNA-FISH probes. In this study a GUI was developed to analyze the generated three-channel 3D microscopy images to extract information about position and [colocalization][] of the spotter chromosomal regions. 

###1. Automatic Nuclei Segmentation###

* 3D Gaussian filter \[[1](#references)\]
* Otsu thresholding
* Morphological operations

###2. DNA-FISH spots identification###

* Coarse localization identification
	* manual thresholding
	

##<a id="references"></a>References##
1. 3D gaussian filter, bla bla bla

[colocalization]: http://en.wikipedia.org/wiki/Colocalization