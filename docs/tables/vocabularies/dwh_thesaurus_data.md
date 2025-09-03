#### Description
This table stores the standardized set of concepts used to represent medical data within the data warehouse. 
It acts as a controlled vocabulary for coding clinical information, laboratory tests, procedures, diagnoses, and medications, covering multiple classification systems (e.g., CIM10, CCAM, ATC, local lab codes). 
Each record represents a unique concept with associated metadata to describe its meaning, structure, permissible values, and usage in the dataset.

#### Columns
{{ read_csv('csv/dwh_thesaurus_data.csv') }}
