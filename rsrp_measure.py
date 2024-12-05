#!/usr/bin/env python3


from serial import Serial

qcm = Serial('/dev/ttyUSB2', baudrate=115200, timeout=3)

on_cmd = "at+qrsrp\r\n".encode()

print('# Showing RSRP on the Quectel module ...')

qcm.write(on_cmd)

filename = "measurements.txt" 


while True:
    # read_until() reads until LF
    rdata = qcm.read_until().decode()
    if not rdata:
        # Timeout occured -> no more data to read
        break
    print(rdata)

    filename = "measurements_rsrp.txt"

    with open(filename,"a") as file:
        for line in str(rdata).splitlines():
            if line.startswith("+"):
                file.write(line + " \n") 

print()
print('# Done!')
