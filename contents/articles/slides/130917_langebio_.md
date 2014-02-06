Date: 2013-09-17
Title: Langebio, CINVESTAV-Irapuato, Irapuato, Guanajuato
Summary: Slides for the visit to Langebio
Template: deck
Tags: research, slides, hd dna-fish, deck
Affiliation: Master in Molecular Biosciences, 	
Place: University of Heidelberg
Image_top: hdfish.png
Category: showcase
Class: entry2
Gallery: pic-show

<div class="slide" id="1"><h2>Chromatin topology plays an important role in gene regulation</h2>
<p><img alt="slide1" src="/static/images/slides/chromatin-organization/slide1_2.png" /></p>
</div><div class="slide" id="2"><h2>Chromatin organization is approached theoretically by polymer models</h2>
<p>One characteristic feature of a polymer model is the mean-squared spatial end-to-end distance $\langle R^{2}\rangle$ which as a function of its genomic distance $g$ scales $\langle R^{2}\rangle \sim g^{2\nu}$, the exponent $\nu$ varies given the dynamics of each polymer representation, such as random walk, self-avoiding walk, or globular state (<a href="#Tark-dame2012">Tark-Dame et al. 2012</a>)</p>
<ul>
<li><em>Fractal globule</em> (<a href="#Lieberman-Aiden2009a">Lieberman-Aiden et al. 2009</a>)</li>
<li><em>Random loop</em> (<a href="#Mateos-Langerak2009">Mateos-Langerak et al. 2009</a>)</li>
<li><em>String and binders switch</em> (<a href="#Barbieri2012">Barbieri et al. 2013</a>)</li>
</ul>
</div><div class="slide" id="3"><h2>Nuclear Topology is experimentally addressed by 3C and FISH</h2>
<ul>
<li><strong>3C</strong> formaldehyde crosslinking snapshots on the bulk to quantify distance between genomic loci, interpreted from contact probabilities</li>
<li><strong>FISH</strong> fluorescently labeled probes are designed to target specific genomic loci. </li>
</ul>
</div><div class="slide" id="4"><h2>Distance between chromatin regions are measured from 3D positions of fluorescent spots</h2>
<p><img alt="slide2" src="/static/images/slides/chromatin-organization/slide2.png" /></p>
<p></div><div class="slide" id="30" style="background-color:#000000;"><img alt="4 loci experiment" src="/static/images/slides/chromatin-organization/OL_008.png"></p>
</div><div class="slide" id="5"><h2>Spots are identified for singles cells</h2>
<p><img alt="spotterUI2" src="/static/images/slides/chromatin-organization/spotterUI.png" /></p>
</div><div class="slide" id="6"><h2>Precise localization of the spots is estimated with Gaussian functions</h2>
<p><img alt="Dot image" src="/static/images/slides/chromatin-organization/dot_image.png" /></p>
<p>\begin{equation}
    f(x,y) = A \exp\left(- \left(\frac{(x-x_o)^2}{2\sigma_x^2} + \frac{(y-y_o)^2}{2\sigma_y^2} \right)\right) + b
\end{equation}</p>
<p>\begin{equation}
    f(z) = A \exp \left( -\frac{(z-z_o)^2}{2\sigma_z^2}\right)
\end{equation}</p>
</div><div class="slide" id="7"><h2></h2>
<p><img alt="gaussian_fit" src="/static/images/slides/chromatin-organization/2D_Gaussian_1D_gaussian.png" /></p>
</div><div class="slide" id="8"><h2>Chromatic aberrations are corrected after registering fiduciary markers</h2>
<p><img alt="Beads identification" src="/static/images/slides/chromatin-organization/beads_identification.png" /></p>
<p><img alt="Beads dense" src="/static/images/slides/chromatin-organization/beads_dense_panels.png" /></p>
</div><div class="slide" id="9"><h2></h2>
<p>\begin{equation*}
\Delta^{ch}_{xi} = x^{ch}_i - x^{ref}_i \\
\Delta^{ch}_{yi} = y^{ch}_i - y^{ref}_i \\
\Delta^{ch}_{zi} = z^{ch}_i - z^{ref}_i \\
\end{equation*}</p>
<p>Then for each channel we formulated the shift $\Delta$ as a function of the three-dimesional localization:</p>
<p>\begin{equation*}
\Delta^{ch}_{x}= f(x,y,z)\\
\Delta^{ch}_{y} = f(x,y,z)\\
\Delta^{ch}_{z} = f(x,y,z)
\end{equation*}</p>
</div><div class="slide" id="10"><h2>Distortions are wavelength dependent</h2>
<p><img alt="uncorrected" src="/static/images/slides/chromatin-organization/uncorrected.png" /></p>
</div><div class="slide" id="11"><h2>Shift is modeled as a higher degree polynomial</h2>
<p>\begin{equation}
    \Delta^{ch}_{dim}(x,y,z) = a_{n,n,n}x^ny^nz^n + a_{n,,n,n-1}x^ny^nz^{n-1} + a_{n,n-1,n}x^ny^{n-1}z^n + \ldots + a_{1,0,0}x + a_{0,1,0}y + + a_{0,0,1}z + a_{0,0,0}
\end{equation}</p>
</div><div class="slide" id="12"><h2></h2>
<p><img alt="shiftw" src="/static/images/slides/chromatin-organization/shoftw.png" /></p>
</div><div class="slide" id="13"><h2>Shift is notably reduced</h2>
<p><img alt="corrected" src="/static/images/slides/chromatin-organization/corrected.png" /></p>
</div><div class="slide" id="14"><h2></h2>
<p>!<img alt="TMR shift" src="/static/images/slides/chromatin-organization/tmr_calibXY.jpg" /></p>
</div><div class="slide" id="15"><h2>Distances within single chromosomes are measured</h2>
<p><img alt="distances" src="/static/images/slides/chromatin-organization/slide5.png" /></p>
</div><div class="slide" id="16"><h2>Our results are in agreement with previous observations</h2>
<p><img alt="4 loci counts" src="/static/images/slides/chromatin-organization/slide6.png" /></p>
<pre style="text-align:right;">Mateos-Langerak et al. 2009 PNAS</pre>

<h3>Outlook</h3>
<h4>Combinatorial labeling provides identifiers for unique regions</h4>
<p><img alt="distances" src="/static/images/slides/chromatin-organization/comb-label.png" /></p>
</div><div class="slide" id="17"><h2>Concluding remarks</h2>
<ul>
<li>
<p>A major question in understanding spatial genome organization is how patterns of chromosome or loci organization are established and maintained</p>
</li>
<li>
<p>Better resolution and perhaps multiplexing for the precise estimation of the localization of chromosome regions can be acheived by using our methodology </p>
</li>
<li>
<p>These measurements will provide insight in understanding the formation of patterns in chromatin organization</p>
</li>
</ul>
</div><div class="slide" id="18"><h2>Aknowledgements</h2>
<h3>Group van Oudenaarden</h3>
<h4>at MIT:</h4>
<ul>
<li>Magda Bienko</li>
<li>Stefan Semrau</li>
</ul>
<h4>at the Hubrecht Institute:</h4>
<ul>
<li>Alexander van Oudenaarden</li>
</ul>
</div><div class="slide" id="30" style="background-color:#000000;"><h1 style="color:#fafafa;">Thank you!</h1></p>
</div>
