import json
import csv
import pandas as pd

converter = [
  {
    "Date": "2022-03-01",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": 1515.0,
    "Specific Energy Consumption": 0.0,
    "Specific Energy Cost": 0.0,
    "Specific Energy Emission": 0.0
  },
  {
    "Date": "2022-03-02",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": 1515.0,
    "Specific Energy Consumption": 0.0,
    "Specific Energy Cost": 0.0,
    "Specific Energy Emission": 0.0
  },
  {
    "Date": "2022-03-03",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-04",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-05",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-06",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-07",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-08",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-09",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-10",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-11",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-12",
    "Unit": "kg",
    "Gas Consumption": 989,
    "Gas Energy Cost": 1978,
    "Gas GHG Emission": 1.731,
    "Running Hours": 4,
    "Off Hours": 20,
    "Per Hour Consumption": 273,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-13",
    "Unit": "kg",
    "Gas Consumption": 1371,
    "Gas Energy Cost": 2742,
    "Gas GHG Emission": 2.399,
    "Running Hours": 5,
    "Off Hours": 19,
    "Per Hour Consumption": 273,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-14",
    "Unit": "kg",
    "Gas Consumption": 1397,
    "Gas Energy Cost": 2794,
    "Gas GHG Emission": 2.445,
    "Running Hours": 4,
    "Off Hours": 20,
    "Per Hour Consumption": 326,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-15",
    "Unit": "kg",
    "Gas Consumption": 1400,
    "Gas Energy Cost": 2800,
    "Gas GHG Emission": 2.45,
    "Running Hours": 7,
    "Off Hours": 17,
    "Per Hour Consumption": 203,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-16",
    "Unit": "kg",
    "Gas Consumption": 1375,
    "Gas Energy Cost": 2750,
    "Gas GHG Emission": 2.406,
    "Running Hours": 3,
    "Off Hours": 21,
    "Per Hour Consumption": 482,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-17",
    "Unit": "kg",
    "Gas Consumption": 1379,
    "Gas Energy Cost": 2758,
    "Gas GHG Emission": 2.413,
    "Running Hours": 6,
    "Off Hours": 18,
    "Per Hour Consumption": 243,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-18",
    "Unit": "kg",
    "Gas Consumption": 1390,
    "Gas Energy Cost": 2780,
    "Gas GHG Emission": 2.433,
    "Running Hours": 6,
    "Off Hours": 18,
    "Per Hour Consumption": 228,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-19",
    "Unit": "kg",
    "Gas Consumption": 997,
    "Gas Energy Cost": 1994,
    "Gas GHG Emission": 1.745,
    "Running Hours": 4,
    "Off Hours": 20,
    "Per Hour Consumption": 232,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-20",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-21",
    "Unit": "kg",
    "Gas Consumption": 885,
    "Gas Energy Cost": 1770,
    "Gas GHG Emission": 1.549,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 2124,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-22",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-23",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-24",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-25",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-26",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-27",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-28",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-29",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-30",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  },
  {
    "Date": "2022-03-31",
    "Unit": "kg",
    "Gas Consumption": 0,
    "Gas Energy Cost": 0,
    "Gas GHG Emission": 0.0,
    "Running Hours": 0,
    "Off Hours": 24,
    "Per Hour Consumption": 0,
    "Production": "Production value not available",
    "Specific Energy Consumption": 0,
    "Specific Energy Cost": 0,
    "Specific Energy Emission": 0
  }
]

#converting json to csv over here
with open('snippets/json/convert_to_csv.json') as json_file:
    jsondata = json.load(json_file)
 
data_file = open('jsonoutput.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
 
count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(data.values())
 
data_file.close()

#Converting csv to excel from here 

df_new = pd.read_csv('jsonoutput.csv')
 
# saving xlsx file
GFG = pd.ExcelWriter('outputexcel.xlsx',engine='xlsxwriter')

df_new.to_excel(GFG, index=False)

workbook  = GFG.book
format = workbook.add_format()
border_format = format.set_border()
format.set_align('center')
format.set_align('vcenter')
format.set_border(1)
worksheet = GFG.sheets['Sheet1']
worksheet.set_column(0, 13, 20,format)

GFG.save()