#### Description
This table contains clinical events and observations associated with a patient, including conditions, procedures, laboratory results, drug exposures, and other healthcare-related data. 
Each record represents a single data point with its associated concept, value, temporal attributes, and care context.

#### Columns
{{ read_csv('csv/dwh_data/dwh_data.csv') }}

##### French PMSI Extension Fields
{{ read_csv('csv/dwh_data/dwh_data_pmsi.csv') }}

##### Drug Exposure Extension Fields
{{ read_csv('csv/dwh_data/dwh_data_drugs.csv') }}
