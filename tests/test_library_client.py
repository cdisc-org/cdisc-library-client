import imp
from cdisc_library_client import CDISCLibraryClient
from unittest import mock

@mock.patch('cdisc_library_client.library_client.CDISCLibraryClient.get_api_json')
def test_get_rule_catalogs(mock_get_api_json):
    client = CDISCLibraryClient(api_key="test")
    mock_response = {
        "_links": {
            "catalogs": {
                "sdtmig-3-4-cr": {
                    "href": "/mdr/rules/sdtmig/3-4",
                    "title": "sdtmig Conformance Rules v3-4",
                    "type": "Conformance Rules Package"
                }
            },
            "self": {
                "href": "/mdr/rules",
                "title": "CDISC Library Rules Catalog List",
                "type": "CDISC Library Product List"
            }
        }
    }
    mock_get_api_json.return_value = mock_response
    rule_catalogs = client.get_rule_catalogs()
    assert rule_catalogs == mock_response["_links"]["catalogs"]

@mock.patch('cdisc_library_client.library_client.CDISCLibraryClient.get_api_json')
def test_get_rules_catalog(mock_get_api_json):
    client = CDISCLibraryClient(api_key="test")
    mock_response = {
        "_links": {
            "self": {
                "href": "/mdr/rules/sdtmig/3-4",
                "title": "sdtmig Conformance Rules v3-4",
                "type": "Conformance Rules Package"
            }
        },
        "rules": {
            "rule1": 10,
            "rule2": 20
        }
    }
    mock_get_api_json.return_value = mock_response
    rules_catalog = client.get_rules_catalog("sdtmig", "3-4")
    assert rules_catalog == mock_response["rules"]
    