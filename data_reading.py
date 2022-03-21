# METHOD
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
                         "FeatDescription": row["FeatDescriptor"],
                         "Classifier": row["Classifier"],
		    	 “Experiment”: [{ "Repetition": row["Repetition"],
                         		"Train": row["Train"],
                         		"BenignPrec": row["BenignPrec"],
                         		"BenignRec": row["BenignRec"],
                         		"MalignRec": row["MalignPrec"],
                         		"MalignPrec": row["MalignRec"],
                         		}]
                         }
  else:
        new_dict = { "Repetition": row["Repetition"],
                         "Train": row["Train"],
                         "BenignPrec": row["BenignPrec"],
                         "BenignRec": row["BenignRec"],
                         "MalignRec": row["MalignPrec"],
                         "MalignPrec": row["MalignRec"]
                         }
        method[my_id]["Experiment"].append(new_dict)

	  
# EXPERIMENT
Experiments = {}
with open('Dades.xlsx’, mode='rb') as fname: 
	dfe = pd.read_excel(fname, sheet_name='MethodOutput') 

for rowid in range(len(dfe)): 
    row = dfe.iloc[rowid] 
    my_id = row["Experiment"] 
    if my_id not in Experiments: 
	Experiments[my_id] = { 
                         "Repetition": row["Repetition"], 
                         "Train": row["Train"], 
                         "BenignPrec": row["BenignPrec"], 
                         "BenignRec": row["BenignRec"],
                         "MalignRec": row["MalignPrec"], 
                         "MalignPrec": row["MalignRec"] 
                         } 
	  
# USERS
Users={} 
with open('Dades.xlsx', mode='rb') as fname: 
    dfe = pd.read_excel(fname, sheet_name='Cases') 

for rowid in range(len(dfe)): 
    row = dfe.iloc[rowid] 
    my_id = row["PatientID"] 
    if my_id not in users: 
        users[my_id] = { 
                "PatientID": row["PatientID"], 
                "Age": int(row['Age']), 
                "Gender": row["Gender"], 
                "DiagnosisPatient": row["DiagnosisPatient"], 
                "Nodules": [{"NoduleID": row["NoduleID"], 
                            "DiagnosisNodul":  row["DiagnosisNodul"] 
                            }] 
                } 

    else: 
        new_dict = {'NoduleID': row["NoduleID"],  
        "DiagnosisNodul": row["DiagnosisNodul"]} 
        users[my_id]["Nodules"].append(new_dict) 
