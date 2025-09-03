#### Description
This table serves as the central identity management for all Patients in the database. It contains records that uniquely identify each patient, and some demographic information.<br>

#####CNIL compliant warehouse
This data model was published before the [CNIL referential for health data warehouse](https://www.cnil.fr/fr/la-cnil-adopte-un-referentiel-sur-les-entrepots-de-donnees-de-sante). 
Some fields are not used to comply with the obligation to separate directly identifying data from clinical data (SEC-LOG-4)

#####Merged patient
In some data source, a patient can be recorded multiple times. 
You can use the `is_merged` and `merged_into` fields to control patient merges. 
A merged patient should not have associated data in other tables. 

#### Columns

{{ read_csv('csv/dwh_patient.csv') }}
