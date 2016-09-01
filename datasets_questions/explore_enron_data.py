#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import pandas as pd

import tools.feature_format as ff

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "Number of employees " + `len(enron_data)`
print "Number of attributes " + `len(enron_data[enron_data.keys()[0]])`

enron_df = pd.DataFrame(enron_data).T
print enron_df.head()

print "Number of poi employess " + `len(enron_df[enron_df.poi == True])`

print "James Prentice total stcok value = " + `enron_data['PRENTICE JAMES']['total_stock_value']`
print "Emails from Wesley Colwell to POI : " + `enron_data['COLWELL WESLEY']['from_this_person_to_poi']`
print "Stock Options for Jeffrey K Skilling : " + `enron_data['SKILLING JEFFREY K']['exercised_stock_options']`

print enron_df[enron_df['total_payments'] != 'NaN'].sort(['total_payments'], ascending=False).head(20)
print enron_df.loc[['SKILLING JEFFREY K', 'LAY KENNETH L', 'FASTOW ANDREW S'], 'total_payments'].sort_values(ascending=False)

print "Number of employess with quantifiable salary " + `len(enron_df[enron_df.salary != 'NaN'])`
print "Number of employess with quantifiable email " + `len(enron_df[enron_df.email_address != 'NaN'])`

feature_list = ["poi", "salary", "bonus"]
print ff.targetFeatureSplit(ff.featureFormat(enron_data, feature_list))

print "Percentage with no payments " + `100*len(enron_df[enron_df.total_payments == 'NaN'])/len(enron_df)`