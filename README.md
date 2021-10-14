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
