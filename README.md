# cdisc-library-client

Python client for accessing the CDISC library. Deployed to PYPI

## operations

```
get_sdtm - get an sdtm standard
get_adam - get an adam or adamig standard
get_cdash - get a cdash standard
get_sdtmig - gets sdtmig standard
get_sendig - gets sendig standard
get_cdashig - gets cdashig standard

get_terminology_package - get a ct package given the version
get_codelist_terms - returns an array of all terms in a codelist
get_codelist_term - returns the library representation of a codelist term

get_rule_catalogs - returns a list of links to all rule catalogs in the CDISC Library
get_rules_catalog - returns all rules in a single rules catalog.
get_rule - gets a rule definition given standard, version, and rule id

get_bc_packages - get biomedical concept package list
get_bc_package_biomedicalconcepts - get biomedical concept list in a package 
get_bc_package_biomedicalconcept - get biomedical concept in a package
get_bc_latest_biomedicalconcepts - get biomedical concept list (latest versions)
get_bc_latest_biomedicalconcept - get biomedical concept (latest version)
get_bc_categories - get biomedical concept categories list
get_bc_latest_biomedicalconcepts_category - get biomedical concepts for a given category (latest version)

get_sdtm_packages - get sdtm dataset specialization package list
get_sdtm_package_datasetspecializations - get sdtm dataset specialization list in a package
get_sdtm_package_datasetspecialization - get sdtm dataset specialization in a package
get_sdtm_latest_sdtm_datasetspecializations - get sdtm dataset specialization list (latest versions)
get_sdtm_latest_sdtm_datasetspecialization - get sdtm dataset specialization (latest version)
get_sdtm_domains - get sdtm dataset specialization domain list
get_sdtm_latest_sdtm_datasetspecializations_domain - get a list of sdtm dataset specializations for a given domain (latest version)

get_biomedicalconcept_latest_datasetspecializations - get a list of dataset specializations that specialize a biomedical concept (latest versions)
```

More info on CDISC Library API endpoints can be found at the [CDISC Library API Portal](https://api.developer.library.cdisc.org/).
