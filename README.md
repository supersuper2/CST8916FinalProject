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

## Implementation Details
### IoT Sensor Simulation

This connection part where is uses the .env file for the environment variables. We define our environment variables (connection strings), and how we use the passed data and index (conn) to send the message.

![code](./screenshots/part1code.png)

This main method, is a while loop set to true, in the loop is an array of locations and each location in one iteration of the while loop, numbers are generated for our json variables. The json and an index number is sent to the sendToIotHub() function, which handles sending of the data to the endpoints. Each iteration of the inner loop pauses for 10 seconds after sending a message to IoT Hub.

For the sensors, the JSON payload is separated into ice thickness, surface temperature, snow accumulation, and external temperature. We use data=json.dumps(msgData) which returns our object full of generated variables into a json string, while passing it to the sendToIotHub() method. This data is sent with new generated data to alternating locations for as long as the program is running.

![code](./screenshots/part2code.png)

### Azure IoT Hub Configuration

