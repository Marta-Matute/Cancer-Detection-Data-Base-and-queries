import pandas as pd
from pymongo import MongoClient

mongoUser = ''
mongoPassword = ''
mongoDB = ''

# En execució remota
Host = 'localhost' 
Port = 27017

DSN = "mongodb://{}:{}".format(Host,Port)

conn = MongoClient(DSN)

bd = conn['Cancer']

#Inicialització de les col·leccions

if "Method" not in bd.list_collection_names():
    methods = bd.create_collection('Method')
else:
    methods = bd["Method"]
    methods.drop()

if "Patient" not in bd.list_collection_names():
    patients = bd.create_collection('Patient')
else:
    patients = bd["Patient"]
    patients.drop()
    

if "Nodules" not in bd.list_collection_names():
    nodules = bd.create_collection('Nodules')
else:
    nodules = bd["Nodules"]
    nodules.drop()

# METHODS
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
		    	         "Experiment": [{"Repetition": int(row["Repetition"]),
                                         "Train": int(row["Train"]),
                                     	 "BenignPrec": row["BenignPrec"],
                                     	 "BenignRec": row["BenignRec"],
                                     	 "MalignRec": int(row["MalignPrec"]),
                                     	 "MalignPrec": row["MalignRec"]
                                     	}]
                         }
         
    else:
        new_dict = {"Repetition": int(row["Repetition"]),
                    "Train": int(row["Train"]),
                    "BenignPrec": row["BenignPrec"],
                    "BenignRec": row["BenignRec"],
                    "MalignRec": int(row["MalignPrec"]),
                    "MalignPrec": row["MalignRec"]
                    }
        Method[my_id]['Experiment'].append(new_dict)

for id_dict in Method.keys():
    methods.insert_one(Method[id_dict])


# PATIENTS
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
                          "Nodules": [{"NoduleID": int(row["NoduleID"]), 
                                       "DiagnosisNodul":  row["DiagnosisNodul"] 
                                     }] 
                         }

    else: 
        new_dict = {'NoduleID': int(row["NoduleID"]),  
        "DiagnosisNodul": row["DiagnosisNodul"]} 
        Patient[my_id]["Nodules"].append(new_dict) 

for id_dict in Patient.keys():
    patients.insert_one(Patient[id_dict])



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
    my_id = row["NoduleID"]
    patient_id = row["PatientID"]
    my_id2 = search(dfe2, my_id, patient_id, 'NodulID', 'PatientID')
    row2 = dfe2.iloc[my_id2]
    no_esta = False

    if my_id not in Nodules:
        no_esta = True
    if my_id2 in Nodules:
        if my_id not in Nodules[my_id2]:
            no_esta = True
    if no_esta:
        Nodules[row['PatientID']] = {
                'PatientID': row['PatientID'],
                "NoduleID": int(row["NoduleID"]),
                "DiagnosisNodul": row['DiagnosisNodul'],
                'Position': {'X': int(row['PositionX']), 'Y': int(row['PositionY']), 'Z': int(row['PositionZ'])},
                'CtScanner': {'CTID': int(row['CTID']), 'Diammeter': float(row['Diameter (mm)'])},
                'Experiment': {'MethodID': row2['MethodID'],
                               'ExperimentRepetition': int(row2['ExperimentRepetition']),
                               'RadiomicsDiagnosis': row2['RadiomicsDiagnosis'],
                               'Train': int(row2['Train'])}
                }

for id_dict in Nodules.keys():
    nodules.insert_one(Nodules[id_dict])

conn.close()
