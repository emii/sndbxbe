Title: Agent based model of the Metastatic microenvironment from the interaction of cell metapopulations 
Date: 2013-07-21
Summary: Project I am currently working on at TIGA Center/Bioquant  
Category: projects
References: C:/Users/ozomatliopochtli/Library/Bibtex/TIGA.bib
Tags: biology, research, TIGA, master, master thesis
Abstract: <strong>Abstract:</strong> Virtual Microscopy offers new possibilities through high-throughput automated microscopy of complete tissue sections. This approach allows robust and reproducible quantitative evaluations in tissues. Previous work by our group and others has shown that immune cell infiltrates can be used as predictive markers in cancer patients. This project therefore aims to generate an automated histological platform to quantify immune cell infiltration in cancer samples based on virtual microscopy. Integration of standard immunohistological tissue preparation and staining, virtual microscopy and imaging analyses into an automated workflow leads then to an improved individualized prediction and subsequent therapy selection in cancer patients.

[TOC]

#Introduction
##_In silico_ models of cancer
some examples or approaches to model the influence of cytokines and the immune system in pathologies like Reumathoid arthritis and psoriasis,
##Tumor microenvironment
##Cytokines, immune system and cancer
###Cytokine network
* feedforward and feedback signals mediated by cytokines

## Agent Based modeling
* Stability in (multi)-agent based models
* Sensitivity analysis
* Parameter estimation
* Optimization

### Cellular automata
3
##Colorectal cancer
In this section we brefly outline the current knowledge of colorectal cancer metastasis in liver, as well we discuss the role of the immune response and its connection to patient prognosis. We also discuss the described mechanisms in which cell interactions play an important role.

## MOdel description and methods
1. the environment, scale, cell sizes are disregarded
this is a NxN latice of micro compartments each representing the adjacen liver, the invasive margine and the metastasis
mmm, to avoid boundary effects we used a torus
2. the entities (metapopulations) are contained in discrete compartments representing the different defined regions in the metastasis
3. trhe rules for interactions
4. the time scales
esach discrete timestep is represented by the fastest process in the model which is the difussion, which is on the seconds scale, while the whole simulation we want to do is in the range of hundreds of days????, or as soon as the system reaches an equilibrium 
5. initial conditions

## Design of experiment

parameter values estimation and sensitivity analysis, use Latin hypercube sampling together with partial rank correlation coefficient to identify the parameters that correlate more with the 

##The hypotesis

tumor cells disregulate the activation cycle of immun cells by bringing them to a different stable state in the dose response space of the normal inmmune response, thus we should stufy which cytokines in the metastatic tissue vary among patients to have them as candidates for these differences

One important thing is to think about the outcome variables which are going to indicate wether the patients are goiung to have beter prognosis..taht is the to have a cytokine signature for the two groups of patients or to have 

