from suds.client import Client
from suds.transport.http import HttpAuthenticated
import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)
logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)


def main():
    url = 'https://blah.com/soap/sp/Services?wsdl'
    credentials = dict(username='xxxx', password='xxxx')
    t = HttpAuthenticated(**credentials)
    client = Client(url, location='https://blah.com/soap/sp/Services', transport=t)
    print(client.last_sent())


if __name__ == "__main__":
    main()
