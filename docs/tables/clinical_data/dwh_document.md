#### Description
This table contains unstructured clinical documents and reports associated with a patient’s healthcare encounter. 
Each record corresponds to a single document instance, such as a clinical report, observation note, or questionnaire form. 
The table captures the document content as free text together with key metadata including the author, the date of creation, the type of document, and the healthcare context in which it was generated (e.g., visit, service, or care unit).

#### Columns
{{ read_csv('csv/dwh_document.csv') }}
