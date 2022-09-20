[![REUSE status](https://api.reuse.software/badge/github.com/SAP-samples/signavio-qualtrics-di)](https://api.reuse.software/info/github.com/SAP-samples/signavio-qualtrics-di)

# SAP Signavio Process Intelligence - SAP Data Intelligence template with Qualtrics Connector

## Description
This repository contains SAP Data Intelligence solutions to enable the connection from Qualtrics to SAP Signavio Process Intelligence through an SAP Data Intelligence pipeline.

For more information, follow this blog post on SAP Community: [Integrating SAP Signavio Process Intelligence and SAP Data Intelligence Cloud: A concrete example with the New Ingestion API](https://blogs.sap.com/2022/07/20/integrating-sap-signavio-process-intelligence-and-sap-data-intelligence-cloud-a-concrete-example-with-the-new-ingestion-api).

## Requirements
- Access to a Qualtrics Survey
- SAP Signavio Process Intelligence license
- SAP Data Intelligence tenant

## Download and Installation
In this GitHub repository you can find 3 folders, "qualtrics_pi_di-1.0.0", "connect_to_qualtrics_survey-1.0.0" and "push_data_to_pi-1.0.0", containing respectively the SAP Data Intelligence graph, the SAP Data Intelligence connector to Qualtrics and the SAP Data Intelligence connector to SAP Signavio Process Intelligence. 

Here are the steps how to use them in your own environment:

0. In SAP Signavio Process Intelligence, create a new Ingestion API data source
1. Download and archive the content of the 3 folders (note: do not archive the folders, but for each folder select the content and add to archive) in 3 zip files, so that they can be imported as solutions into your SAP Data Intelligence tenant. In order to import solutions in SAP Data Intelligence, you can go to System Management, go to Files, click on the '+' symbol, select "Import Solution" and choose your zip file.
2. In SAP Data Intelligence, create an OPENAPI connection to Qualtrics
	- Host: qualtrics.com
	- Authentication Type: Basic
	- Username: the Qualtrics data center ID (can be found under your Qualtrics User, Account Settings, Qualtrics IDs)
	- Password: the Qualtrics token (can be found under your Qualtrics User, Account Settings, Qualtrics IDs)
3. In SAP Data Intelligence, create an OPENAPI connection to SAP Signavio
	- Host: spi-etl-ingestion.eu-prod-cloud-os-eu.suite-saas-prod.signav.io (note: the API endpoint url of Ingestion API will change soon)
	- Authentication Type: Basic
	- Username: it's not relevant, you can type "signavio"
	- Password: the Ingestion API token (can be found in the Ingestion API data source created at step 0)
4. In SAP Data Intelligence, open the Modeler and add the imported graph ("Qualtrics to SAP Signavio")
5. Configure the graph, save and execute
	- In the Qualtrics operator, add (1) the connection, and (2) the Qualtrics Survey ID
	- In the SAP Signavio operator, add (1) the connection, and (2) the name of the target table to be pushed in SAP Signavio Process Intelligence
6. Test the result: access to Ingestion API Integration in SAP Signavio Process Intelligence and check in the logs if a new request to push data has been received.

## How to obtain support
This sample is not part of the product. It is an open source artifact with no maintenance nor official support.

For additional support, [ask a question in SAP Community](https://answers.sap.com/questions/ask.html).

## License
Copyright (c) 2022 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSE) file.