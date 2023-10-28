# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_app.py'.

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


@st.cache_data
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race', 'gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()
 
# Write your code to filter streamlit warnings 
st.set_option("deprecation.showPyplotGlobalUse", False)

# Write the code to design the web app

# Add title on the main page and in the sidebar.
st.title("Census Data Visualisation Web App")
st.sidebar.title("Census Data Visualisation")
# Using the 'if' statement, display raw data on the click of the checkbox.
if st.sidebar.button('Display Raw data'):
  st.subheader("Census Data Set")
  st.dataframe(census_df)
  st.write("Number of Rows: ", census_df.shape[0])
  st.write("Number of Columns: ", census_df.shape[1])
# Add a multiselect widget to allow the user to select multiple visualisations.
# Add a subheader in the sidebar with the label "Visualisation Selector"
st.sidebar.subheader("Visualisation Selector")

# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
# Store the current value of this widget in a variable 'plot_list'.
plot_list = st.sidebar.multiselect('Select the plots/charts', ('Pie Chart', 'Box Plot', 'Count Plot'))

# Display pie plot using matplotlib module and 'st.pyplot()'
if 'Pie Chart' in plot_list:
  st.subheader("Pie Chart")
  pie_data = census_df['income'].value_counts()
  explode = [0, 0.15]
  plt.figure(figsize = (16, 6))
  plt.pie(pie_data, labels = pie_data.index, autopct = '%1.2f%%', explode = explode ,startangle = 30,wedgeprops = {'edgecolor' : 'red'} )
  plt.title("Distribution of records for the income-group features")
  st.pyplot()
  
  pie_data = census_df['gender'].value_counts()
  plt.figure(figsize = (16, 6))
  plt.pie(pie_data, labels = pie_data.index, autopct = '%1.2f%%', explode = explode,startangle = 30,  wedgeprops = {'edgecolor' : 'red'})
  plt.title("Distribution of records for the gender features")
  st.pyplot()

# Display box plot using matplotlib module and 'st.pyplot()'
if 'Box Plot' in plot_list:
  st.subheader("Box Plot")
  plt.figure(figsize = (16, 6))
  sns.boxplot(x = 'hours-per-week', y = 'income', data = census_df)
  plt.title("Showing the difference in the range of values for the hours-per-week feature for different income groups.")
  st.pyplot()

  plt.figure(figsize = (16, 6))
  sns.boxplot(x = 'hours-per-week', y = 'gender', data = census_df)
  plt.title("Showing the difference in the range of values for the hours-per-week feature for different gender groups.")
  st.pyplot()

# Display count plot using seaborn module and 'st.pyplot()' 
if 'Count Plot' in plot_list:
  st.subheader("Count plot")
  plt.figure(figsize = (16, 6))
  sns.countplot(x = 'workclass', hue = 'income', data = census_df)
  plt.title("Showing the count of a number of records for unique workclass feature values for different income groups.", fontsize = 15)
  st.pyplot()

