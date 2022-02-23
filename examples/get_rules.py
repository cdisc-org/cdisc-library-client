import os
from cdisc_library_client import CDISCLibraryClient

if __name__ == "__main__":
    api_key = os.environ.get("CDISC_LIBRARY_API_KEY")
    client = CDISCLibraryClient(api_key=api_key)

    catalogs = client.get_rule_catalogs()
    assert catalogs
    for catalog, link in catalogs.items():
        href = link["href"]
        standard = href.split("/")[-2]
        version = href.split("/")[-1]
        rules = client.get_rules_catalog(standard, version)
        print(f"{catalog} has {len(rules.values())} rules")
