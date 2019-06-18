import serial


class PiSerial:

    def start(self):
        port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)
        print('start')
        mes = bytes('#BPM_PRES\n', 'utf-8')
        port.write(mes)
        return 'STARTED'

    def stop(self):
        port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)
        print('stop')
        mes = bytes('#BPM_PRES\n', 'utf-8')
        port.write(mes)

    def listen(self):
        while True:
            port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)
            resp = port.readline()
            decresp = resp.decode('utf-8')

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
        return data
