from azure.iot.device.aio import IoTHubDeviceClient
from dotenv import load_dotenv

import time
import os
import json
import asyncio
import datetime
import random

load_dotenv()
connectionStrings = [os.getenv('IOTHUB_STR1'), os.getenv('IOTHUB_STR2'), os.getenv('IOTHUB_STR3')]
print("Connection Strings:\n" + connectionStrings[0] + ", \n" + connectionStrings[1] + ", \n" + connectionStrings[2])

async def sendToIotHub(data, conn):
    try:
        # Create an instance of the IoT Hub Client class
        deviceId = IoTHubDeviceClient.create_from_connection_string(connectionStrings[conn])

        # Connect to client
        await deviceId.connect()

        #Send message
        await deviceId.send_message(data)
        print("Message sent to IoT Hub:", data)

        # Shutdown client
        await deviceId.shutdown()
        
    
    except Exception as e:
        print("Error:", str(e))

def main():
    # Run an infinite while loop to send data
    while True:
        # Generate random value
        locations = ["Dow's Lake", "Fifth Avenue", "NAC"]

        # Generate data for each location
        for x in enumerate(locations):
            iceThickness = random.randrange(0, 10) # generates a random num between 0 and 10
            surfaceTemp = random.randrange(-30, 10) # generates a random num between -30 and 10 for temp
            snowAccumulation = random.randrange(0, 10) # generates a random num between 0 and 10
            externalTemp = random.randrange(-30, 10) # generates a random number between -30 and 10
            
            msgData={ # pass the generated variables to an object
                "location": locations[x[0]],
                "iceThickness": iceThickness,
                "surfaceTemperature": surfaceTemp,
                "snowAccumulation": snowAccumulation,
                "externalTemperature": externalTemp,
                "timestamp":str(datetime.datetime.now())
            }
            # the following runs an asynchronous task and passing the payload
            asyncio.run(sendToIotHub(data=json.dumps(msgData), conn=x[0]))
            time.sleep(10)

if __name__ == '__main__':
    main()
    