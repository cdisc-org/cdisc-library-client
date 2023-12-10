import os
from cdisc_library_client import CDISCLibraryClient

if __name__ == "__main__":
    api_key = os.environ.get("CDISC_LIBRARY_API_KEY")
    client = CDISCLibraryClient(api_key=api_key)

    # Get BC packages
    bc_packages = client.get_bc_packages("v2")
    print(f"There are {len(bc_packages)} Biomedical Concept packages")

    # Get BCs in package
    for package in bc_packages:
      title = package['title']
      href = package['href']
      package = href.split("/")[-2]
      biomedicalconcepts = client.get_bc_package_biomedicalconcepts("v2", package)
      print(f"{title} has {len(biomedicalconcepts)} Biomedical Concepts")

    # Get a specific BC in a package
    bc = client.get_bc_package_biomedicalconcept("v2", "2023-12-12", "C25298")
    package = bc['_links']['parentPackage']['title']
    title = bc['shortName']
    print(f"{title} in {package} has {len(bc['dataElementConcepts'])} Data Element Concepts")

    # Get BC categories
    categories = client.get_bc_categories("v2")
    print(f"There are {len(categories)} Biomedical Concept categories")

    # Get latest BCs
    biomedicalconcepts = client.get_bc_latest_biomedicalconcepts("v2")
    print(f"There are {len(biomedicalconcepts)} Biomedical Concepts in the CDISC Library")

    # Get the latest version of a specific BC
    bc = client.get_bc_latest_biomedicalconcept("v2", "C25298")
    package = bc['_links']['parentPackage']['title']
    title = bc['shortName']
    print(f"{title} in {package} has {len(bc['dataElementConcepts'])} Data Element Concepts")

    # Get latest BCs in a category
    biomedicalconcepts = client.get_bc_latest_biomedicalconcepts_category("v2", "RECIST 1.1")
    print(f"There are {len(biomedicalconcepts)} Biomedical Concepts in the RECIST 1.1 category in the CDISC Library")

    # Get latest BCs in a category
    biomedicalconcepts = client.get_bc_latest_biomedicalconcepts_category("v2", "")
    print(f"There are {len(biomedicalconcepts)} Biomedical Concepts in the CDISC Library")

    # Get SDTM Dataset Specialization Packages
    sdtm_packages = client.get_sdtm_packages("v2")
    print(f"There are {len(sdtm_packages)} SDTM Dataset Specialization packages")

    # Get Specializations in package
    for package in sdtm_packages:
      title = package['title']
      href = package['href']
      package = href.split("/")[-2]
      datasetspecializations = client.get_sdtm_package_datasetspecializations("v2", package)
      print(f"{title} has {len(datasetspecializations)} SDTM Dataset Specializations")

    # Get a specific SDTM Dataset Specializatio in a package
    sdtm = client.get_sdtm_package_datasetspecialization("v2", "2023-12-12", "SYSBP")
    package = sdtm['_links']['parentPackage']['title']
    title = sdtm['shortName']
    print(f"{title} in {package} has {len(sdtm['variables'])} Variables")

    # Get SDTM domains
    domains = client.get_sdtm_domains("v2")
    print(f"There are {len(domains)} SDTM domains")

    # Get latest SDTM Dataset Specializations
    specializations = client.get_sdtm_latest_sdtm_datasetspecializations("v2")
    print(f"There are {len(specializations)} SDTM Dataset Specializations in the CDISC Library")

    # Get the latest version of a specific SDTM Dataset Specialization
    sdtm = client.get_sdtm_latest_sdtm_datasetspecialization("v2", "SYSBP")
    package = sdtm['_links']['parentPackage']['title']
    title = sdtm['shortName']
    print(f"{title} in {package} has {len(sdtm['variables'])} Variables")

    # Get latest SDTM Dataset Specializations in a domain
    specializations = client.get_sdtm_latest_sdtm_datasetspecializations_domain("v2", "VS")
    print(f"There are {len(specializations)} SDTM Dataset Specializations in the VS domain in the CDISC Library")

   # Get latest SDTM Dataset Specializations in a domain
    specializations = client.get_sdtm_latest_sdtm_datasetspecializations_domain("v2", "")
    print(f"There are {len(specializations)} SDTM Dataset Specializations in the CDISC Library")

    # Get latest SDTM Dataset Specializations that specialize a Biomedical Concept
    specializations = client.get_sdtm_biomedicalconcept_latest_datasetspecializations("v2", "")
    sdtm_specializations = specializations['sdtm']
    print(f"There are {len(sdtm_specializations)} SDTM Dataset Specializations in the CDISC Library")

    # Get latest SDTM Dataset Specializations that specialize a Biomedical Concept
    biomedicalConcept = "C25298"
    specializations = client.get_sdtm_biomedicalconcept_latest_datasetspecializations("v2", biomedicalConcept)
    sdtm_specializations = specializations['sdtm']
    print(f"There are {len(sdtm_specializations)} SDTM Dataset Specializations in the CDISC Library that specialize {biomedicalConcept}")

    # Get latest SDTM Dataset Specializations that specialize a Biomedical Concept
    biomedicalConcept = "C105585"
    specializations = client.get_sdtm_biomedicalconcept_latest_datasetspecializations("v2", biomedicalConcept)
    sdtm_specializations = specializations['sdtm']
    print(f"There are {len(sdtm_specializations)} SDTM Dataset Specializations in the CDISC Library that specialize {biomedicalConcept}")

    # Get latest SDTM Dataset Specializations that specialize a Biomedical Concept
    biomedicalConcept = "C123456"
    specializations = client.get_sdtm_biomedicalconcept_latest_datasetspecializations("v2", biomedicalConcept)
    sdtm_specializations = specializations['sdtm']
    print(f"There are {len(sdtm_specializations)} SDTM Dataset Specializations in the CDISC Library that specialize {biomedicalConcept}")
