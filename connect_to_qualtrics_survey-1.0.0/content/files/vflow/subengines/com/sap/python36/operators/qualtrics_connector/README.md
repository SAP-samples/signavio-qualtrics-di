# Py3 Qualtrics Operator (v1.3)

* Connect SAP DI to Qualtrics API
* Fetch data from survey, optionally starting from given date
* Return csv and json file strings

## Ports
* ### Input
  * None

* ### Output
  * **print** (type: basic.string)
  * **csvOutput** (type: basic.string)
  * **jsonOutput** (type: basic.string)

## Tags

* **aiohttp** (version: (No version))
* **aiohttp** (version: (No version))

## Configuration

* **qualtrics_connection** - (type: object, required) Input Connection to Qualtrics
* **surveyID** - (type: string, required) Survey ID
* **useDate** - (type: boolean, required, default=False) Fixed start date to use for download
* **startDate** - (type: string, optional)

## References
* https://blogs.sap.com/2021/03/08/sap-data-intelligence-integration-with-qualtrics/