<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Twenty Five Years of GPS</h3><p>On Friday, the Global Positioning System (GPS) celebrated its 25th birthday in space. Launched into service on February 14 1989, the first of the <a href="http://en.wikipedia.org/wiki/GPS_Block_II">Block II</a> satellites was launched and started one of the most important changes in navigation in human history.</p>
<p>Originally set up as a research project for providing navigation for American military requirements, the GPS satellite project began in 1972, although the first ten trial satellites in <a href="http://en.wikipedia.org/wiki/GPS_Block_I">Block I</a> were not launched until 1978 and through to 1985. Having declared the process a success, the commercially available Block II satellites were launched in 1989 and 1990, with additional <a href="http://en.wikipedia.org/wiki/GPS_Block_IIA">IIA</a> and <a href="http://en.wikipedia.org/wiki/GPS_Block_IIR">IIR</a> satellites being launched during 1990–1997 and 1997–2004 respectively.</p>
<p>By December 1993, the GPS satellites had reached 24 in orbit, providing a standard positioning service (non-military uses) with a precise positioning service (military use) two years later. Originally the civilian use location services were close to within a few hundred metres, though additional frequencies providing greater civilian accuracy were launched in early 2000s, providing for more accurate vehicle navigation units.</p>
<p>GPS navigation works by having a set of synchronised atomic clocks and using the differences between the received signals to calculate an area. Three signals are required for location a point on the earth's surface, though four or more signals are required to pinpoint a location above the surface. Since each satellite does not stay in exactly the same orbit, a set of delta locations are calculated and published as corrections to the orbital almanac which is transmitted electronically to receivers to improve the accuracy of the location as well as improved acquisition time. And perhaps most interestingly is that GPS clocks provide a real-time test for general relativity; if it wasn't for the corrections built-in to take into account relativistic effects the GPS locations would <a href="http://www.astronomy.ohio-state.edu/~pogge/Ast162/Unit5/gps.html">diverge over 10km per day</a>.</p>
<p>Initially vehicle navigation units were bulky, and fitted to larger assets like aeroplanes and container ships, but as the ariel technology improved it became possible to mount them on smaller vehicles such as cars, and then ultimately smaller hand-held devices. These days flight paths are routinely plotted and navigated with the assistance of GPS, and together with assisted GPS at airports have even aided aeroplanes to land autonomously.</p>
<p>Geolocation has become increasingly important in on-line services, with various <a href="http://www.geoiptool.com">geo-ip</a> tools available on-line and even used to perform crude filtering (such as determining whether or not to stream <a href="http://bbc.co.uk/iplayer/">BBC content</a> outside the UK). There are even <a href="http://diveintohtml5.info/geolocation.html">APIs in HTML5</a> to access the location of the user's browser, assuming that they are on a locatable device; but with the widely available set of WiFi access points broadcasting locations, even without a GPS unit it is often possible to pinpoint someone to a few hundred meters. Passing a callback function to <code> navigator.geolocation.getCurrentPosition()</code> will return a position with co-ordinates including the latitude and longitude of the browser, along with an accuracy estimate.</p>
<p>Today, most mobile smartphones carry a GPS receiver and allow a user's location to be accurately pinpointed to within a few tens of meters, with only a few seconds of pinpointing. Together with on-board electronic compasses, this allows a user to determine not only how far they are away from a particular location but also which direction they must face in order to walk there. As long as there is a view of the horizon your location on this planet can be identified quickly and easily.</p><br><br><br><br><br><br></body></html>