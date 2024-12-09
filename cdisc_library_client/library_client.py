import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from .custom_exceptions import ResourceNotFoundException

class CDISCLibraryClient:

    def __init__(self, api_key, **params):
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 502, 503, 504, 408]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self._session = requests.Session()
        self._session.mount("https://", adapter)
        self._session.mount("http://", adapter)
        self.base_api_url = params.get("base_api_url", "https://library.cdisc.org/api")
        self._user_agent = params.get("user_agent", "library_client")
        self._api_key = api_key

    def get_api_json(self, uri):
        headers = {
            'Accept': 'application/json',
            'api-key': self._api_key,
            "User-Agent": self._user_agent
        }
        raw_data = self._session.get(self.base_api_url+uri, headers=headers)
        if raw_data.status_code >=  200 and raw_data.status_code <= 299:
            return raw_data.json()
        elif raw_data.status_code == 404:
            raise ResourceNotFoundException(f"Resource {self.base_api_url+uri} is not found.")
        else:
            raise Exception(f"Request to {self.base_api_url+uri} returned unsuccessful {raw_data.status_code} response")

    def get_raw_response(self, uri):
        headers = {
            'Accept': 'application/json',
            'api-key': self.api_key,
            "User-Agent": "pipeline"
        }
        return self._session.get(self.base_api_url+uri, headers=headers)

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

    def get_tig(self, version, substandard):
        href = f"/mdr/integrated/tig/{version}/{substandard}"
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

    def get_rule_catalogs(self):
        """
        Returns an object containing a mapping of catalog titles to links to the catalogs of the form:
        {
            "sdtmig-3-4-cr": {
                "href": "/mdr/rules/sdtmig/3-4",
                "title": "sdtmig Conformance Rules v3-4",
                "type": "Conformance Rules Package"
            }...
        }
        """
        href = f"/mdr/rules"
        response = self.get_api_json(href)
        return response.get("_links", {}).get("catalogs", {})

    def get_rules_catalog(self, standard: str, version: str):
        """
        Returns an object containing a mapping of rule id to rule definitions
        """
        href = f"/mdr/rules/{standard}/{version}"
        response = self.get_api_json(href)
        return response.get("rules", {})

    def get_rule(self, standard: str, version: str, rule_id: str):
        """
        Returns a rule definition given a standard, version and rule id.
        """
        href = f"/mdr/rules/{standard}/{version}/rule/{rule_id}"
        return self.get_api_json(href)

    def get_bc_packages(self, version: str):
        href = f"/cosmos/{version}/mdr/bc/packages"
        response = self.get_api_json(href)
        return response.get("_links", {}).get("packages", [])

    def get_bc_package_biomedicalconcepts(self, version: str, package: str):
        href = f"/cosmos/{version}/mdr/bc/packages/{package}/biomedicalconcepts"
        response = self.get_api_json(href)
        return response.get("_links", {}).get("biomedicalConcepts", [])

    def get_bc_package_biomedicalconcept(self, version: str, package: str, biomedicalconcept: str):
        href = f"/cosmos/{version}/mdr/bc/packages/{package}/biomedicalconcepts/{biomedicalconcept}"
        return self.get_api_json(href)

    def get_bc_latest_biomedicalconcepts(self, version: str):
        href = f"/cosmos/{version}/mdr/bc/biomedicalconcepts"
        response = self.get_api_json(href)
        return response.get("_links", {}).get("biomedicalConcepts", [])

    def get_bc_latest_biomedicalconcept(self, version: str, biomedicalconcept: str):
        href = f"/cosmos/{version}/mdr/bc/biomedicalconcepts/{biomedicalconcept}"
        return self.get_api_json(href)

    def get_bc_categories(self, version: str):
        href = f"/cosmos/{version}/mdr/bc/categories"
        response = self.get_api_json(href)
        return response.get("_links", {}).get("categories", [])

    def get_bc_latest_biomedicalconcepts_category(self, version: str, category: str):
        href = f"/cosmos/{version}/mdr/bc/biomedicalconcepts?category={category}"
        response = self.get_api_json(href)
        return response.get("_links", {}).get("biomedicalConcepts", [])

    def get_sdtm_packages(self, version: str):
        href = f"/cosmos/{version}/mdr/specializations/sdtm/packages"
        response = self.get_api_json(href)
        return response.get("_links", {}).get("packages", [])

    def get_sdtm_package_datasetspecializations(self, version: str, package: str):
        href = f"/cosmos/{version}/mdr/specializations/sdtm/packages/{package}/datasetspecializations"
        response = self.get_api_json(href)
        return response.get("_links", {}).get("datasetSpecializations", [])

    def get_sdtm_package_datasetspecialization(self, version: str, package: str, datasetspecialization: str):
        href = f"/cosmos/{version}/mdr/specializations/sdtm/packages/{package}/datasetspecializations/{datasetspecialization}"
        return self.get_api_json(href)

    def get_sdtm_latest_sdtm_datasetspecializations(self, version: str):
        href = f"/cosmos/{version}/mdr/specializations/sdtm/datasetspecializations"
        response = self.get_api_json(href)
        return response.get("_links", {}).get("datasetSpecializations", [])

    def get_sdtm_latest_sdtm_datasetspecialization(self, version: str, datasetspecialization: str):
        href = f"/cosmos/{version}/mdr/specializations/sdtm/datasetspecializations/{datasetspecialization}"
        return self.get_api_json(href)

    def get_sdtm_domains(self, version: str):
        href = f"/cosmos/{version}/mdr/specializations/sdtm/domains"
        response = self.get_api_json(href)
        return response.get("domains", [])

    def get_sdtm_latest_sdtm_datasetspecializations_domain(self, version: str, domain: str):
        href = f"/cosmos/{version}/mdr/specializations/sdtm/datasetspecializations?domain={domain}"
        response = self.get_api_json(href)
        return response.get("_links", {}).get("datasetSpecializations", [])

    def get_biomedicalconcept_latest_datasetspecializations(self, version: str, biomedicalconcept: str):
        href = f"/cosmos/{version}/mdr/specializations/datasetspecializations?biomedicalconcept={biomedicalconcept}"
        response = self.get_api_json(href)
        return response.get("_links", {}).get("datasetSpecializations", [])
