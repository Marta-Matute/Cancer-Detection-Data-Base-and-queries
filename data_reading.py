import pandas as pd

# METHOD
Method = {}
with open('Dades.xlsx', mode='rb') as fname:
    dfe = pd.read_excel(fname, sheet_name='MethodOutput')

for rowid in range(len(dfe)):
    row = dfe.iloc[rowid]

    my_id = row["MethodID"]
    if my_id not in Method:
        Method[my_id] = {"MethodID": row["MethodID"],
                         "FeatSelection": row["FeatSelection"],
                         "FeatDescription": row["FeatDescriptor"],
                         "Classifier": row["Classifier"],
		    	 
                         "Experiment": [{"Repetition": row["Repetition"],
                                         "Train": row["Train"],
                                     	 "BenignPrec": row["BenignPrec"],
                                     	 "BenignRec": row["BenignRec"],
                                     	 "MalignRec": row["MalignPrec"],
                                     	 "MalignPrec": row["MalignRec"],
                                     	}]
                         }
    else:
        new_dict = {"Repetition": row["Repetition"],
                    "Train": row["Train"],
                    "BenignPrec": row["BenignPrec"],
                    "BenignRec": row["BenignRec"],
                    "MalignRec": row["MalignPrec"],
                    "MalignPrec": row["MalignRec"]
                    }
        Method[my_id]["Experiment"].append(new_dict)

	  
# USERS
Patient = {} 
with open('Dades.xlsx', mode='rb') as fname: 
    dfe = pd.read_excel(fname, sheet_name='Cases') 

for rowid in range(len(dfe)): 
    row = dfe.iloc[rowid] 
    my_id = row["PatientID"] 
    if my_id not in Patient: 
        Patient[my_id] = {"PatientID": row["PatientID"], 
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
        Patient[my_id]["Nodules"].append(new_dict) 

#NODULES
def search(dfe, my_id, patient_id, name1, name2):
    for i in range(len(dfe)):
        if(dfe.iloc[i][name1]==my_id and dfe.iloc[i][name2]==patient_id):
            return i
    return -1

Nodules={}
with open('Dades.xlsx', mode='rb') as fname:
    dfe = pd.read_excel(fname, sheet_name='Cases')
    dfe2 = pd.read_excel(fname, sheet_name='Training')

for rowid in range(len(dfe)):
    row = dfe.iloc[rowid]
    #valor_del_camp = row["nom_camp"]
    my_id = row["NoduleID"]
    patient_id = row["PatientID"]
    my_id2 = search(dfe2, my_id, patient_id, 'NodulID', 'PatientID')
    row2 = dfe2.iloc[my_id2]
   
    if (my_id or my_id2) not in Nodules:
        Nodules[my_id2] = { 'PatientID': row['PatientID'],
                            "NoduleID": row["NoduleID"],
                            "DiagnosisNodul": row['DiagnosisNodul'],
                            'Position': {'X': row['PositionX'], 'Y': row['PositionY'], 'Z': row['PositionZ']},
                            'CtScanner': {'CTID': row['CTID'], 'Diammeter': row['Diameter (mm)']},
                            'Experiment': {'MethodID': row2['MethodID'],
                                           'ExperimentRepetition': row2['ExperimentRepetition'],
                                           'RadiomicsDiagnosis': row2['RadiomicsDiagnosis'],
                                           'Train': row2['Train']
                                           }
                          }
