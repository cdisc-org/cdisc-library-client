import os
from cdisc_library_client import CDISCLibraryClient

if __name__ == "__main__":
    api_key = os.environ.get("CDISC_LIBRARY_API_KEY")
    client = CDISCLibraryClient(api_key=api_key)

    # Get codelist terms
    terms = client.get_codelist_terms("adamct-2014-09-26", "C117745")
    print(len(terms))

    # Get codelist term
    term = client.get_codelist_term("adamct-2014-09-26", "C117745", "C98724")
    print(term)
