write a thorough demonstration of the functionality of your project in the top-level README.md file. Think of this as a tutorial for someone who wants to learn to use your tools. 

If you created a webapp or other project for which the user is not expected to directly interact with code, you may instead use this space to carefully describe what your app does and what its limitations might be. 

including careful instructions on how I can run the app and what I should do to observe its functionality. 


# Introduction

Our overall objective of the project is to predict whether an individual is at risk of getting cardiovascular disease given his personal data. Our project has two parts:

## Part 1: Data Visualization and Machine Learning

This part can be found in the `health-inspector.ipynb` notebook file. 

We start by accessing a cardiovascular disease data set. The data file `cardio-train.csv` is in the directory called `data`. Then we visualize the data with a heatmap, a box-and-whisker plot, and a kernel density estimate (KDE) plot to find whether correlations exist between different features in the data set and whether outliers exist in the data set. Next, we use these results to clean the data set for better model perfomance.

In the machine learning part, we create three different models:

- a sequential model using five columns with the highest correlation scores based on the heatmap as predictor data
- a sequential model using all of the columns as predictor data
- a multinomial logistic regression model using all of the columns as predictor data

In all of the three models, target data is whether a patient has cardiovascular disease.

Through lots of experiments, we achieve the highest accuracy with the multinomial logistic regression model and decide to incorporate this model into our webapp by pickling.


## Part 2: Webapp Development

![root.jpg](/images/root.jpg)

![input1.jpg](/images/input1.jpg)

![result1.jpg](/images/result1.jpg)

![input2.jpg](/images/input2.jpg)

![result2.jpg](/images/result2.jpg)