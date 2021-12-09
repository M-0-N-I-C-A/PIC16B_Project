# Introduction

Our overall objective of the project is to predict whether an individual is at risk of cardiovascular disease based on his personal data. Our project has the following two parts.

## Part 1: Data Visualization and Machine Learning

This part can be found in the `cardio-plt-ml.ipynb` notebook file. 

We start by accessing a cardiovascular disease data set that contains standard health information and information on the presence/absence of cardiovascular disease for over 70,000 patients. The data file `cardio_train.csv` is in the directory called `data`. Then we visualize the data with a heatmap, a box-and-whisker plot, and a kernel density estimate (KDE) plot to find whether correlations exist between different variables in the data set and whether outliers exist in the data set. Next, we use these results to clean the data set for better modeling perfomance.

In the machine learning part, we create three different models:

- a `Sequential` model using the five columns with the highest correlation scores based on the heatmap as predictor data
- a `Sequential` model using all of the columns as predictor data
- a multinomial logistic regression model using all of the columns as predictor data

In all of these three models, target data is whether a patient has cardiovascular disease or not.

Through lots of experiments, we achieve the highest accuracy with the multinomial logistic regression model and decide to incorporate this model into our webapp by pickling.


## Part 2: Webapp Development

Our webapp allows a user to input his personal information and will predict whether he is at risk of cardiovascular disease based on the multinomial logistic regression model.

Here's our home page:

![root.jpg](/images/root.jpg)

After clicking the `Submit your information`, users will be directed to the submission page to input their personal information.

Here're two examples of two different results our webapp will show based on different user input:

- Tom is our first user.

![input1.jpg](/images/input1.jpg)

He inputs his information as shown in the above image and clicks the `Submit information` button.

![result1.jpg](/images/result1.jpg)

As shown in this above image, our webapp predicts that he is healthy, i.e. not at risk of cardiovascular disease, based on the model.

- Amy is our second user.

![input2.jpg](/images/input2.jpg)

She inputs her information as shown in the above image and clicks the `Submit information` button.

![result2.jpg](/images/result2.jpg)

As shown in this above image, our webapp predicts that she is at risk of cardiovascular disease and suggests that she had better go to see her doctor.

We recognize that our app might have the following limitations:

- Since the accuracy of the multinomial logistic regression model is 73% on the test data set, our webapp may make inaccurate predictions and provide incorrect suggestions for our users.

- Since we have not deployed our webapp online by Heorku, other people do not have direct access to our webapp.