# Signavio Data Ingestion Operator

* Push data to Signavio Ingestion API
* Get data as CSV, transform data accordingly to fit to Signavio requirements
* Automatically create schema-file for Signavio to understand data in the right way

## Ports
* ### Input
  * **csvInput** (type: basic.string)

* ### Output
  * **print** (type: basic.string)
  * **stopping** (type: basic.string)

## Tags

* **aiohttp** (version: (No version))

## Configuration

* **table_name** - (type: string, required) Give a name how the table of the imported data should be called
* **signavio_connection** - (type: object, required) Input Connection: Signavio 
* **primary_key** - (type: string, optional) give column name of the primary key. optional, if not set the first column in the csv will be used.
* **custom_schema** - (type: boolean, required, default=False) The user has the option to select between a fully custom setting creation for file formatting, and a semi-automated file formatting. "True" will require the user to provide a full data schema and primary key
* **data_schema** - (type: string, optional) provide schema how to convert data into signavio preferred format (please also see the Signavio documentation about schema files https://documentation.signavio.com/beta/process-intelligence/ingestion-api.htm)
* **from_qualtrics** - (type: boolean, optional, default=True) If Qualtrics is the datasource for the data to be ingested, data formatting is easier as certain assumptions about date-time formats and datatypes are made.
* **datetime_columns** - (type: array of strings, optional) Columns of the input csv which should be transformed as datatime-type data columns
* **datetime_format** - (type: string, optional) Specify here the format in which the data in the datetime-type columns can be expected, e.g "%Y-%m-%d %H:%M:%S" (Python DateTime Format, for more information visit https://pythonexamples.org/python-datetime-format/)

## References
* https://blogs.sap.com/?p=1569297?url_id=text-global-profile-inbox-mod
* https://documentation.signavio.com/beta/process-intelligence/ingestion-api.htm