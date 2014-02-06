Date: 2013-11-18
Title: Progress seminar
Summary: Slides for the TIGA progress seminar
Template: deck
Tags: research, slides, TIGA, deck
Affiliation: Master in Molecular Biosciences,
Place: University of Heidelberg
Image_top: cytokine-network.png
Category: showcase
Class: entry2

<div class="slide" id="1"><h2>Outline</h2>
<ul>
<li>Talk about what I have done so far</li>
<li>About what's to be done</li>
<li>Get feedback from you</li>
</ul>
</div><div class="slide" id="2"><h2>Immune cell infiltrates correlate with treatment prognosis</h2>
<p><img alt="slide1" src="/static/images/tiga/TIL.png" />
<img alt="slide2" src="/static/images/tiga/density_vs_progression.png" /></p>
<ul>
<li>
<p>Biopsy samples from patients are cryosectioned. Subsequentially, specimens are immunohistochemically analyzed for different immune cell markers (CD3<sup>+</sup>, CD8<sup>+</sup>, granzyme B<sup>+</sup>)</p>
</li>
<li>
<p>Full tissue sections are imaged and evaluated, different regions are defined: liver (<strong>L</strong>), adjacent liver (<strong>AL</strong>), invasive  margin (<strong>IM</strong>), and liver metastases (<strong>LM</strong>).</p>
</li>
</ul>
<p>Figures adapted from <a href="#Halama2011a">Halama et al. 2011</a></p>
</div><div class="slide" id="3"><h2>Immune cell infiltrates correlate with treatment prognosis</h2>
<p>In most tumors the infiltration of immune cells has been tightly linked to a positive response of patients to treatment. However a high variability in the density of the infiltrations is also charachteristic from patients. It has been hypotesized that most of this variability arises from the tumor microenvironment.</p>
<ul>
<li>cytokines, chemokines</li>
<li>growth and angiogenic factors</li>
</ul>
<h3>the immune response is a complex process involving different elements interacting within a spatial context that requires a systematic approach</h3>
</div><div class="slide" id="4"><h2>Cytokine concentrations were measured</h2>
<h3>Cytokine concentration range spans various orders of magnitude</h3>
<p>The absolute cytokine concentration profiles were measured form a cohort of around 50 patients in four diferent tumor microenvironment compartments. There are big differences in the concentration among cytokines (from some pg to hundreds of ng per ml)</p>
<p><img alt="slide2.5" src="/static/images/tiga/boxplot-ck-coeff_variation-all-regions.png" /></p>
</div><div class="slide" id="5"><h2>Cytokine concentrations were measured</h2>
<h3>The absolute cytokine concentration profiles were measured across the different compartments</h3>
<p>integrating information from cytokine concentrations measured </p>
<p>We first grouped the data by region (<strong>L</strong> Liver, <strong>AL</strong> Adjacent liver, <strong>IM</strong> Invasive margin, <strong>LM</strong> Liver Metastasis, and Supernatant) and afterwards by gene, thus we see the distribution of the measurements in a boxplot across al patients</p>
<p><img alt="slide3" src="/static/images/tiga/boxplot-ck-profile-region-patients_log10.png" /></p>
</div><div class="slide" id="6"><h2>Cytokine levels are log-normally distributed</h2>
<p>s
<img alt="slide4" src="/static/images/tiga/hist_cytokine_concentrations.png" /></p>
</div><div class="slide" id="7"><h2>Cytokine levels are log-normally distributed</h2>
<p><img alt="slide3" src="/static/images/tiga/ecdf_kstest.png" /></p>
</div><div class="slide" id="8"><h2>Cytokine levels vary across and within regions</h2>
<p>Their distrbution allows us to calculate their coefficient of variation, a normalized measure of dispertion.</p>
<p>is defined as $\hat{C}_v = \frac{\sigma}{\mu}$, in our case, for log-normal distributions: $\hat{C}_v = \sqrt{e^{\sigma^2} -1}$</p>
<p>Given this measure we can rank our cytokines:</p>
<table border="1" cellpadding="4" cellspacing="0" align="center" style="font-size:1.2em; text-align:center;">
<tr><td style="background:#00B4A1">ICAM1</td><td style="background:#80C9A1">Il12</td><td style="background:#8CCDA1">FGF2</td><td style="background:#ADD9A1">Il18</td><td style="background:#BEE0A1">CCL5</td><td style="background:#DEEFA1">Il8</td></tr>
<tr><td style="background:#4EBCA1">IFNA2</td><td style="background:#84CBA1">CCL7</td><td style="background:#8CCDA1">CSF3</td><td style="background:#ADD9A1">HGF</td><td style="background:#C8E5A1">MIF</td><td style="background:#F0F7A1">CLEC11A</td></tr>
<tr><td style="background:#6FC4A1">CCL27</td><td style="background:#88CCA1">Il16</td><td style="background:#93D0A1">CSF-1</td><td style="background:#B5DDA1">CCL11</td><td style="background:#CDE7A1">CCL4</td><td style="background:#FFFFA1">Il6</td></tr>
<tr><td style="background:#73C6A1">Il3</td><td style="background:#88CCA1">VCAM1</td><td style="background:#96D1A1">SCF</td><td style="background:#B8DEA1">VEGFA</td><td style="background:#CDE7A1">CXCL10</td><td style="background:#FFFFFF">&nbsp;</td></tr>
<tr><td style="background:#73C6A1">IL2RA</td><td style="background:#88CCA1">IFNG</td><td style="background:#9AD2A1">IL12A</td><td style="background:#BBDFA1">CXCL1</td><td style="background:#D2E9A1">CXCL9</td><td style="background:#FFFFFF">&nbsp;</td></tr>
<tr><td style="background:#80C9A1">PDGFB</td><td style="background:#8CCDA1">CXCL12</td><td style="background:#9DD3A1">IL1RN</td><td style="background:#BEE0A1">TNFSF10</td><td style="background:#D5EAA1">CCL2</td><td style="background:#FFFFFF">&nbsp;</td></tr>
</table>

<p>pic</p>
</div><div class="slide" id="9"><h2>Cytokine levels vary across and within regions</h2>
<p><img alt="slidecl" src="/static/images/tiga/boxplot-ck-coeff_variation-region-patients_log10.png" /></p>
</div><div class="slide" id="10"><h2>Some cytokine profiles are highly correlated</h2>
<p><img alt="slidecpc" src="/static/images/tiga/rank_corr_matrix.png" /></p>
</div><div class="slide" id="11"><h2>Some cytokine profiles are highly correlated</h2>
<p><img alt="slidecpc" src="/static/images/tiga/rank_corr_matrix.png" /></p>
</div><div class="slide" id="12"><h2>Modelling a cytokine network</h2>
<ul>
<li>The immune cells regulate the overall response by mutually influencing each others activity</li>
<li>Modulated activities include both the production of other cytokines in addition to an effector funciton</li>
<li>Each cell types is characterized by a set of cytokines that it can secrete as well as set of cytokine that control its activity</li>
</ul>
</div><div class="slide" id="13"><h2>Uncertainty and sensitivity analysis</h2>
<ul>
<li>
<p>Accuracy of results from mathematical and computer models of biological systems is often complicated by the presence of uncertainties in experimental data that are used to estimate parameter values.</p>
</li>
<li>
<p>Increased understanding of the relationships between input and output variables in a system or model.</p>
</li>
<li>
<p>Sensitivity analysis techniques can help to identify control parameters</p>
</li>
<li>
<p>Model simplification – fixing model inputs that have no effect on the output, or identifying and removing redundant parts of the model structure.</p>
</li>
</ul>
</div><div class="slide" id="14"><h2>Latin hypercube sampling - Partial rank correlation coefficient</h2>
<ul>
<li>
<p>Latin hypercube sampling is a statistical method for generating a sample of plausible collections of parameter values from a multidimensional distribution. Minimizing the correlation between parameters while distributing them within even intervals across the sample space</p>
</li>
<li>
<p>Rahter than exactly quantifying sensitivity we use PRCC to identify which input variables are contributing significantly to the output uncertainty (correlation between one parameter and one output variable)</p>
</li>
</ul>
</div><div class="slide" id="15"><h2>Example from literature</h2>
</div><div class="slide" id="16"><h2>Episim allows for the modelling of tissue-level together with its microenvironment</h2>
<ul>
<li>Integrate information about the tissue context in which cancer develops</li>
<li>Capturing the evolution of the various cell populations (<strong>AL</strong>, <strong>IM</strong>, <strong>LM</strong>)</li>
<li>Action of cytokines signals as activators/inhibitors of the immune cells</li>
<li>Incorporate both "continuum" variables and agent-base variables in a modular approach</li>
<li>Focus on the immune cell density of the <strong>IM</strong></li>
<li>Allow the evaluation of input parameters controling immune cell density and their activation state</li>
<li>Immuno-depressed/activated -&gt; tumor-dormancy/escape/elimination</li>
</ul>
</div><div class="slide" id="17"><h2>Elements of the model</h2>
<ol>
<li>The environment where entities reside, representing a section of the liver metastasis. </li>
<li>The entities of the model, consisting of discrete liver, immune, and metastases cells, and continuous chemokine variables. </li>
<li>The rules that govern the dynamics of the system, representing the biological interactions of the entities.</li>
</ol>
</div><div class="slide" id="18"><h2>Parameter scan</h2>
<p><img alt="slideps" src="/static/images/tiga/parameter_scan.png" /></p>
</div><div class="slide" id="19"><h2>Using the cluster</h2>
<ul>
<li>Parameter files (.properties) were generated in MATLAB using LHS for the combination of parameters</li>
</ul>
<p>100 jobs, 7 parameters, 200 simulation steps</p>
<p>start: 8.30 pm end: 2.30 am (I think it finished bacuase of wall-time set to 6h)</p>
<p>the first run:</p>
<div class="codehilite"><pre><span class="n">PBS</span> <span class="n">Job</span> <span class="n">Id</span><span class="o">:</span> <span class="mi">2668358</span><span class="o">-</span><span class="mf">8.</span><span class="n">cln035</span><span class="p">.</span><span class="n">bioquant</span><span class="p">.</span><span class="n">uni</span><span class="o">-</span><span class="n">heidelberg</span><span class="p">.</span><span class="n">de</span>
<span class="n">Job</span> <span class="n">Name</span><span class="o">:</span>   <span class="n">RD2_simulation</span><span class="o">-</span><span class="mi">8</span>
<span class="n">Exec</span> <span class="n">host</span><span class="o">:</span>  <span class="n">cln099</span><span class="o">-</span><span class="kt">int</span><span class="o">/</span><span class="mi">7</span>
<span class="n">Execution</span> <span class="n">terminated</span>
<span class="n">Exit_status</span><span class="o">=</span><span class="mi">0</span>
<span class="n">resources_used</span><span class="p">.</span><span class="n">cput</span><span class="o">=</span><span class="mo">00</span><span class="o">:</span><span class="mo">06</span><span class="o">:</span><span class="mi">36</span>
<span class="n">resources_used</span><span class="p">.</span><span class="n">mem</span><span class="o">=</span><span class="mi">1098544</span><span class="n">kb</span>
<span class="n">resources_used</span><span class="p">.</span><span class="n">vmem</span><span class="o">=</span><span class="mi">5810488</span><span class="n">kb</span>
<span class="n">resources_used</span><span class="p">.</span><span class="n">walltime</span><span class="o">=</span><span class="mo">00</span><span class="o">:</span><span class="mi">18</span><span class="o">:</span><span class="mi">14</span>
</pre></div>


<p>the last run:</p>
<div class="codehilite"><pre><span class="n">PBS</span> <span class="n">Job</span> <span class="n">Id</span><span class="o">:</span> <span class="mi">2668358</span><span class="o">-</span><span class="mf">91.</span><span class="n">cln035</span><span class="p">.</span><span class="n">bioquant</span><span class="p">.</span><span class="n">uni</span><span class="o">-</span><span class="n">heidelberg</span><span class="p">.</span><span class="n">de</span>
<span class="n">Job</span> <span class="n">Name</span><span class="o">:</span>   <span class="n">RD2_simulation</span><span class="o">-</span><span class="mi">91</span>
<span class="n">Exec</span> <span class="n">host</span><span class="o">:</span>  <span class="n">cln099</span><span class="o">-</span><span class="kt">int</span><span class="o">/</span><span class="mi">0</span>
<span class="n">Execution</span> <span class="n">terminated</span>
<span class="n">Exit_status</span><span class="o">=</span><span class="mi">0</span>
<span class="n">resources_used</span><span class="p">.</span><span class="n">cput</span><span class="o">=</span><span class="mo">00</span><span class="o">:</span><span class="mo">02</span><span class="o">:</span><span class="mi">08</span>
<span class="n">resources_used</span><span class="p">.</span><span class="n">mem</span><span class="o">=</span><span class="mi">1003376</span><span class="n">kb</span>
<span class="n">resources_used</span><span class="p">.</span><span class="n">vmem</span><span class="o">=</span><span class="mi">5743788</span><span class="n">kb</span>
<span class="n">resources_used</span><span class="p">.</span><span class="n">walltime</span><span class="o">=</span><span class="mo">00</span><span class="o">:</span><span class="mo">01</span><span class="o">:</span><span class="mi">58</span>
</pre></div>


</div><div class="slide" id="20"><h2>Concluding remarks</h2>
<ul>
<li>
<p>The model aims to integrate a continuous representation of cytokines/chemokines with a discrete representations of different cell-types organized in tissue compartments. </p>
</li>
<li>
<p>As the immune response is a complex process involving different elements interacting within a spatial context and their responses vary given their identity and immediate neighborhood, these particular characteristics are suitable to be approached as discrete entities. </p>
</li>
<li>
<p>Agent based models allow us to incorporate different aspects of the immune system that could give rise to emergent behaviors explaining the variability observed in the density of immune cell infiltrates in patients.</p>
</li>
</ul>
</div><div class="slide" id="21"><h2>Outlook</h2>
<ul>
<li>Incorporate more patient data to the analysis</li>
<li>Look more closely at the literature to reduce the number of cytokines important for our case</li>
<li>Actually translating our data into the model</li>
<li>Write scripts for analysing the output data (i.e. PRCC analysis)</li>
</ul>
</div><div class="slide" id="22"><h2>Aknowledgements</h2>
<ul>
<li>Thomas</li>
<li>Niels H.</li>
<li>Niels G.</li>
</ul>
</div>
