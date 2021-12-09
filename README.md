# Introduction

Our overall objective of the project is to predict whether an individual is at risk of cardiovascular disease given his personal data. Our project has the following two parts.

## Part 1: Data Visualization and Machine Learning

This part can be found in the `health-inspector.ipynb` notebook file. 

We start by accessing a cardiovascular disease data set that contains standard health information and information on the presence/absence of cardiovascular disease for over 70,000 patients. The data file `cardio-train.csv` is in the directory called `data`. Then we visualize the data with a heatmap, a box-and-whisker plot, and a kernel density estimate (KDE) plot to find whether correlations exist between different features in the data set and whether outliers exist in the data set. Next, we use these results to clean the data set for better model perfomance.

In the machine learning part, we create three different models:

- a sequential model using five columns with the highest correlation scores based on the heatmap as predictor data
- a sequential model using all of the columns as predictor data
- a multinomial logistic regression model using all of the columns as predictor data

In all of the three models, target data is whether a patient has cardiovascular disease.

Through lots of experiments, we achieve the highest accuracy with the multinomial logistic regression model and decide to incorporate this model into our webapp by pickling.


## Part 2: Webapp Development

Our webapp allows users to input their personal data and get a prediction on the risk of getting cardiovascular disease based on the model.

This is the home page of our webapp.

![root.jpg](/images/root.jpg)

By clicking the `Submit your information`, users will be directed to a page where they can submit their personal information. 

Here are two examples showing different prediction results based on user input:

- Our first user Tom inputs his information as shown in the next image and clicks the `Submit information` button. As we can see from the second image below, he is predicted by our model that he is healthy, i.e. not at risk of cardiovascular disease.

![input1.jpg](/images/input1.jpg)

![result1.jpg](/images/result1.jpg)

- Our second user Amy inputs her information as shown in the next image and clicks the `Submit information` button. As we can see from the second image below, she is predicted by our model that she is at risk of cardiovascular disease and our webapp gives a suggestion that she had better go to see her doctor.

![input2.jpg](/images/input2.jpg)

![result2.jpg](/images/result2.jpg)

We recognize that our app might have the following limitations:

- Since the accuracy of the multinomial logistic regression model is 73% on the test data set, our webapp may make inaccurate predictions and provide incorrect suggestions for our users.

- Since we have not deployed our webapp online by Heorku, other people do not have direct access to our webapp.