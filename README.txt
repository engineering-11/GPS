The script that acquires GPS data is named "GPS.py". Follow the steps below to run the script.

1. Locate your GPS sensor, and the blue cable that connects USB to four female connectors.
2. Optionally, locate the skinny pink cable and the long black cable with a chunky rectangular end.
3. Connect the blue USB cable to the GPS sensor: red->3.3V, white->TX, green->RX, black->GND.
4. Optionally, for better signal attach the skinny pink cable to the GPS sensor by snapping on the small end near where it says "breakout v3" on the sensor.
5. Optionally, for better signal attach the long black cable to the other end of the skinny pink cable.
6. Plug in the blue USB cable to the rasberry pi, and supply power to the raspberry pi.
7. Now that the hardware is setup, run "sudo pip3 install adafruit-circuitpython-gps". This installs certain necessary libraries. If prompted, type in the password to your pi and press enter.
8. Now run the script by typing [python3] [name_of_script] [datalog_frequency_in_seconds (minimum 1)] [optional_csv_filename]".
8a. An example could be "python3 GPS.py 1". This runs the script "GPS.py" and prints data every 1 second.
8b. Another example could be "python3 GPS.py 3 gps_data.csv". This runs the script "GPS.py", and every 3 seconds it both prints GPS data to the screen and logs an entry in "gps_data.csv". If "gps_data.csv" already exists, it appends to the file. Otherwise it creates a new file.
9. Note that valid GPS data will only be printed and logged if the GPS sensor has acquired a fix. It may take a few minutes to acquire a fix. For best results, do the optional step 2 and step 4. Also, it helps if your sensor has a direct line of sight to the sky.
