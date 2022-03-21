Method = {}
with open('Dades.xlsx’, mode='rb') as fname:
    dfe = pd.read_excel(fname, sheet_name='MethodOutput')

for rowid in range(len(dfe)):
    row = dfe.iloc[rowid]

    my_id = row["MethodID"]
    if my_id not in method:
        method[my_id] = {
                         "MethodID": row["MethodID"],
                         "FeatSelection": row["FeatSelection"],
                         "FeatDescription": row["FeatDescriptor"]
                         "Classifier": row["Classifier"]
		    “Experiment”: [ { "Repetition": row["Repetition"],
                         "Train": row["Train"],
                         "BenignPrec": row["BenignPrec"]
                         "BenignRec": row["BenignRec"]
                         "MalignRec": row["MalignPrec"]
                         "MalignPrec": row["MalignRec"]
                         }]
                                 }
  else:
        new_dict = { "Repetition": row["Repetition"],
                         "Train": row["Train"],
                         "BenignPrec": row["BenignPrec"]
                         "BenignRec": row["BenignRec"]
                         "MalignRec": row["MalignPrec"]
                         "MalignPrec": row["MalignRec"]
                         }
        method[my_id]["Experiment"].append(new_dict)
