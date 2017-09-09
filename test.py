import urllib.request
import base64
import suds
import suds.transport
from suds.client import Client
import array

class HTTPSudsPreprocessor(urllib.request.BaseHandler):

    def http_request(self, req):
        message = \
        """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:air="http://www.travelport.com/schema/air_v16_0" xmlns:com="http://www.travelport.com/schema/common_v13_0" -->
            <soapenv:header>
            <soapenv:body>
            <air:availabilitysearchreq xmlns:air="http://www.travelport.com/schema/air_v16_0" xmlns:com="http://www.travelport.com/schema/common_v13_0" authorizedby="Test" targetbranch="P2916782 using 1G PCC 664M">
            <air:searchairleg>
            <air:searchorigin>
            <com:airport code="LHR">
            </com:airport></air:searchorigin>
            <air:searchdestination>
            <com:airport code="JFK">
            </com:airport></air:searchdestination>
            <air:searchdeptime preferredtime="2011-11-08">
            </air:searchdeptime></air:searchairleg>
            </air:availabilitysearchreq>
            </soapenv:body>
        """
        user = 'Universal API/uAPI5632685783-282e0d4d'
        password = 'xS!7K6d%3?'
        # auth = base64.b64encode('Universal API/uAPI2514620686-0edbb8e4:D54HWfck9nRZNPbXmpzCGwc95')
        auth = base64.b64encode(b'Universal API/uAPI5632685783-282e0d4d:xS!7K6d%3?')
        req.add_header('Content-Type', 'text/xml; charset=utf-8')
        req.add_header('Accept', 'gzip,deflate')
        req.add_header('Cache-Control', 'no-cache')
        req.add_header('Pragma', 'no-cache')
        req.add_header('SOAPAction', 'LowFareSearchReq')
        req.add_header('Authorization', 'Basic %s' % (auth))
        return req

    https_request = http_request


URL = "https://americas.universal-api.travelport.com/B2BGateway/connect/uAPI/AirService"
https = suds.transport.https.HttpTransport()
opener = urllib.request.build_opener(HTTPSudsPreprocessor)
https.urlopener = opener
suds.client.Client(URL, transport=https)
# Client(URL, headers={'user': 'Universal API/uAPI5632685783-282e0d4d', 'password': 'xS!7K6d%3?', 'branch': 'P2916782 using 1G PCC 664M'})
