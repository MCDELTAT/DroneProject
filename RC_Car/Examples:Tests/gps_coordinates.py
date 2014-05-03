//GPS_Coordinates_Test
//Written by Aaron Chamberlain February 2014
//Just a simple test to print out the lat and long of the Raspberry pi
//this was used to debug and test accuracy of the system. 

import gps

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
	try:
		
		report = session.next()
		# print report
		if report['class'] == 'TPV':
			if hasattr(report, 'lat'):
				print ("Latitude= ", str(report.lat))
				print ("Longtitude= ", str(report.lon))

	except KeyError:
		pass
	except KeyboardInterrupt:
		quit()
	except StopIteration:
		session = None
		print "GPSD has terminated"