# Matemàtica Computacional i Analítica de Dades - 2022
1. [Cèlia Martínez, NIU: 1569504, Github user: celia-m15](https://github.com/celia-m15) 
2. [Marta Matute, NIU 1496672, Github user: Marta-Matute](https://github.com/Marta-Matute)
3. [Goretti Peña, NIU: 1566866, Github user: gorettipena](https://github.com/gorettipena)
5. [Judit Ugas, NIU: 1569163, Github user: Juditu](https://github.com/Juditu)

## Introduction
In this repository we find a project where we work with the design, implementation and queries for a database in MongoBD. We'll use data about Lung Cancer Detection, taken from the research funded by ATTRACT in the project ToPiomics, Radiomics for Early Detection of Lung Cancer. 

## Goals
Our main objective for this project will be to create a data base using MongoDB in such way that we can answer the following queries:
1. Different Scanners that we find on the data base. Sow the device.
2. Total number of nodules used for the training in experiment 1 of method 2. 
3. Maximum, minimum and average value for Benign Precision grouped by classification. Show the method ID, maximum benign precision, minimum benign precision and average benign precision. 
4. Total number of men and women. Show gender and total number.
5. Patients with more than two nodules. Show Patient's ID, gender, age and diagnosis. 
6. Show the 4 methods with the most repetitions in the experiment. Show the Method's ID and the number of repetitions for the experiment. 
7. For each of patient, the number of scanners that were done. Show the patient's ID, device and date of the computed tomography. 
8. Show the patients whose all nodules are Benign and the total count. 
9. Modify the parameter ResolutionTV increasing it by 20% from the scans that took place on 18/11/2018.

## Explanation for files in the repository 
Data:
  - Dades.xlsx
    All the data to sort in the correct way
  - JocDeProves.xlsx
    All the queries explained abovve solved
Reading:
  - data_reading.py
    A Python file used to read all data, put in the correct way (with corresponding entities) and update in MongoDB server.
Test:
  - Joc de proves - JSON queries
    A JSON file used to test data and if data is organized correctly.
    
 ## Explanation for entities
 We considered to split data in 4 different collections. Those are Patient, Nodules, CtScanner and Method.
 
In the collection Patient is saved the information of the entity Patient, as age, gender, etc. Apart of the entity key "NoduleID" and nodul Diagnosis. We have added diagnosis of nodule to access this information more quickly, as we considered it important.
 
 In the collection Nodules is saved the rest of the information about Nodules, and is related with the entity CTScanner and Method. To save the data is used a dictionary with 2 keys, PatientID and NoduleID. Each row has more than one experiment. In that case is applied subset pattern as it allows us to more easily access the information that we consider most relevant and that we will consult more frequently.
 
 In the collection CtScanner is saved all data related to Scanner, as device used, resolution, etc.

Finally, we have created the Method collection which contains information from Method and Experiment entities. For this collection we have considered applying the attribute pattern by creating a list of all the experiments that have been performed for each method.
