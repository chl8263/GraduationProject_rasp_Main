import gps

import paho.mqtt.client as mqtt

broker = "192.168.0.7"

port = 1883


def on_message(client, userdata, msg):
    print("message -> " + str(msg.payload))


session = gps.gps("localhost", "2947")

session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

client1 = mqtt.Client()

client1.on_message = on_message

client1.connect(broker, port, 60)

client1.subscribe("aa", 0)

client1.loop_start()

while True:

    try:

        # client1.publish(client1.getId)

        client1.publish("aa", "aaaaaaa")

        report = session.next()

        a = ""

        #                print report

        if report['class'] == 'TPV':

            # f hasattr(report, 'time'):

            print report.time

            if hasattr(report, 'lat'):
                print ("!!!!!!!!!!!")

                print ('%6.3f' % (report.lat))

                a += str(report.lat)

                print ("!!!!!!!!!!!")

            if hasattr(report, 'lon'):
                print ("!!!!!!!!!!!")

                print report.lon

                a += ","

                a += str(report.lon)

                print ("!!!!!!!!!!!")



        else:

            print 'GPS Signal\nnot found'



    except KeyError:

        pass

    except KeyboardInterrupt:

        quit()

    except StopIteration:

        session = None

        print "GPSD has terminated"

    client1.publish("aa", a)

