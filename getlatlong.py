from geopy import geocoders
g = geocoders.GoogleV3()
x = ['939 North Spring Garden DeLand, FL 32720']
for address in x:
	place, (lat, lng) = g.geocode(x)
	print "%s: %.5f, %.5f" % (place, lat, lng)