#### Description
This table stores the history of identifier for a patient (IPP). 
A patient may have multiple identifiers because they were created in duplicate and then merged in the source or in the warehouse. 
A column specifies which identifier should be displayed to the user.

#####CNIL compliant warehouse
This data model was published before the [CNIL referential for health data warehouse](https://www.cnil.fr/fr/la-cnil-adopte-un-referentiel-sur-les-entrepots-de-donnees-de-sante). <br>
This table is not used in the warehouse as it contains only directly identifying data. 
Nevertheless, it can be used in the identifying part of the warehouse to store patient identifier history.

##### Uniqueness
An identifier should be unique for one center and one software. We have a uniqueness constraint for the combination of the fields `hospital_patient_id`, `instance_ipp_id`, `ipp_origin_code`.

#### Columns
{{ read_csv('csv/dwh_patient_ipphist.csv') }}
