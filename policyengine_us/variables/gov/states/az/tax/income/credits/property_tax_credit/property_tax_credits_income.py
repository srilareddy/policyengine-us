from policyengine_us.model_api import *


class az_property_tax_credit_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "Income to calculate the arizona property tax the credit"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.AZ

    adds = [
        "capital_gains_excluded_from_taxable_income",
        "tax_exempt_interest_income",
        "public_pension_income",
        "adjusted_gross_income",
    ]
