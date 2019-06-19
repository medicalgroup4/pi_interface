import serial


class PiSerial:

    def start(self):
        port = serial.Serial("/dev/ttyACM0", baudrate=9600, bytesize=serial.EIGHTBITS, timeout=0.1, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        print('start')
        mes = "BPM_PRES\n"
        encoded = mes.encode('ASCII')
        port.write(encoded)
        port.close()
        return 'STARTED'

    def stop(self):
        port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0.1)
        print('stop')
        mes = bytes('#BPM_STOP\n', 'ASCII')
        port.write(mes)
        port.close()

    def listen(self):
        port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0.1)

        while True:
            resp = port.readline()
            decresp = resp.decode('ASCII')

            print(decresp)

            systolic, diastolic, heartrate = '0', '0', '0'

            if decresp.startswith('#SYST'):
                systolic = int(decresp.replace('#SYST', ''))

            if decresp.startswith('#DIST'):
                diastolic = int(decresp.replace('#DIST', ''))

            if decresp.startswith('#HERA'):
                heartrate = int(decresp.replace('#HERA', ''))

            if systolic and diastolic and heartrate is not None:
                break

        data = [systolic, diastolic, heartrate]
        port.close()
        return data
