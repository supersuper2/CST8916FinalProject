# Final Project Assignment: Real-time Monitoring System for Rideau Canal Skateway

## Scenario Description
The Rideau Canal Skateway in Ottawa that allows the public to skate on its surface throughout the winter season, making it one of Ottawa's largest skating attractions. The issue is that given global warming and the skateway being a canal, the National Capital Commission (NCC) must determine whether the canal is safe enough for the public to skate on or to close the canal for the rest of the winter.

### Problem Solved
This issue can be solved by placing IoT sensors within the canal to measure the following:

* Ice Thickness (in cm) - Ensures the public does not fall into the canal.
* Surface Temperature (in Celsius) - Ice melting risks.
* Snow Accumulation (in cm) - Determines ice structure, meaning if theres too much the public cant skate.
* External Temperature (in Celsius) - Whether it is safe to skate in the canal outside.

The analysis and processing of theses measurements, while visualizing them, will allow NCC to determine the appropriate measures to be taken, the goal being to open the canal without risking public safety. With IoT sensors, information about the canal's condition can be determined in real-time, allowing the NCC to determine specific conditions on when to open the canal. For example, the NCC may open the canal on a day they deem safe and close the canal the next day due to poor conditions.

## System Architecture
![cst8916finaldiagram1 drawio](https://github.com/user-attachments/assets/c7f9669f-b71e-41f2-95a0-ed20184b2598)

The architecture above shows the relationship of the IoT devices along with Azure Cloud services. The IoT devices send their data via a connection string to IoT hub which is then sent to Azure Stream Analytics for processing. When the data is finished processing, it is then sent to Azure Blob storage where it is stored in containers.

