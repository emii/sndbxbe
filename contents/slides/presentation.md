Date: 2013-04-16
Title: MDC Interview Week Spring 2013, Max Delbrueck Centrum, Berlin Buch
Summary: Slides for the interview week at MDC
Abstract: My presentation for the lab meeting April 15 - 18, 2013
Template: deck
Tags: research, slides
Affiliation: Master in Molecular Biosciences, 	
Place: University of Heidelberg
Image_top: hdfish.png
Category: showcase
Class: entry2

<div class="slide" id="1"><h2>Instructions:</h2>
<p><h3 style="text-align:center; color: #1985b2;">1. press arrows &larr; and &rarr; to navigate</h3>
<h3 style="text-align:center; color: #1985b2;">2. interrupt whenever you have a question</h3></p>
</div><div class="slide" id="2"><h2>Trying D3.js</h2>
<p style="text-align:center;"><iframe src="/static/D3/testD3.html" height="500" width="690" marginwidth="0" marginheight="0" scrolling="no" frameborder="0"></iframe></p>

</div><div class="slide" id="3"><h2>The title:</h2>
<blockquote>
<p class="slide">A glimpse into chromatin organization by HD-DNA FISH</p>
</blockquote>
<hr />
<blockquote>
<p class="slide">The data analysis pipeline for HD-DNA FISH</p>
</blockquote>
</div><div class="slide" id="4"><h2>Outline</h2>
<ul>
<li>Introduction</li>
<li>Explain the general analysis pipeline<ul>
<li>The SpotterUI </li>
</ul>
</li>
<li>Interleaved 4-loci spotting</li>
<li>Combinatorial labeling spotting</li>
<li>Measuring and correcting the shift<ul>
<li>projective transform as a first approach</li>
<li>a more refined approach</li>
</ul>
</li>
<li>What would be next</li>
</ul>
</div><div class="slide" id="5"><h2>What is HD DNA-FISH?</h2>
<ul>
<li>A methodology that allow us to visualize genomic regions between 3 kbps and 10 kbps</li>
<li>It uses hybridization of ~4 times labeled 200nt amplicons</li>
<li>Similar to smRNA-FISH, this regions are detected as small fluorescent spots</li>
<li>Adds some sophistication to smRNA FISH</li>
<li>Requires higher precision for spot identification</li>
<li>Exact 3D position matters </li>
</ul>
</div><div class="slide" id="6"><h2>The spot identification pipeline</h2>
<ol>
<li>Segmentation of the ROIs</li>
<li>Correct for the shift between channels</li>
<li>Increase S/N ratio (filter for particle size - LoG)</li>
<li>Select for the intensity threshold</li>
<li>Count, assign, and compute spot features<ul>
<li>Precise position</li>
<li>Intensity, volume, FWHM</li>
</ul>
</li>
</ol>
</div><div class="slide" id="7"><h2>The spot identification pipeline</h2>
<ol>
<li><strong>Segmentation of the ROIs</strong></li>
<li><strong>Correct for the shift between channels</strong></li>
<li>Increase S/N ratio (filter for particle size - LoG)</li>
<li>Select for the intensity threshold</li>
<li><strong>Count, assign, and compute spot features</strong><ul>
<li><strong>Precise position</strong></li>
<li><strong>Intensity, volume, FWHM</strong></li>
</ul>
</li>
</ol>
</div><div class="slide" id="8"><h2>The SpotterUI is a cub from ImageM</h2>
<p><img alt="SpotterUI" src="/static/images/slides/chromatin-organization/spotterUI_segmentation.png" /></p>
</div><div class="slide" id="9"><h2>The shift is corrected by a linear transformation</h2>
<p><img alt="bead selection tool" src="/static/images/slides/chromatin-organization/CPS.png" /></p>
</div><div class="slide" id="10"><h2>The applied transformation seems to work</h2>
<p><img alt="TMR shift" src="/static/images/slides/chromatin-organization/tmr_calibXY.jpg" /></p>
</div><div class="slide" id="11"><h2>The spots are counted after selecting a threshold value</h2>
<p><img alt="SpotterUI2" src="/static/images/slides/chromatin-organization/spotterUI.png" /></p>
<p></div><div class="slide" id="31" style="background-color:#000000;"><p style="text-align:center;"><h3 style="color:#fafafa; text-align:center;">The 4 loci experiment</h3></p><p><img alt="4 loci experiment" src="/static/images/slides/chromatin-organization/OL_008.png"></p></p>
</div><div class="slide" id="12"><h2>The 4 loci experiment</h2>
<p><img alt="4 loci" src="/static/images/slides/chromatin-organization/4_loci.png" /></p>
<ul>
<li>Interleaved probe sets in both A594 and Cy5 are separated each 10 Mbp</li>
<li>Single chromosomes are observed to be separated in a large fraction of cells</li>
<li>1 distance between spots of the same color</li>
<li>4 distances between spots of different colors</li>
</ul>
</div><div class="slide" id="13"><h2>The numbers after counting</h2>
<p><img alt="4 loci counts" src="/static/images/slides/chromatin-organization/4_loci_counts.png" /></p>
<ul>
<li>Counts for both channels are expected to be <em>almost</em> the same</li>
<li>The total spot counts resembles the cell-cycle-phase distribution</li>
</ul>
</div><div class="slide" id="14"><h2></h2>
<h3>37 out of 324 nuclei have a 4:4 spots configuration</h3>
<p><img alt="4 loci counts" src="/static/images/slides/chromatin-organization/configurations_of_dots1.png" /></p>
</div><div class="slide" id="15"><h2>K-means clustering is applied and certain configuration selected</h2>
<p><img alt="4 loci conf" src="/static/images/slides/chromatin-organization/4_loci_conf.png" /></p>
</div><div class="slide" id="16"><h2></h2>
<p><img alt="4 loci counts" src="/static/images/slides/chromatin-organization/counts3_hists.png" /></p>
</div><div class="slide" id="17"><h2></h2>
<p><img alt="4 loci counts" src="/static/images/slides/chromatin-organization/more_counts1.png" /></p>
</div><div class="slide" id="18"><h2></h2>
<h3>61 out of 324 nuclei have 4:4,3:4,4:3,4:5,5:4 spots configurations</h3>
<p><img alt="4 loci counts" src="/static/images/slides/chromatin-organization/configurations_of_dots2.png" /></p>
</div><div class="slide" id="19"><h2></h2>
<p><img alt="4 loci counts" src="/static/images/slides/chromatin-organization/more_counts.png" /></p>
</div><div class="slide" id="20"><h2></h2>
<h3>A leveling-off of physical distances &gt; 20 Mbp is observed</h3>
<p><img alt="4 loci counts" src="/static/images/slides/chromatin-organization/level-off.png" /></p>
<pre style="text-align:right;">Mateos-Langerak et al. 2009 PNAS</pre>

</div><div class="slide" id="21"><h2>Combinatorial labeling setup</h2>
<p><img alt="Combinatorial labeling" src="/static/images/slides/chromatin-organization/comb-label.png" /></p>
<ul>
<li>When observing to the data, I found no major co-localization of the probes</li>
<li>I then went back to do a more detailed assessment of the shift calibration</li>
</ul>
</div><div class="slide" id="22"><h2>Summary I</h2>
<ul>
<li>Some improvements to ImageM were made: auto-segmentation, interaction with single nuclei, etc.</li>
<li>The linear transformation for the correction of the shift was fine as a first approach, however not enough for the multi-labeling scenario</li>
<li>A refined method for correcting the shift is necessary</li>
</ul>
</div><div class="slide" id="23"><h2>Chromatic Aberrations</h2>
<p>Dispersion: When different colors of light propagate at different speeds in a medium, the refractive index is <strong>wavelength dependent</strong>. Chromatic aberrations are those <strong>departures</strong> from <strong>perfect imaging</strong> that are due to dispersion.</p>
<hr />
<p style="text-align:center;">Axial chromatic aberration</p>

<p><img alt=" Axial chromatic aberration " src="/static/images/slides/chromatin-organization/long_color.gif" /> 
<p style="text-align:center;">the shift is in the z direction</p></p>
<hr />
<p style="text-align:center;">Transverse chromatic aberration</p>

<p><img alt=" Transverse chromatic aberration " src="/static/images/slides/chromatin-organization/lat_color.gif" /> 
<p style="text-align:center;">the shift is in the xy plane</p></p>
</div><div class="slide" id="24"><h2>First approach to correct for the shift</h2>
<h3>The projective transformation</h3>
<p><img alt="Projective transformation" src="/static/images/slides/chromatin-organization/projective_transform.png" /></p>
</div><div class="slide" id="25"><h2>Drawbacks</h2>
<ul>
<li>although is position based (XY), it stills linear</li>
<li>based on manual selection of the beads (variability)</li>
<li>only performs correction on the XY plane</li>
</ul>
</div><div class="slide" id="26"><h2>Second approach to correct the shift</h2>
<ol>
<li>Automatic identification of the  coarse position for all beads in the different channels</li>
<li>Refinement of the coarse position by fitting a 2D gaussian for the XY plane and a 1D gaussian for the Z position along the x,y coordinates gotten from the 2D gaussian</li>
<li>Fit a plane for each Z-position and interpolate. (Before talking to Stefan)</li>
</ol>
</div><div class="slide" id="27"><h2>1. Beads are identified by (close) distance relation</h2>
<ul>
<li>
<p>a <strong>clique</strong> is a complete subgraph (all nodes are conected to each other)</p>
</li>
<li>
<p><strong>Automatic identification of fluorescent beads in different channels</strong></p>
<ul>
<li>
<p>how to know that a given bead position in one channel corresponds to same bead in the other channel?</p>
<ol>
<li>use of distances to build an adjacency matrix</li>
<li>from the adjacency matrix find the cliques of size(number of channels)</li>
</ol>
</li>
<li>
<p>possible problems:</p>
<ol>
<li>misidentification  of debris as beads</li>
<li>movement of beads from one channel to another</li>
<li>beads closer than corresponding shift</li>
</ol>
</li>
</ul>
</li>
</ul>
</div><div class="slide" id="28"><h2>Beads identification</h2>
<p><img alt="Beads identification" src="/static/images/slides/chromatin-organization/beads_identification.png" /></p>
<p style="text-align: center;">
<strong>A.</strong>beads image
<strong>B.</strong> identification of single cliques
<strong>C.</strong> zoom of the identified cliques
</p>

</div><div class="slide" id="29"><h2>Dense distribution of beads</h2>
<p><img alt="Beads dense" src="/static/images/slides/chromatin-organization/beads_dense_panels.png" /></p>
<p style="text-align: center;">
<strong>A.</strong>beads image
<strong>B.</strong>identification of nearest beads in other channels
<strong>C.</strong>identification of beads' cliques
</p>

</div><div class="slide" id="30"><h2>Shift measurement</h2>
<p><img alt="Shift quantification" src="/static/images/slides/chromatin-organization/shift_magnitude.png" /></p>
</div><div class="slide" id="31"><h2>Shift measurement</h2>
<h3>After calibration using the linear transform</h3>
<p><img alt="Shift quantification calib" src="/static/images/slides/chromatin-organization/shift_magnitude_clalib.png" /></p>
</div><div class="slide" id="32"><h2>2. Beads are fitted to Gaussian functions</h2>
<h3>A bead seen from different planes</h3>
<p><img alt="Dot image" src="/static/images/slides/chromatin-organization/dot_image.png" /></p>
</div><div class="slide" id="33"><h2>Gaussian function fitting</h2>
<p><img alt="Gaussian Fit" src="/static/images/slides/chromatin-organization/2D_Gaussian_1D_gaussian.png" /></p>
</div><div class="slide" id="34"><h2>Polynomial function fitting</h2>
<p style="text-align:center"><object type="image/svg+xml" data="/static/images/slides/chromatin-organization/a594_shift_p2.svg" width="900px" height="900px"></object></p>

</div><div class="slide" id="35"><h2>Outlook</h2>
<h3>Precise position estimation</h3>
<ul>
<li>
<p>Use automatic identification of the beads together with gaussian fit correction to get the coordinate positioning of the beads and correct the shift. Use the same approach to get the HD-FISH spots features</p>
</li>
<li>
<p>From there use Stefan's approach to calculate the shift as a function of the position in x,y, and z of the beads</p>
</li>
<li>
<p>Experiment-wise, Magda is preparing a 2-channel single-loci DNA-FISH image acquisition which would help to calculate the shift specific for the medium in which probes are. Also to estimate the shift at different z-planes (no need of 3D experiment with beads) </p>
</li>
</ul>
<h3>After precise position estimation</h3>
<ul>
<li>
<p>Re-analyze the 4 loci experiment</p>
</li>
<li>
<p>Continue the analysis of the multi-labeling experiment</p>
</li>
</ul>
</div><div class="slide" id="36"><h2>Aknowledgements</h2>
<ul>
<li>Magda</li>
<li>
<p>Stefan</p>
</li>
<li>
<p>Lennart</p>
</li>
<li>Mauro</li>
<li>
<p>Philipp</p>
</li>
<li>
<p>Alexander</p>
</li>
</ul>
<p></div><div class="slide" id="30" style="background-color:#000000;"><h1 style="color:#fafafa;">Thank you!</h1></p>
</div>
