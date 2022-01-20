import os
from cdisc_library_client.cdisc_library_client import CDISCLibraryClient

if __name__ == "__main__":
    api_key = os.environ.get("CDISC_LIBRARY_API_KEY")
    client = CDISCLibraryClient(api_key=api_key)

    # Get all products
    products = client.get_products()

    # Get sdtm
    sdtm = client.get_sdtm(version="2-0")
    # Get sdtmig
    sdtmig = client.get_sdtmig(version="3-4")
    # Get sendig
    sendig = client.get_sendig(version="3-1-1")
    # Get adam
    adam = client.get_adam(version="adam-2-1")
    # Get adamig
    adamig = client.get_adam(version="adamig-1-3")
    # Get CDASH
    cdash = client.get_cdash(version="1-0")
    #Get CDASHIG
    cdashig = client.get_cdashig(version="2-0")
    # Get CT package
    ct = client.get_terminology_package(version="sdtmct-2018-12-21")
    # Get QRS supplement
    instrument = client.get_qrs_instrument(instrument="SIXMW1", version="1-0")