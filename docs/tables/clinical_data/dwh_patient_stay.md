#### Description
This table records each encounter or visit a person has with the healthcare system and serves as a central link to other clinical events.

#####CNIL compliant warehouse
This data model was published before the [CNIL referential for health data warehouse](https://www.cnil.fr/fr/la-cnil-adopte-un-referentiel-sur-les-entrepots-de-donnees-de-sante). 
Some fields are not used to comply with the obligation to separate directly identifying data from clinical data (SEC-LOG-4)

#### Columns
{{ read_csv('csv/dwh_patient_stay.csv') }}
