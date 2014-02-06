## Outline

* Talk about what I have done so far
* About what's to be done
* Get feedback from you

## Immune cell infiltrates correlate with treatment prognosis

![slide1](/static/images/tiga/TIL.png)
![slide2](/static/images/tiga/density_vs_progression.png)

* Biopsy samples from patients are cryosectioned. Subsequentially, specimens are immunohistochemically analyzed for different immune cell markers (CD3<sup>+</sup>, CD8<sup>+</sup>, granzyme B<sup>+</sup>)

* Full tissue sections are imaged and evaluated, different regions are defined: liver (**L**), adjacent liver (**AL**), invasive  margin (**IM**), and liver metastases (**LM**).

Figures adapted from [Halama et al. 2011](#Halama2011a)

## Immune cell infiltrates correlate with treatment prognosis

In most tumors the infiltration of immune cells has been tightly linked to a positive response of patients to treatment. However a high variability in the density of the infiltrations is also charachteristic from patients. It has been hypotesized that most of this variability arises from the tumor microenvironment.

* cytokines, chemokines
* growth and angiogenic factors

### the immune response is a complex process involving different elements interacting within a spatial context that requires a systematic approach 

## Cytokine concentrations were measured

### Cytokine concentration range spans various orders of magnitude 

The absolute cytokine concentration profiles were measured form a cohort of around 50 patients in four diferent tumor microenvironment compartments. There are big differences in the concentration among cytokines (from some pg to hundreds of ng per ml)

![slide2.5](/static/images/tiga/boxplot-ck-coeff_variation-all-regions.png)

## Cytokine concentrations were measured

### The absolute cytokine concentration profiles were measured across the different compartments
integrating information from cytokine concentrations measured 

We first grouped the data by region (**L** Liver, **AL** Adjacent liver, **IM** Invasive margin, **LM** Liver Metastasis, and Supernatant) and afterwards by gene, thus we see the distribution of the measurements in a boxplot across al patients

![slide3](/static/images/tiga/boxplot-ck-profile-region-patients_log10.png)

## Cytokine levels are log-normally distributed
s
![slide4](/static/images/tiga/hist_cytokine_concentrations.png)

## Cytokine levels are log-normally distributed

![slide3](/static/images/tiga/ecdf_kstest.png)

## Cytokine levels vary across and within regions

Their distrbution allows us to calculate their coefficient of variation, a normalized measure of dispertion.

is defined as $\hat{C}_v = \frac{\sigma}{\mu}$, in our case, for log-normal distributions: $\hat{C}_v = \sqrt{e^{\sigma^2} -1}$

Given this measure we can rank our cytokines:

<table border="1" cellpadding="4" cellspacing="0" align="center" style="font-size:1.2em; text-align:center;">
<tr><td style="background:#00B4A1">ICAM1</td><td style="background:#80C9A1">Il12</td><td style="background:#8CCDA1">FGF2</td><td style="background:#ADD9A1">Il18</td><td style="background:#BEE0A1">CCL5</td><td style="background:#DEEFA1">Il8</td></tr>
<tr><td style="background:#4EBCA1">IFNA2</td><td style="background:#84CBA1">CCL7</td><td style="background:#8CCDA1">CSF3</td><td style="background:#ADD9A1">HGF</td><td style="background:#C8E5A1">MIF</td><td style="background:#F0F7A1">CLEC11A</td></tr>
<tr><td style="background:#6FC4A1">CCL27</td><td style="background:#88CCA1">Il16</td><td style="background:#93D0A1">CSF-1</td><td style="background:#B5DDA1">CCL11</td><td style="background:#CDE7A1">CCL4</td><td style="background:#FFFFA1">Il6</td></tr>
<tr><td style="background:#73C6A1">Il3</td><td style="background:#88CCA1">VCAM1</td><td style="background:#96D1A1">SCF</td><td style="background:#B8DEA1">VEGFA</td><td style="background:#CDE7A1">CXCL10</td><td style="background:#FFFFFF">&nbsp;</td></tr>
<tr><td style="background:#73C6A1">IL2RA</td><td style="background:#88CCA1">IFNG</td><td style="background:#9AD2A1">IL12A</td><td style="background:#BBDFA1">CXCL1</td><td style="background:#D2E9A1">CXCL9</td><td style="background:#FFFFFF">&nbsp;</td></tr>
<tr><td style="background:#80C9A1">PDGFB</td><td style="background:#8CCDA1">CXCL12</td><td style="background:#9DD3A1">IL1RN</td><td style="background:#BEE0A1">TNFSF10</td><td style="background:#D5EAA1">CCL2</td><td style="background:#FFFFFF">&nbsp;</td></tr>
</table>
pic
## Cytokine levels vary across and within regions

![slidecl](/static/images/tiga/boxplot-ck-coeff_variation-region-patients_log10.png)

## Some cytokine profiles are highly correlated

![slidecpc](/static/images/tiga/rank_corr_matrix.png)

## Some cytokine profiles are highly correlated

![slidecpc](/static/images/tiga/rank_corr_matrix.png)

## Modelling a cytokine network

* The immune cells regulate the overall response by mutually influencing each others activity
* Modulated activities include both the production of other cytokines in addition to an effector funciton
* Each cell types is characterized by a set of cytokines that it can secrete as well as set of cytokine that control its activity




## Uncertainty and sensitivity analysis

* Accuracy of results from mathematical and computer models of biological systems is often complicated by the presence of uncertainties in experimental data that are used to estimate parameter values.

* Increased understanding of the relationships between input and output variables in a system or model.

* Sensitivity analysis techniques can help to identify control parameters

* Model simplification – fixing model inputs that have no effect on the output, or identifying and removing redundant parts of the model structure.

## Latin hypercube sampling - Partial rank correlation coefficient

* Latin hypercube sampling is a statistical method for generating a sample of plausible collections of parameter values from a multidimensional distribution. Minimizing the correlation between parameters while distributing them within even intervals across the sample space

* Rahter than exactly quantifying sensitivity we use PRCC to identify which input variables are contributing significantly to the output uncertainty (correlation between one parameter and one output variable)

## Example from literature



## Episim allows for the modelling of tissue-level together with its microenvironment

* Integrate information about the tissue context in which cancer develops
* Capturing the evolution of the various cell populations (**AL**, **IM**, **LM**)
* Action of cytokines signals as activators/inhibitors of the immune cells
* Incorporate both "continuum" variables and agent-base variables in a modular approach
* Focus on the immune cell density of the **IM**
* Allow the evaluation of input parameters controling immune cell density and their activation state
* Immuno-depressed/activated -> tumor-dormancy/escape/elimination

## Elements of the model

1. The environment where entities reside, representing a section of the liver metastasis. 
2. The entities of the model, consisting of discrete liver, immune, and metastases cells, and continuous chemokine variables. 
3. The rules that govern the dynamics of the system, representing the biological interactions of the entities.

## Parameter scan

![slideps](/static/images/tiga/parameter_scan.png)


## Using the cluster
* Parameter files (.properties) were generated in MATLAB using LHS for the combination of parameters

100 jobs, 7 parameters, 200 simulation steps

start: 8.30 pm end: 2.30 am (I think it finished bacuase of wall-time set to 6h)

the first run:

	PBS Job Id: 2668358-8.cln035.bioquant.uni-heidelberg.de
	Job Name:   RD2_simulation-8
	Exec host:  cln099-int/7
	Execution terminated
	Exit_status=0
	resources_used.cput=00:06:36
	resources_used.mem=1098544kb
	resources_used.vmem=5810488kb
	resources_used.walltime=00:18:14

the last run:

	PBS Job Id: 2668358-91.cln035.bioquant.uni-heidelberg.de
	Job Name:   RD2_simulation-91
	Exec host:  cln099-int/0
	Execution terminated
	Exit_status=0
	resources_used.cput=00:02:08
	resources_used.mem=1003376kb
	resources_used.vmem=5743788kb
	resources_used.walltime=00:01:58

## Concluding remarks

* The model aims to integrate a continuous representation of cytokines/chemokines with a discrete representations of different cell-types organized in tissue compartments. 

* As the immune response is a complex process involving different elements interacting within a spatial context and their responses vary given their identity and immediate neighborhood, these particular characteristics are suitable to be approached as discrete entities. 

* Agent based models allow us to incorporate different aspects of the immune system that could give rise to emergent behaviors explaining the variability observed in the density of immune cell infiltrates in patients.

## Outlook

* Incorporate more patient data to the analysis
* Look more closely at the literature to reduce the number of cytokines important for our case
* Actually translating our data into the model
* Write scripts for analysing the output data (i.e. PRCC analysis)

## Aknowledgements

* Thomas
* Niels H.
* Niels G.
