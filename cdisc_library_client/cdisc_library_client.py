import requests
import json
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from cdisc_library_client.custom_exceptions import ResourceNotFoundException

class CDISCLibraryClient:

    def __init__(self, api_key, **params):
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 502, 503, 504, 408],
            allowed_methods=["GET", "POST"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.http = requests.Session()
        self.http.mount("https://", adapter)
        self.http.mount("http://", adapter)
        self.base_api_url = params.get("base_api_url", "https://library.cdisc.org/api")
        self.user_agent = params.get("user_agent", "library_client")
        self.api_key = api_key

    def get_api_json(self, href):
        headers = {
            'Accept': 'application/json',
            'api-key': self.api_key,
            "User-Agent": self.user_agent
        }
        raw_data = self.http.get(self.base_api_url+href, headers=headers)
        if raw_data.status_code == 200:
            return json.loads(raw_data.text)
        elif raw_data.status_code == 404:
            raise ResourceNotFoundException(f"Resource {self.base_api_url+href} is not found.")
        else:
            raise Exception(f"Request to {self.base_api_url+href} returned unsuccessful {raw_data.status_code} response")
    
    def get_raw_response(self, href):
        headers = {
            'Accept': 'application/json',
            'api-key': self.api_key,
            "User-Agent": "pipeline"
        }
        return self.http.get(self.base_api_url+href, headers=headers)
    
    def get_products(self):
        href = "/mdr/products"
        return self.get_api_json(href)
    
    def get_sdtm(self, version):
        href = f"/mdr/sdtm/{version}"
        return self.get_api_json(href)

    def get_sdtmig(self, version):
        href = f"/mdr/sdtmig/{version}"
        return self.get_api_json(href)

    def get_sendig(self, version):
        href = f"/mdr/sendig/{version}"
        return self.get_api_json(href)

    def get_adam(self, version):
        href = f"/mdr/adam/{version}"
        return self.get_api_json(href)
    
    def get_cdash(self, version):
        href = f"/mdr/cdash/{version}"
        return self.get_api_json(href)
        
    def get_cdashig(self, version):
        href = f"/mdr/cdashig/{version}"
        return self.get_api_json(href)

    def get_terminology_package(self, version):
        href = f"/mdr/ct/packages/{version}"
        return self.get_api_json(href)
    
    def get_codelist_terms(self, version, codelist):
        terms = []
        try:
            href = f"/mdr/ct/packages/{version}/codelists/{codelist}"
            data = self.get_api_json(href)
            terms = data.get("terms", [])
        except ResourceNotFoundException:
            pass
        return terms

    def get_codelist_term(self, version, codelist, term):
        term_data = None
        try:
            href = f"/mdr/ct/packages/{version}/codelists/{codelist}/terms/{term}"
            term_data = self.get_api_json(href)
        except ResourceNotFoundException:
            return None
        return term_data

    def get_qrs_instrument(self, instrument, version):
        href = f"/mdr/qrs/instruments/{instrument}/versions/{version}"
        return self.get_api_json(href)