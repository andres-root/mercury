import urllib.request
import base64
import suds
import suds.transport
from suds.client import Client
import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)
logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)


class HTTPSudsPreprocessor(urllib.request.BaseHandler):

    def http_request(self, req):
        message = \
        """
            <soapenv:Envelope" -->
            <soapenv:header>
            <soapenv:body>
                <LowFareSearchReq xmlns="http://www.travelport.com/schema/air_v42_0" TraceId="b0eb94ba-3561-4af9-bdba-ea4272ac9825" TargetBranch="P2916782">
                  <BillingPointOfSaleInfo xmlns="http://www.travelport.com/schema/common_v42_0" OriginApplication="uAPI" />
                  <SearchAirLeg>
                    <SearchOrigin>
                      <CityOrAirport xmlns="http://www.travelport.com/schema/common_v42_0" Code="BOG" PreferCity="true" />
                    </SearchOrigin>
                    <SearchDestination>
                      <CityOrAirport xmlns="http://www.travelport.com/schema/common_v42_0" Code="SFO" PreferCity="true" />
                    </SearchDestination>
                  </SearchAirLeg>
                  <AirSearchModifiers>
                    <PreferredProviders>
                      <Provider xmlns="http://www.travelport.com/schema/common_v42_0" Code="1G" />
                    </PreferredProviders>
                  </AirSearchModifiers>
                  <SearchPassenger xmlns="http://www.travelport.com/schema/common_v42_0" Code="ADT" />
                  <AirPricingModifiers />
                </LowFareSearchReq>
            </soapenv:body>
        """
        # user = 'Universal API/uAPI5632685783-282e0d4d'
        # password = 'xS!7K6d%3?'
        # auth = base64.b64encode('Universal API/uAPI2514620686-0edbb8e4:D54HWfck9nRZNPbXmpzCGwc95')
        auth = base64.b64encode(b'Universal API/uAPI5632685783-282e0d4d:xS!7K6d%3?')
        req.add_header('Content-Type', 'text/xml; charset=utf-8')
        req.add_header('Accept', 'gzip,deflate')
        req.add_header('Cache-Control', 'no-cache')
        req.add_header('Pragma', 'no-cache')
        req.add_header('SOAPAction', '""    ')
        req.add_header('Authorization', 'Basic %s' % (auth.decode('utf-8')))
        return req

    https_request = http_request


URL = "https://americas.universal-api.travelport.com/B2BGateway/connect/uAPI/AirService"
https = suds.transport.https.HttpTransport()
opener = urllib.request.build_opener(HTTPSudsPreprocessor)
https.urlopener = opener
suds.client.Client(URL, transport=https)
