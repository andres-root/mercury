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
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:air="http://www.travelport.com/schema/air_v42_0" xmlns:com="http://www.travelport.com/schema/common_v38_0">
               <soapenv:Header/>
               <soapenv:Body>
                  <LowFareSearchReq xmlns="http://www.travelport.com/schema/air_v42_0" TraceId="947a5a58-ad2a-4db4-88e5-ad5583ae4fce" TargetBranch="P2916782" ReturnUpsellFare="true">
              <BillingPointOfSaleInfo xmlns="http://www.travelport.com/schema/common_v42_0" OriginApplication="uAPI" />
              <SearchAirLeg>
                <SearchOrigin>
                  <CityOrAirport xmlns="http://www.travelport.com/schema/common_v42_0" Code="BOG" PreferCity="true" />
                </SearchOrigin>
                <SearchDestination>
                  <CityOrAirport xmlns="http://www.travelport.com/schema/common_v42_0" Code="SFO" PreferCity="true" />
                </SearchDestination>
                <SearchDepTime PreferredTime="2017-09-13" />
              </SearchAirLeg>
              <SearchAirLeg>
                <SearchOrigin>
                  <CityOrAirport xmlns="http://www.travelport.com/schema/common_v42_0" Code="SFO" PreferCity="true" />
                </SearchOrigin>
                <SearchDestination>
                  <CityOrAirport xmlns="http://www.travelport.com/schema/common_v42_0" Code="BOG" PreferCity="true" />
                </SearchDestination>
                <SearchDepTime PreferredTime="2017-09-30" />
              </SearchAirLeg>
              <AirSearchModifiers>
                <PreferredProviders>
                  <Provider xmlns="http://www.travelport.com/schema/common_v42_0" Code="1G" />
                </PreferredProviders>
              </AirSearchModifiers>
              <SearchPassenger xmlns="http://www.travelport.com/schema/common_v42_0" Code="ADT" />
              <AirPricingModifiers>
                <AccountCodes>
                  <AccountCode xmlns="http://www.travelport.com/schema/common_v42_0" Code="-" />
                </AccountCodes>
              </AirPricingModifiers>
            </LowFareSearchReq>
               </soapenv:Body>
            </soapenv:Envelope>
        """
        # user = 'Universal API/uAPI5632685783-282e0d4d'
        # password = 'xS!7K6d%3?'
        # auth = base64.b64encode('Universal API/uAPI2514620686-0edbb8e4:D54HWfck9nRZNPbXmpzCGwc95')
        auth = base64.b64encode(b'Universal API/uAPI5632685783-282e0d4d:xS!7K6d%3?')
        print(auth.decode('utf-8'))
        req.add_header('Accept-Encoding', 'gzip,deflate')
        req.add_header('Content-Type', 'text/xml;charset=UTF-8')
        req.add_header('Cache-Control', 'no-cache')
        req.add_header('Pragma', 'no-cache')
        req.add_header('SOAPAction', "http://localhost:8080/kestrel/AirService")
        req.add_header('action', "http://localhost:8080/kestrel/AirService")
        # req.add_header('Authorization', 'Basic %s' % (auth.decode('utf-8')))
        req.add_header('Authorization', 'Basic VW5pdmVyc2FsIEFQSS91QVBJNTYzMjY4NTc4My0yODJlMGQ0ZDp4UyE3SzZkJTM/')
        return req

    https_request = http_request


URL = "https://americas.universal-api.travelport.com/B2BGateway/connect/uAPI/AirService"
https = suds.transport.https.HttpTransport()
import ipdb; ipdb.set_trace()
opener = urllib.request.build_opener(HTTPSudsPreprocessor)
https.urlopener = opener
try:
    suds.client.Client(URL, transport=https)
except Exception as e:
    print(e)

# client = suds.client.Client(URL, headers={'Content-Type': 'text/xml;charset=UTF-8', 'Authorization': 'Basic VW5pdmVyc2FsIEFQSS91QVBJNTYzMjY4NTc4My0yODJlMGQ0ZDp4UyE3SzZkJTM/'})
# client.set_options(headers={'Content-Type': 'text/xml;charset=UTF-8', 'Authorization': 'Basic VW5pdmVyc2FsIEFQSS91QVBJNTYzMjY4NTc4My0yODJlMGQ0ZDp4UyE3SzZkJTM/'})
