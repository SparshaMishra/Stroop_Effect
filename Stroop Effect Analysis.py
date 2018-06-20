
# coding: utf-8

# # Stroop Effect 

# In a Stroop task, participants are presented with a list of words, with each word displayed in a color of ink. The participant’s task is to say out loud the color of the ink in which the word is printed. The task has two conditions: a congruent words condition, and an incongruent words condition. In the congruent words condition, the words being displayed are color words whose names match the colors in which they are printed: for example RED, BLUE. In the incongruent words condition, the words displayed are color words whose names do not match the colors in which they are printed: for example PURPLE, ORANGE. In each case, we measure the time it takes to name the ink colors in equally-sized lists. Each participant will go through and record a time from each condition.

# ### Q1. What is our independent variable? What is our dependent variable?

# ANS - The independent variable is the word which is printed.
#       The dependent variable is the time that the participant takes to read out the color of the ink of the word that is printed. 

# ### Q2. What is an appropriate set of hypotheses for this task? What kind of statistical test do you expect to perform? Justify your choices.

# ANS - The appropriate set of hypothesis for this task in my case is Null Hypothesis (H0) which means that there is no change. A Null Hypothesis says that there is no difference in the time taken to perform both the tasks. But according to the Stroop Task, the Alternative Hypothesis (H1) would be that the incongruent task takes more time than the congruent task. It is a harder task for the participant to say the color out loud without reading word that is printed with it. Here we are assuming that the incongruent task will be taking more time than the congruent task. 
# 
# In this case, I will be performing a t-test because we do not know the population standard deviation and the sample set is less than 30. The t-test that will be performed is a one tailed t-test where the Alternative Hypothesis is that the participant's incongruent sample mean is going to be larger than the participant's congruent sample mean. 

# ### Q3. Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability.

# ANS - The Sample Size is - 24 
# 
# The Mean is - $xbar = \Sigma{x}/n$ 
#                   (Here the xbar is the Sample Mean, x is the value and n is the sample Size) 
#                   
#       Congruent: 14.05
#       Incogruent: 22.02
#     
# Median of the table is - 
#       Congruent: 14.3565
#       Incongruent: 21.0175
#       
# Sample Standard Deviation: $\sigma = \Sigma{(x - xbar)^2}/n$
# 
#       Congruent: 3.559358 
#       Incongruent: 4.797057

# In[51]:


# Import the Libraries 
from scipy import stats
import math
from scipy.stats import t
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Enable inline viewing of graphs
get_ipython().run_line_magic('matplotlib', 'inline')

# Load the data from csv file
stroop_path = "https://raw.githubusercontent.com/SparshaMishra/Stroop_Effect/master/stroopdata.csv"

# Parse the csv into pandas data structures
df = pd.read_csv(stroop_path)
congruentSeries = df['Congruent']
incongruentSeries = df['Incongruent']

# Display the table
df


# In[43]:


df.describe()


# ###### Central Tendency 

# As we can observe from the above table that the mean of the congruent condition is 14.051125 and the mean of the incongruent condition is 22.015917

# ###### Variability

# Here we can observe that the standard deviation for the congruent condition is 3.559358 and for incongruent condition is 4.797057

# ###### Q4. Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.

# In[24]:


# Box plots for both the conditions
title = 'Box Plot for both the Conditions'
kind = 'box'
dataFrame.plot(title=title, kind=kind)
ylabel = plt.ylabel('Time (in seconds)')


# The above visualization of a box plot shows that the incongruent condition has two outliners, where both the outliner participants took longer time than the other participants in incongruent conditions. The result of these two conditions are shown in the form of a histogram below, where we can observe a uniform right shift from the congruent condition to the incongruent condition.

# In[38]:


# Histogram of the Congruent Condition
title = 'Histogram of the Congruent Condition'
kind = 'hist'
plot = congruentSeries.plot(title=title, kind=kind, bins=7)
xLabel = plt.xlabel('Time (in seconds)')
window = plt.axis([0,48,0,7])


# In[37]:


# Histogram of the Incongruent Condition
title = 'Histogram of the Incongruent Condition'
kind = 'hist'
plot = incongruentSeries.plot(title=title, kind=kind)
xLabel = plt.xlabel('Time (in seconds)')
window = plt.axis([0,48,0,7])


# In[36]:


# Histogram of Both the Conditions
title = 'Histogram of Both the Conditions'
kind = 'hist'
alpha = 0.5
plot = df.plot(title=title, kind=kind, alpha=alpha, bins=12)
xLabel = plt.xlabel('Time (in seconds)')
window = plt.axis([0,48,0,7])


# ### Q5. Now, perform the statistical test and report your results. What is your confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?

# In[48]:


# To get the t-critical value for a 95% confidence level and 23 d.f
t.ppf(.95, 23)


# Here we can see that for confidence level of 95%, the t-critical value is 1.7139

# The point estimate for the difference of the mean is 22.02 - 14.05 = 7.97

# In[49]:


df['Difference'] = df['Congruent'] - df['Incongruent']
df['Difference'].std(axis=0)


# Here we have calculated the standard deviation

# Now let us calculate t-statistic

# In[52]:


7.97/(4.8648 / math.sqrt(24))


# We observe here that our t-statistic is 8.02 which is much greater than our critical value which is 1.713. This is why we will be rejecting the Null Hypothesis. 

# So it is proved that it does take a much longer time in the incongruent condition performed by the participants than in the congruent condition. 

# I can now say that the results do match up to my expectations 

# ### 6. Optional: What do you think is responsible for the effects observed? Can you think of an alternative or similar task that would result in a similar effect? Some research about the problem will be helpful for thinking about these two questions!

# In my opinion, I guess it is our subconsciousness and our stimuli response in the brain which automatically registers the word that is right in front of us. It is easily registered by the brain as the color of the word and the word displayed match with each other. But when the color and the word that is displayed are not the same, our brain takes time to register and first registers the word and then focuses on the color which causes error and thus takes more time to provide the correct response.
# 
# 

# Another similar task can be that we have to say the number of times the word is present in front of us. 
# Like for example "one" , here our answer will be 1. 
# But when it is displayed "one one", our mind registers the word "one" first and the count which is 2, later. 

# ### Reference

# 
# https://en.wikipedia.org/wiki/Stroop_effect
# 
# http://www.statisticshowto.com/t-statistic/
# 
# http://www.statisticssolutions.com/manova-analysis-paired-sample-t-test/
