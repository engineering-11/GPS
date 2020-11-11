import time
import datetime
import board
import busio
import adafruit_gps
import serial
import sys
import csv
import os


logging = False

def usage_error():
    print("Usage error!")
    print("Correct format: python3 [this filename] [frequency in seconds (min of 1)] [optional csv filename]")
    print("If a csv filename is provided, sensor data will be logged")

if len(sys.argv) != 2 and len(sys.argv) != 3:
    usage_error()
    exit()

try:
    freq = float(sys.argv[1])
except ValueError:
    print("Frequency must be a number")
    exit()

if len(sys.argv) == 3:
    filename = sys.argv[2]
    if len(filename) < 4:
        print("filename must end in .csv")
        exit()
    logging = True
    if not os.path.isfile(filename): # if file doesn't exist, add fields as first row
    	fields = ["Date", "latitude", "longitude"]
    	with open(filename, 'w+') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(fields)

def log_data(dt, lat, lon, filename):
    with open(filename, 'a') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow([dt, lat, lon])


# setup uart, initiate GPS sensor with typical settings
uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")

last_print = time.monotonic()
while True:
    gps.update()
    if (not gps.has_fix) or not (gps.timestamp_utc and gps.latitude and gps.longitude) :
        print("Searching for fix")
    else:
        lat = gps.latitude
        lon = gps.longitude

        try: # ensure datetime object not corrupted
            dt = datetime.datetime(*gps.timestamp_utc[:6]) # convert from time.time_struct to datetime object
        except ValueError:
            print("Searching for fix")
            continue

        print("==========")
        print("UTC time: " + str(dt))
        print("Lat, Lon: {0:.6f}, {0:.6f}".format(lat, lon))

        if logging:
            log_data(dt, lat, lon, filename)
            print("Data logged!")
        print("==========")

    time.sleep(0.5*freq)
    gps.update() # call multiple times per second so don't overflow buffer
    time.sleep(0.5*freq)

# Other gps.x fields: satellites, altitude_m, speed_knots, track_angle_deg, horizontal_dilution, height_geoid

