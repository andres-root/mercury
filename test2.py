from suds.client import Client
import suds.transport
from suds.sax.element import Element
from suds.sax.attribute import Attribute
import base64

https = suds.transport.https.HttpTransport()
URL = "hcttps://americas.universal-api.travelport.com/B2BGateway/connect/uAPI/AirService"
auth = base64.b64encode(b'Universal API/uAPI5632685783-282e0d4d:xS!7K6d%3?')
auth = str(auth)
# # Headers
# code = Element('Authorization').setText(auth)

# reqsoapheader = Element('ReqSOAPHeader').insert(code)
# reqsoap_attribute = Attribute('xmlns', "http://schemas.acme.eu/")
# reqsoapheader.append(reqsoap_attribute)

message = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
       <soapenv:Header/>
       <soapenv:Body>
          <air:AvailabilitySearchReq TraceId="trace" AuthorizedBy="user" TargetBranch="P2916782 using 1G PCC 664M" xmlns:air="http://www.travelport.com/schema/air_v29_0" xmlns:com="http://www.travelport.com/schema/common_v29_0">
             <com:BillingPointOfSaleInfo OriginApplication="UAPI"/>
             <air:SearchAirLeg>
                <air:SearchOrigin>
                   <com:Airport Code="LGW"/>
                </air:SearchOrigin>
                <air:SearchDestination>
                   <com:Airport Code="EDI"/>
                </air:SearchDestination>
                <air:SearchDepTime PreferredTime="2014-12-31">
                </air:SearchDepTime>
             </air:SearchAirLeg>
             <air:AirSearchModifiers>
                <air:PreferredProviders>
                   <com:Provider Code="$Provider"/>
                </air:PreferredProviders>
             </air:AirSearchModifiers>
          </air:AvailabilitySearchReq>
       </soapenv:Body>
    </soapenv:Envelope>
"""

headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'Accept': 'gzip,deflate',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Authorization': 'Basic {0}'.format(str(auth))
}
try:
    client = Client(URL, headers=headers, transport=https)
except Exception as e:
    print(e)
