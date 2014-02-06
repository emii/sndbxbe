Title: Analysis of cytokine profiling from liver metastasis samples
Date: 2013-07-24
Summary: A Brief analysis of the cytokine proifiles from liver metastasis of colorectal cancer
Category: projects
Tags: biology, research, TIGA, master, master thesis
References: C:/Users/ozomatliopochtli/Library/Bibtex/TIGA.bib

Cytokines are signaling peptides recently found to be important in the tumor microenvironmet determining tumour invasion and the spatial distribution of immune cell infiltrates.

## Tumor Infiltrating Lymphocytes

<a class="fancybox" rel="figures" data-title-id="caption-1" href="/static/images/tiga/TIL.png" title="click to enlarge"><img src="/static/images/tiga/TIL.png"/></a>
<div id="caption-1" class="caption"><b>Figure 1.</b> Staining for CD3+ (T-lymphoytes) of the invasive margins in metastasis from different patients. 2, 10, 11, 24 progression free survaival moths respectively. Adapted from [Halama et al. 2011](#Halama2011a)</div>

<a class="fancybox" rel="figures" data-title-id="caption-2" href="/static/images/tiga/density_vs_progression.png" title="click to enlarge"><img src="/static/images/tiga/density_vs_progression.png"/></a>
<div id="caption-2" class="caption"><b>Figure 1]2.</b> Progression-free survival of patients according to the density score value CD3+ + CD8+ GRanzymeB+ of the invasive margins in metastasis. Adapted from [Halama et al. 2011](#Halama2011a)</div>


##Sample preparation and cytokine measurements

Biopsy samples from patients are cryosectioned. Subsequentially, specimens are immunohistochemically analyzed for different immune cell markers (CD3<sup>+</sup>, CD8<sup>+</sup>, granzyme B<sup>+</sup>, FOXP3, NKp46 and CD68<sup>+</sup>). Full tissue sections are imaged and evaluated and different regions are defined: liver, adjacent liver, invasive  margin (500 um width on each side of the border between malignant cells and peritumoral stroma), and liver metastases. Tissue sections were disected and different compartments were treated separately for lysis and posterior multiplexed cytokine detection by luminex assay. (flow cytometry-based method utilizing magnetic microspheres conjugated with monoclonal antibodies using the BioPlex 200 platform with HRF (Bio-Rad, USA), incorporating Luminex xMAP? technology, and validated custom plexes for simultaneous measurement [??](#Krzystek-Korpacka2013))

## Turning off the safety mechanisms
Cytokine interactiong netwoork 
Human IL-10 (hIL-10) suppresses the proliferation and cytokine production of all T cells and the activity of macrophages
Likewise Tumor associated macrophages produce IL-10 which also inhibits the antitumoral cytokine IL12-in a autocrine manner

## Overall distribution of absolute measurements in concentration

We first grouped the data by region (**L** Liver, **AL** Adjacent liver, **IM** Invasive margin, **LM** Liver Metastasis, and Supernatant) and afterwards by gene, thus we see the distribution of the measurements in a boxplot across al patients

<a class="fancybox" rel="figures" href="/static/images/tiga/boxplot-ck-profile-region-patients_log10.png" title="Cytokine profiles" target="_blank"><img src="/static/images/tiga/boxplot-ck-profile-region-patients_log10.png" style="background-color:#fff; max-width: 90%;" alt="" /></a>
<p class="caption" style="width: 90%;"><strong>Figure 1.</strong> Cytokine profiles</p>

We then asked which genes in each region have a concentration over 20 pM. We filtered genes with a median cytokine concentration among all the patients was over 20pM.

<!this is the table 1>

<table border="1" cellpadding="4" cellspacing="0" align="center" style="font-size:0.7em;">
<tr><td colspan="4">Region</td></tr>
<tr><td>L</td><td>AL</td><td>IM</td><td>LM</td></tr>
<tr><td style="background:#00B4A1">IFNG</td><td style="background:#00B4A1">VEGFA</td><td style="background:#00B4A1">IFNG</td><td style="background:#00B4A1">IFNG</td></tr>
<tr><td style="background:#00B4A1">CSF3</td><td style="background:#00B4A1">IFNG</td><td style="background:#20B5A1">CCL11</td><td style="background:#37B8A1">CCL7</td></tr>
<tr><td style="background:#37B8A1">CCL27</td><td style="background:#20B5A1">CCL7</td><td style="background:#20B5A1">CCL7</td><td style="background:#40B9A1">CCL27</td></tr>
<tr><td style="background:#4EBCA1">TNFSF10</td><td style="background:#37B8A1">CCL2</td><td style="background:#37B8A1">SCF</td><td style="background:#47BBA1">Il6</td></tr>
<tr><td style="background:#4EBCA1">CXCL1</td><td style="background:#40B9A1">CCL27</td><td style="background:#37B8A1">IL12A</td><td style="background:#47BBA1">CCL11</td></tr>
<tr><td style="background:#55BEA1">CCL4</td><td style="background:#40B9A1">Il8</td><td style="background:#40B9A1">CCL27</td><td style="background:#4EBCA1">SCF</td></tr>
<tr><td style="background:#5ABFA1">PDGFB</td><td style="background:#55BEA1">CXCL1</td><td style="background:#47BBA1">PDGFB</td><td style="background:#4EBCA1">CSF-1</td></tr>
<tr><td style="background:#60C0A1">CSF-1</td><td style="background:#5ABFA1">CSF-1</td><td style="background:#55BEA1">CSF-1</td><td style="background:#60C0A1">TNFSF10</td></tr>
<tr><td style="background:#6FC4A1">CXCL12</td><td style="background:#5ABFA1">PDGFB</td><td style="background:#73C6A1">TNFSF10</td><td style="background:#65C2A1">IFNA2</td></tr>
<tr><td style="background:#6FC4A1">CXCL10</td><td style="background:#5ABFA1">CCL4</td><td style="background:#73C6A1">Il18</td><td style="background:#65C2A1">Il18</td></tr>
<tr><td style="background:#73C6A1">Il18</td><td style="background:#6AC3A1">Il18</td><td style="background:#73C6A1">IFNA2</td><td style="background:#65C2A1">FGF2</td></tr>
<tr><td style="background:#73C6A1">IFNA2</td><td style="background:#6AC3A1">TNFSF10</td><td style="background:#7CC8A1">CXCL12</td><td style="background:#6AC3A1">IL12A</td></tr>
<tr><td style="background:#80C9A1">Il3</td><td style="background:#73C6A1">CXCL12</td><td style="background:#80C9A1">CCL4</td><td style="background:#78C7A1">CCL4</td></tr>
<tr><td style="background:#88CCA1">Il12</td><td style="background:#73C6A1">IFNA2</td><td style="background:#80C9A1">CCL2</td><td style="background:#78C7A1">Il3</td></tr>
<tr><td style="background:#88CCA1">IL2RA</td><td style="background:#84CBA1">Il3</td><td style="background:#84CBA1">VEGFA</td><td style="background:#80C9A1">CXCL12</td></tr>
<tr><td style="background:#88CCA1">CXCL9</td><td style="background:#84CBA1">CXCL10</td><td style="background:#84CBA1">Il3</td><td style="background:#8CCDA1">CCL5</td></tr>
<tr><td style="background:#8FCEA1">CCL5</td><td style="background:#8CCDA1">FGF2</td><td style="background:#84CBA1">CXCL1</td><td style="background:#8FCEA1">IL2RA</td></tr>
<tr><td style="background:#8FCEA1">FGF2</td><td style="background:#8CCDA1">Il12</td><td style="background:#88CCA1">FGF2</td><td style="background:#8FCEA1">Il12</td></tr>
<tr><td style="background:#A6D7A1">CLEC11A</td><td style="background:#8FCEA1">IL2RA</td><td style="background:#93D0A1">Il12</td><td style="background:#93D0A1">CXCL1</td></tr>
<tr><td style="background:#AFDBA1">HGF</td><td style="background:#AAD8A1">CCL5</td><td style="background:#96D1A1">IL2RA</td><td style="background:#A3D6A1">CCL2</td></tr>
<tr><td style="background:#B2DCA1">Il16</td><td style="background:#ADD9A1">CXCL9</td><td style="background:#9AD2A1">Il8</td><td style="background:#B2DCA1">Il16</td></tr>
<tr><td style="background:#D0E8A1">IL1RN</td><td style="background:#B5DDA1">CLEC11A</td><td style="background:#A6D7A1">CCL5</td><td style="background:#B2DCA1">VEGFA</td></tr>
<tr><td style="background:#D2E9A1">VCAM1</td><td style="background:#BEE0A1">Il16</td><td style="background:#ADD9A1">CXCL10</td><td style="background:#B2DCA1">CXCL10</td></tr>
<tr><td style="background:#D2E9A1">ICAM1</td><td style="background:#BEE0A1">HGF</td><td style="background:#C0E2A1">Il16</td><td style="background:#B2DCA1">Il8</td></tr>
<tr><td style="background:#FFFFA1">MIF</td><td style="background:#D2E9A1">IL1RN</td><td style="background:#C3E3A1">CXCL9</td><td style="background:#C0E2A1">CXCL9</td></tr>
<tr><td style="background:#FFFFFF">&nbsp;</td><td style="background:#D5EAA1">ICAM1</td><td style="background:#C8E5A1">ICAM1</td><td style="background:#C8E5A1">HGF</td></tr>
<tr><td style="background:#FFFFFF">&nbsp;</td><td style="background:#DCEEA1">VCAM1</td><td style="background:#CDE7A1">HGF</td><td style="background:#D2E9A1">ICAM1</td></tr>
<tr><td style="background:#FFFFFF">&nbsp;</td><td style="background:#F8FBA1">MIF</td><td style="background:#D7ECA1">IL1RN</td><td style="background:#D5EAA1">IL1RN</td></tr>
<tr><td style="background:#FFFFFF">&nbsp;</td><td style="background:#FFFFFF">&nbsp;</td><td style="background:#DEEFA1">VCAM1</td><td style="background:#DCEEA1">VCAM1</td></tr>
<tr><td style="background:#FFFFFF">&nbsp;</td><td style="background:#FFFFFF">&nbsp;</td><td style="background:#E3F1A1">CLEC11A</td><td style="background:#F4F9A1">MIF</td></tr>
<tr><td style="background:#FFFFFF">&nbsp;</td><td style="background:#FFFFFF">&nbsp;</td><td style="background:#F8FBA1">MIF</td><td style="background:#FAFCA1">CLEC11A</td></tr>
</table>

<p class="caption" style="width: 90%; margin-top: 5px; margin-bottom: 5px;"><strong>Table 1.</strong> Cytokines with median concentration above 20 pM, (ascending order)</p>

<!this is the table 2>

<table border="1" cellpadding="4" cellspacing="0" align="center" style="font-size:0.7em;">
<tr><td style="background:#00B4A1">ICAM1</td><td style="background:#80C9A1">Il12</td><td style="background:#8CCDA1">FGF2</td><td style="background:#ADD9A1">Il18</td><td style="background:#BEE0A1">CCL5</td><td style="background:#DEEFA1">Il8</td></tr>
<tr><td style="background:#4EBCA1">IFNA2</td><td style="background:#84CBA1">CCL7</td><td style="background:#8CCDA1">CSF3</td><td style="background:#ADD9A1">HGF</td><td style="background:#C8E5A1">MIF</td><td style="background:#F0F7A1">CLEC11A</td></tr>
<tr><td style="background:#6FC4A1">CCL27</td><td style="background:#88CCA1">Il16</td><td style="background:#93D0A1">CSF-1</td><td style="background:#B5DDA1">CCL11</td><td style="background:#CDE7A1">CCL4</td><td style="background:#FFFFA1">Il6</td></tr>
<tr><td style="background:#73C6A1">Il3</td><td style="background:#88CCA1">VCAM1</td><td style="background:#96D1A1">SCF</td><td style="background:#B8DEA1">VEGFA</td><td style="background:#CDE7A1">CXCL10</td><td style="background:#FFFFFF">&nbsp;</td></tr>
<tr><td style="background:#73C6A1">IL2RA</td><td style="background:#88CCA1">IFNG</td><td style="background:#9AD2A1">IL12A</td><td style="background:#BBDFA1">CXCL1</td><td style="background:#D2E9A1">CXCL9</td><td style="background:#FFFFFF">&nbsp;</td></tr>
<tr><td style="background:#80C9A1">PDGFB</td><td style="background:#8CCDA1">CXCL12</td><td style="background:#9DD3A1">IL1RN</td><td style="background:#BEE0A1">TNFSF10</td><td style="background:#D5EAA1">CCL2</td><td style="background:#FFFFFF">&nbsp;</td></tr>
</table>
<p class="caption" style="width: 90%; margin-top: 5px;"><strong>Table 2.</strong> Unique cytokines by coefficient of variation</p>

<a class="fancybox" rel="figures" href="/static/images/tiga/hist_cytokine_concentrations.png" title="Histogram of cytokine concentrations" target="_blank"><img src="/static/images/tiga/hist_cytokine_concentrations.png" style="background-color:#fff; max-width: 90%;" alt="" /></a>
<p class="caption" style="width: 90%;"><strong>Figure 2.</strong> Histogram of cytokine concentrations</p>


<a class="fancybox" rel="figures" href="/static/images/tiga/ecdf_kstest.png" title="mpirical CDF" target="_blank"><img src="/static/images/tiga/ecdf_kstest.png" style="background-color:#fff; max-width: 90%;" alt="click to enlarge" /></a>
<p class="caption" style="width: 90%;"><strong>Figure 3.</strong> Empirical CDF comparison with standard normal distribution, p values come from [Kolmogorov-Smirnoff](http://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test) test at alpha = 0.05, hypotesis are rejected despite their great resemblance, and I am not sure why, when I perform the 2 sample test `kstest2` with normally desitributed random values with mean 0 and std 1, the tests fails to reject the hypotesis that they come from the same distribution....wierd!</p>


<a class="fancybox" rel="figures" href="/static/images/tiga/boxplot-ck-coeff_variation-region-patients_log10.png" title="Coefficient of variation sorted" target="_blank"><img src="/static/images/tiga/boxplot-ck-coeff_variation-region-patients_log10.png" style="background-color:#fff; max-width: 90%;" alt="" /></a>
<p class="caption" style="width: 90%;"><strong>Figure 3.</strong> Cytokine concentrations sorted by coefficient of variation</p>

## Coefficient of variation for lognormally distributed data

\\begin{equation}
   \hat{C}_v = \sqrt{e^{\sigma^2} -1}
\\end{equation}



<a class="fancybox" rel="figures" href="/static/images/tiga/boxplot-ck-coeff_variation-all-regions.png" title="Coefficient of variation sorted for all regions" target="_blank"><img src="/static/images/tiga/boxplot-ck-coeff_variation-all-regions.png" style="background-color:#fff; max-width: 90%;" alt="" /></a>
<p class="caption" style="width: 90%;"><strong>Figure 4.</strong> Cytokine concentrations sorted by coefficient of variation for all regions (L,AL,IM,LM)</p>

boxplot-ck-coeff_variation-all-regions-single-ck.png

<a class="fancybox" rel="figures" href="/static/images/tiga/boxplot-ck-coeff_variation-all-regions-single-ck.png" title="Coefficient of variation sorted for all regions" target="_blank"><img src="/static/images/tiga/boxplot-ck-coeff_variation-all-regions-single-ck.png" style="background-color:#fff; max-width: 90%;" alt="" /></a>
<p class="caption" style="width: 90%;"><strong>Figure 5.</strong> Cytokine concentrations sorted by coefficient of variation for all regions (L,AL,IM,LM)</p>

<a class="fancybox" rel="figures" href="/static/images/tiga/rank_corr_matrix.png" title="Rank correlations matrix" target="_blank"><img src="/static/images/tiga/rank_corr_matrix.png" style="background-color:#fff; max-width: 90%;" alt="" /></a>
<p class="caption" style="width: 90%;"><strong>Figure 6.</strong> Correlation matrix for cytokine levels across patients</p>

<a class="fancybox" rel="figures" href="/static/images/tiga/ck_corr_network.png" title="Network of correlations" target="_blank"><img src="/static/images/tiga/ck_corr_network.png" style="background-color:#fff; max-width: 90%;" alt="" /></a>
<p class="caption" style="width: 90%;"><strong>Figure 7.</strong> Network for cytokine correlating in levels across patients, I used a threshold for corelation of &gt; 0.75 and &lt; -0.6, </p>

<a class="fancybox" rel="figures" href="/static/images/tiga/ck_corr_network-07.png" title="Network of correlations" target="_blank"><img src="/static/images/tiga/ck_corr_network-07.png" style="background-color:#fff; max-width: 90%;" alt="" /></a>
<p class="caption" style="width: 90%;"><strong>Figure 8.</strong> Network for cytokine correlating in levels across patients, I used a threshold for corelation of &gt; 0.7 and &lt; -0.6, </p>

When we observe the cytokine profiles for different cytokines we see that some of them have both clear patterns of localized concentration and low or high variability. The aim of ana;lysing this kind of data is to integrate it into a theoretical model. We can observe that two highly variable cytokine profiles correlate, this means that the variability is coupled in a system and it is not independent from other variable cks, we can also see correlation of mildly variable together with low variable cks. For example the correlation between VEGFA and IL8 is remarkable, with a spearman ncorrelation coefficient of 0.84, being IL8 one of the highly variable cytokines.

As we ask for correlation of cytokine in levels we also want to concentrate in those that are still variable but does not show any correlation with other ones. If each one of the cytokines is a feature, then maybe we can use feature reduction to know which of the genes are the most variable, then concentrate on clustering the patients given these cytokines. another approach could be to use Principal component analysis and then from there cluster the patients, however there we loose the info of which genes are the most determining ones.

Another problem is the factr that we lack values from some of the cytokines, and I still don't know hwat to do with those. One option is to take missing values from the most highly correlated cytokines, using the neighborhood from other patients.

## Missing data imputation

`knnimpute(Data, k)` replaces NaNs in Data with a weighted mean of the k nearest-neighbor columns. The weights are inversely proportional to the distances from the neighboring columns.




<a class="fancybox" rel="figures" href="/static/images/tiga/Ck_profiiles_clustergram_rows_euc-ward_spear-weight.png" title="Network of correlations" target="_blank"><img src="/static/images/tiga/Ck_profiiles_clustergram_rows_euc-ward_spear-weight.png" style="background-color:#fff; max-width: 90%;" alt="" /></a>
<p class="caption" style="width: 90%;"><strong>Figure 9.</strong> `Clustergram` function in MATLAB performs biclustering. After data impuatation with NN using weighted with k=2 we parformed clustering for all the different available samples, we also excluded ICAM1 beacuse it lacked a lot of measurements. For the distances and linkage we used euclidean and ward for rows, and spearman and weighted for columns. The values are standarized to the mean and std of the row. The question here since we already see that the clusetering already recovers very well the different spatial distributons, separating L/AL from IM/LM, this already tells us that there are some genes especific for the different cell types localized at the different regions.</p>

<a class="fancybox" rel="figures" href="/static/images/tiga/Spatial_Ck_profiiles_clustergram_rows_euc-ward2.png" title="Network of correlations" target="_blank"><img src="/static/images/tiga/Spatial_Ck_profiiles_clustergram_rows_euc-ward2.png" style="background-color:#fff; max-width: 90%;" alt="" /></a>
<p class="caption" style="width: 90%;"><strong>Figure 9.</strong> `Clustergram` function in MATLAB performs biclustering. After data impuatation with NN using weighted with k=2 we parformed clustering for all the different available samples, we also excluded ICAM1 beacuse it lacked a lot of measurements. For the distances and linkage we used euclidean and ward for rows, and spearman and weighted for columns. The values are standarized to the mean and std of the row. The question here since we already see that the clusetering already recovers very well the different spatial distributons, separating L/AL from IM/LM, this already tells us that there are some genes especific for the different cell types localized at the different regions.</p>

<!SICARII (SIngle Cell ARtificial IntelIgence) also from the plural of sicarius, use developmental principles to build biological machines with emergent properties and autoorganization.>