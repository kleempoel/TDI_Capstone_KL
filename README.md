# Data science applications in Health Genomics
## Kevin Leempoel - TDI Capstone Project

Machine learning and big data processing remains largely unexplored in health genomics and precision medicine.
But recent studies have demonstrated than machine and deep learning applied to large clinical trials enables researchers and clinicians to create more accurate patient profiles, resulting in an improved diagnosis and treatments of  diseases.

As part of my capstone project for [The Data Incubator](https://www.thedataincubator.com/) program (Winter 2020 cohort), I aimed to evaluate the relevance of data science tools in Health Genomics and publish my findings, scripts and interactive visualization tools. 
This work is relevant not only to other researchers but also to clinicians and the medical industry in general.


## Description of the project
The project uses Machine Learning to predict
- 1. The Predisposition to genetic diseases in humans using a simulated dataset
- 2. Local adaptation of livestock using Cattle genetic data from Uganda

A summary of the project and its deliverables can be found [here](Explanation.ipynb)


## Scripts and Results
- [Genetic predisposition to a simulated disease in humans](Scripts/RandomForest_HumanSimulation.ipynb)
- [Environmental adaptation in Ugandan Cattle](Scripts/UGBT.ipynb)
- Other scripts can be found in the `Scripts/` folder, or directly through the [Project Description page](Explanation.ipynb)


## Data
- Datasets for human simulations and Ugandan Cattle can be found in `Data_Sim/` and `Data_UGBT/` respectively


## Future improvements
- Compare current results with [variant spark](https://github.com/aehrc/VariantSpark), a fast and scalable Random Forest Classifier.
- Compare current results with a Deep learning approaches. [For example](https://www.mdpi.com/2073-4425/10/7/553/pdf)
- Interactive manhattan plots and maps of global distribution.


