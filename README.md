# Project Proposal

## Group Members:
- Joanna Shen
- Monica Zheng
- Wenxin Cai

## Abstract
We would like to predict how vulnerable a person is to several most common deadly diseases including lung cancer, large intestine cancer, cervical cancer etc. and present the result on a webapp. To achieve this objective, we would first collect large data sets of the listed diseases’ patients. Then, we would use machine learning to identify the top ten relevant factors contributing to a certain disease such as the frequency of smoking cigarettes and the sleeping schedules. Finally, a “risk index” will be calculated for each user.

## Planned Deliverables
We aim to create an interactive webapp that allows the users to choose a certain disease, key in their own data and receive a “risk index” that indicates the possibility of suffering from that disease and several personalized infographics regarding the particular disease.

### Scenario 1: Full Success
* An interactive webapp with carefully-designed attractive interfaces
* Users being directed to different interfaces based on their input
* A wide range (>=10) of deadly diseases’ predictions
* Higher accuracy of predictions compared to professional medical advice
* Comparison between general population’s data and patients’ data on different risk factors through visualization
* Providing follow-up advice

### Scenario 2: Partial Success
* An interactive webapp with a single attractive interface
* Predicting a single disease 
* High accuracy compared to professional medical advice
* Providing follow-up advice

## Resources Required
We need large data sets about patients of our desired list of diseases covering both their lifestyle and medical information. For example, for cervical cancer, we would include data on age, number of sexual partners, first sexual intercourse (age), number of pregnancies, smokes (packs/year) etc., as shown in https://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29, and large data sets about the general population including both their lifestyle and medical information.

## Tools and Skills Required
- Machine learning to select the most important features
    - Packages: pandas, scikit-learn, tensorflow, numpy
- Database management to clean and prepare the data to be used
    - Packages: pandas,  sqlite, numpy
- Advanced interactive visualization techniques to make our graphics more understandable and appealing
    - Packages: plotly, matplotlib
- Webapp design
    - Packages: django, ....

## What You Will Learn
We will learn about
* How to design, create, and maintain a webapp with the above-mentioned python packages
* How to clean up and deal with large data sets and interaction with databases
* How to improve prediction accuracy through machine learning
* How to visualize more complicated data
* How to version control through git and GitHub
* How to detect and prevent the development of specified diseases

## Risks
- Lack of accessibility to appropriate data sets
- Difficulty in identifying the most important risk factors with a higher accuracy
- Difficulty in creating multiple interfaces in the webapp

## Ethics
While white patients might benefit from the existence of our product, patients of color might be harmed by our product. Due to pre-existing inequality, patients of color have less access to health care and medical services than white patients. As a result, the available data sets online mostly consist of data on white patients and therefore our webapp might be influenced by the inherent bias and not be able to produce highly accurate predictions for other groups of patients. This could exacerbate the inequality in access to accurate and timely disease diagnosis between patients of color and white patients. 
Overall, we believe that the existence of our health-related product is very likely to make the world a better place by raising people’s awareness of early-stage cancer prevention, the relationship between daily habits and disease development, and the long-term benefit of getting relevant vaccinations. Our assumptions are listed as follows:
1. The commonality among patients of a certain disease will enable our model to predict the probability of a new individual suffering from the disease with high accuracy.
2. Early-stage cancer detection can prevent the disease’s rapid development and would therefore increase people’s life expectancy and make the world a better place.

## Tentative Timeline
### In 2 weeks, we hope to:
Collect, prepare, and clean the data set
Learn the basics of making a webapp
Finalize the list of diseases to be analyzed

### In 4 weeks, we hope to:
Finish feature selection through machine learning for each disease
Find the type of visualization that would best present the comparison of risk factors between general population’s data and patients’ data
Construct the basic structure of our webapp

### In 6 weeks, we hope to:
Ensure the webapp successfully accepts inputs and gives outputs for a single disease
Plot relevant figures of the general population’s data and patients’ data
Realize the transition between different interfaces

### In 8 weeks, we hope to:
Ensure the webapp runs smoothly for all listed diseases
Add the previously plotted figures to the webapp
Add appropriate advice for each user in the webapp
Make the webapp more attractive and good-looking
