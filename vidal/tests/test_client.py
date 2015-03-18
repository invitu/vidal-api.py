import unittest
import responses

from vidal import client

class AuthentificationTest(unittest.TestCase):

    def setUp(self):
        self.client = client.VidalClient(api_key = "")

    @responses.activate
    def test_auth_forbidden(self):
        responses.add(responses.GET, 'http://api.vidal.fr', status=403)

        self.assertFalse(self.client.is_authenticated())

    @responses.activate
    def test_auth_all_good(self):
        responses.add(responses.GET, 'http://api.vidal.fr', status=200)

        self.assertTrue(self.client.is_authenticated())

    @responses.activate
    def test_auth_when_internal_server_error(self):
        responses.add(responses.GET, 'http://api.vidal.fr', status=500)

        self.assertFalse(self.client.is_authenticated())


class ChainedCommandTest(unittest.TestCase):

    def setUp(self):
        self.client = client.VidalClient(api_key = "")

    @responses.activate
    def test_chained_command_get(self):
        responses.add(responses.GET, 'http://api.vidal.fr/rest/api/product/94930/packages', status=200)

        result = self.client.product(94930).packages.get()
        self.assertTrue(result is not None)

    @responses.activate
    def test_chained_command_search(self):
        responses.add(responses.GET, 'http://api.vidal.fr/rest/api/products', status=200, body="""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:vidal="http://api.vidal.net/-/spec/vidal-api/1.0/">
  <title>Packages for Product 94930</title>
  <link rel="self" type="application/atom+xml" href="/rest/api/product/94930/packages" />
  <id>vidal://product/94930/packages</id>
  <updated>2015-02-16T23:00:00Z</updated>
  <dc:date>2015-02-16T23:00:00Z</dc:date>
  <entry>
    <title>COQUELUSEDAL PARACETAMOL 100 mg Suppos Plq/10</title>
    <link rel="alternate" type="application/atom+xml" href="/rest/api/package/218745" />
    <link rel="related" type="application/atom+xml" href="/rest/api/product/94930" title="PRODUCT" />
    <link rel="related" type="application/atom+xml" href="/rest/api/package/218745/documents/opt" title="OPT_DOCUMENT" />
    <link rel="related" type="application/atom+xml" href="/rest/api/package/218745/documents" title="DOCUMENT" />
    <category term="PACKAGE" />
    <author>
      <name>VIDAL</name>
    </author>
    <id>vidal://package/218745</id>
    <updated>2015-02-16T23:00:00Z</updated>
    <summary type="text">COQUELUSEDAL PARACETAMOL 100 mg Suppos Plq/10</summary>
    <vidal:id>218745</vidal:id>
    <vidal:name>COQUELUSEDAL PARACETAMOL 100 mg Suppos Plq/10</vidal:name>
    <vidal:dispensationPlace>PHARMACY</vidal:dispensationPlace>
    <vidal:exceptional>false</vidal:exceptional>
    <vidal:horsGHS>false</vidal:horsGHS>
    <vidal:itemType>VIDAL</vidal:itemType>
    <vidal:cip>3771034</vidal:cip>
    <vidal:vatRate name="NORMAL">10.0</vidal:vatRate>
    <vidal:pharmacistPrice>2.44</vidal:pharmacistPrice>
    <vidal:drugId>94930</vidal:drugId>
    <vidal:onMarketDate>2009-09-04</vidal:onMarketDate>
    <vidal:otc>true</vidal:otc>
    <vidal:cis>61293112</vidal:cis>
    <vidal:cip13>3400937710343</vidal:cip13>
    <vidal:marketStatus name="AVAILABLE">Commercialisé</vidal:marketStatus>
    <vidal:company vidalId="294" type="DISTRIBUTOR">Elerté</vidal:company>
    <vidal:company vidalId="294" type="HOLDER">Elerté</vidal:company>
    <vidal:refundRate name="NR">NR</vidal:refundRate>
    <vidal:communityAgreement>false</vidal:communityAgreement>
  </entry>
</feed>
""")

        result = self.client.products.get(q = "amoxyiciline")
        self.assertTrue(result is not None)
        self.assertTrue(len(result.entries) == 1)
        item = result.entries[0]

        self.assertEqual(item.vidal_id, str(218745))
        self.assertEqual(item.vidal_cip, "3771034")
        self.assertEqual(item.vidal_marketstatus["name"], "AVAILABLE")
        self.assertEqual(item.id, "vidal://package/218745")


if __name__ == '__main__':
    unittest.main()