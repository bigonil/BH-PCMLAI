# Welcome to the BH-PCMLAI
Berkeley, Haas School of Business: Professional Certificate in Machine Learning and Artificial Intelligence
``
Projects Protfolio
``


# 1) Exploratory Data Analysis Report: Will Customers Accept the Coupon?

## Introduction:

This exploratory data analysis (EDA) focuses on understanding the factors influencing customers' decisions to accept or reject driving coupons. The analysis involves the use of Python, leveraging various visualization techniques and statistical summaries.

## Dataset Overview:

The dataset includes information about customers, such as age, gender, bar visits, income, and passenger categories. The primary goal is to distinguish characteristics that differentiate customers accepting coupons from those who do not.

## Key Findings:

### 1. Age Distribution:
   - A significant portion of customers falls in the 20-40 age range.
   - No clear distinction in age between customers who accepted and did not accept the coupon.

### 2. Bar Visits and Acceptance:
   - Customers over the age of 25 who visit bars more than once a month are more likely to accept bar coupons.
   - Indicates that socializing activities, like going to bars, may influence coupon acceptance.

### 3. Passenger Categories and Gender:
   - Males are more prevalent than females, especially in categories like 'Friends' and 'Partner.'
   - Impact of passenger categories on coupon acceptance varies.

### 4. Income Distribution:
   - No clear correlation observed between income distribution and coupon acceptance.

### 5. Hypothesis Testing:
   - Chi-square test revealed a significant association between age, bar visits, and acceptance of bar coupons.
   - Rejected the null hypothesis, suggesting a meaningful connection.

### 6. Passenger Type and Coupon Acceptance:
   - Analysis of different passenger types ('Alone', 'Kids', 'Friends', 'Partner') revealed varying acceptance rates.
   - The 'Alone' category showed a distinct pattern.

## Repository:

The code, visualizations, and detailed analysis can be found in the GitHub repository: [[GitHub Repository Link](https://github.com/bigonil/BH-PCMLAI/blob/main/p_assign_app_5_1/prompt.ipynb)].







# 2) Practical Application Assignment 11.1: What Drives the Price of a Car?

## Introduction:

Your goal is to understand what factors make a car more or less expensive. As a result of your analysis, you should provide clear recommendations to your client -- a used car dealership -- as to what consumers value in a used car.

## Dataset Overview:

In this application, you will explore a dataset from kaggle. The original dataset contained information on 3 million used cars. The provided dataset contains information on 426K cars to ensure speed of processing.

## Repository:

The code, visualizations, and detailed analysis can be found in the GitHub repository: [[GitHub Repository Link Practical Application Assignment 11.1](https://github.com/bigonil/BH-PCMLAI/blob/main/practical_application_II/prompt_II.ipynb)].

Use CRISP-DM, which stands for Cross-Industry Standard Process for Data Mining, is a widely used methodology for data mining projects. It provides a structured approach to planning and executing data mining tasks. Below, we detail each phase of the CRISP-DM process, highlighting how it applies to typical data science projects like the one we’ve been discussing involving vehicle price prediction through regression models.

### 1. **Business Understanding**

This initial phase focuses on understanding the project objectives and requirements from a business perspective, and then converting this knowledge into a data mining problem definition and a preliminary plan designed to achieve the objectives.

**Key Tasks:**
- Determine business objectives: Clarify the goals and objectives of the organization seeking to perform the data mining.
- Assess the situation: Understand the current situation, including constraints, assumptions, and other factors.
- Determine data mining goals: Translate the business objectives into data mining goals.
- Produce a project plan: Describe the intended plan for achieving the data mining goals and the initial assessment of tools and techniques.

**Example for Vehicle Price Prediction:**
- **Objective**: Maximize the accuracy of used vehicle price predictions using available data.
- **Data Mining Goal**: Develop a predictive model that estimates prices based on features like make, model, year, odometer reading, etc.

### 2. **Data Understanding**

This phase starts with data collection and proceeds with activities in order to get familiar with the data, to identify data quality issues, to discover first insights into the data, or to detect interesting subsets to form hypotheses for hidden information.

**Key Tasks:**
- Collect initial data: Acquire the data listed in the project resources.
- Describe data: Examine the data and report on its structure, entries, and attributes.
- Explore data: Conduct exploratory data analysis (EDA) to understand the data.
- Verify data quality: Check for missing values, corrupt data, and outliers.

**Example:**
- **Collect Data**: Load data from multiple sources (e.g., CSV files, SQL databases).
- **Explore Data**: Use statistical summaries and visualization tools to understand distributions and relationships.

### 3. **Data Preparation**

The data preparation phase covers all activities needed to construct the final dataset from the initial raw data. Data cleaning is a major part of this phase.

**Key Tasks:**
- Select data: Decide on the data to be used for analysis.
- Clean data: Handle missing data and remove outliers.
- Construct data: Derive attributes, create new attributes if necessary, and complete other transformations.
- Integrate data: Combine data from different sources.
- Format data: Format the data to fit the model requirements.

**Example:**
- **Clean Data**: Impute missing values and smooth out noise.
- **Construct Data**: Create polynomial and interaction features as discussed.

### 4. **Modeling**

In this phase, various modeling techniques are selected and applied, and their parameters are calibrated to optimal values.

**Key Tasks:**
- Select modeling techniques: Choose the statistical or machine learning algorithms to use.
- Generate test design: Create a methodology to evaluate the model's effectiveness.
- Build model: Run the modeling tools to create one or more models.
- Assess model: Evaluate the model(s) according to the evaluation criteria.

**Example:**
- **Build Model**: Develop Lasso and Ridge regression models.
- **Assess Model**: Use cross-validation and metrics like RMSE and \( R^2 \) to evaluate models.

### 5. **Evaluation**

After modeling, this phase evaluates the model, or models, to ensure they meet the business objectives set in the first phase. It is important to review the steps executed to construct the model and be certain it properly achieves the business goals.

**Key Tasks:**
- Evaluate results: Review the model results in the context of business objectives.
- Review process: Assess if there is any important factor or task that has been overlooked.
- Determine next steps: Decide on the necessary steps, whether to proceed to deployment, initiate further iterations, or set up new projects.

**Example:**
- **Evaluate Results**: Confirm that the model meets the business expectations for pricing accuracy.
- **Review Process**: Reflect on the modeling process and identify any potential improvements.

### 6. **Deployment**

The final phase involves deploying the data mining solution to the business. This might include implementing the model within a decision-making process, supplying ongoing maintenance, monitoring, and reporting of the model's performance.

**Key Tasks:**
- Plan deployment: Plan the deployment of the data mining result(s).
- Plan monitoring and maintenance: Establish a method for ongoing monitoring and maintenance of the solution.
- Produce final report: Generate a comprehensive report of the project.
- Review project: Evaluate what went right and what went wrong, lessons learned, and knowledge gained.

**Example:**
- **Plan Deployment**: Integrate the predictive model into the online used car marketplace.
- **Produce Final Report**: Document all methodologies, performances, insights, and recommendations.

# 3) Improving the quality grading of white wine based on its chemical properties

## Introduction:

The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. For more details, consult: http://www.vinhoverde.pt/en/ or the reference [Cortez et al., 2009].  Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

## Dataset Overview:

These datasets can be viewed as classification or regression tasks.  The classes are ordered and not balanced (e.g. there are many more normal wines than excellent or poor ones). Outlier detection algorithms could be used to detect the few excellent or poor wines. Also, we are not sure if all input variables are relevant. So it could be interesting to test feature selection methods.

**Business Problem**
A potential business problem that could be addressed using this dataset is improving the quality grading of white wine based on its chemical properties. Wine quality grading is crucial for vineyards and distributors as it influences pricing, marketing, and sales strategies. However, manual quality assessment can be subjective and inconsistent. Employing a K-Nearest Neighbors (KNN) classification model could standardize quality assessments, making them more objective and reliable. The model would predict the quality rating of a wine based on its chemical attributes, assisting wine producers and sellers in accurately categorizing their products.

**Choice of Metric**
For the KNN model, choosing an appropriate evaluation metric is crucial. Given the problem's nature—a classification task with multiple classes—the accuracy metric is a straightforward and intuitive choice. Accuracy measures the proportion of total correct predictions, which is useful when class distributions are relatively balanced. However, for more insight into model performance across different wine qualities, weighted F1-score would be an excellent metric. The weighted F1-score considers both precision and recall and adjusts for label imbalance by weighting the scores according to the number of true instances for each label, providing a better sense of model performance on minority classes.

## Repository:

The code, visualizations, and detailed analysis can be found in the GitHub repository: [GitHub Repository White Wine](
https://github.com/bigonil/BH-PCMLAI/blob/main/white_whine_quality/try_it_12.1_improving_white_wine.ipynb)


# 4) Practical Application Assignment 17.1: Comparing Classifiers 

## Introduction:
n this third practical application assignment, your goal is to compare the performance of the classifiers (k-nearest neighbors, logistic regression, decision trees, and support vector machines) you encountered in this section of the program. You will use a dataset related to the marketing of bank products over the telephone.

## Dataset Overview:
The dataset you will use comes from the [UCI Machine Learning repository](https://archive.ics.uci.edu/dataset/222/bank+marketing).The data is from a Portuguese banking institution and is a collection of the results of multiple marketing campaigns. You can make use of the [article Links](https://github.com/bigonil/BH-PCMLAI/blob/main/practical_application_III/CRISP-DM-BANK.pdf) for more information on the data and features. The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed. 

There are four datasets: 
1) bank-additional-full.csv with all examples (41188) and 20 inputs, ordered by date (from May 2008 to November 2010), very close to the data analyzed in [Moro et al., 2014]
2) bank-additional.csv with 10% of the examples (4119), randomly selected from 1), and 20 inputs.
3) bank-full.csv with all examples and 17 inputs, ordered by date (older version of this dataset with less inputs). 
4) bank.csv with 10% of the examples and 17 inputs, randomly selected from 3 (older version of this dataset with less inputs). 
The smallest datasets are provided to test more computationally demanding machine learning algorithms (e.g., SVM). 

The classification goal is to predict if the client will subscribe (yes/no) a term deposit (variable y).

## Repository:

The code, visualizations, and detailed analysis can be found in the GitHub repository: [[GitHub Repository Link Practical Application Assignment 17.1](https://github.com/bigonil/BH-PCMLAI/blob/main/practical_application_III/prompt_III.ipynb)].

## Business Understanding:
To compare and plot the performance of the Logistic Regression model against the KNN algorithm, Decision Tree, and SVM models, we'll follow these steps:

1. Load the dataset and perform any necessary preprocessing.
2. Split the data into training and test sets.
3. Train each model on the training data: Logistic Regression, K-Nearest Neighbors (KNN), Decision Tree, and Support Vector Machine (SVM).
4. Evaluate each model on the test set using appropriate metrics, such as accuracy, precision, recall, and F1-score.
5. Plot the performance metrics for each model for comparison.

