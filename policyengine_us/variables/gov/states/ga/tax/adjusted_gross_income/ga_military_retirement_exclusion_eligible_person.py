from policyengine_us.model_api import *


class ga_military_retirement_exclusion_eligible_person(Variable):
    value_type = bool
    entity = Person
    label = "Georgia military retirement exclusion"
    definition_period = YEAR
    reference = (
        "https://dor.georgia.gov/document/booklet/2021-it-511-individual-income-tax-booklet/download#page=15"
        "https://dor.georgia.gov/document/document/2022-it-511-individual-income-tax-booklet/download#page=15"
        "https://advance.lexis.com/documentpage/?pdmfid=1000516&crid=fb5db531-a80f-4790-bddb-eefc8327ef60&config=00JAA1MDBlYzczZi1lYjFlLTQxMTgtYWE3OS02YTgyOGM2NWJlMDYKAFBvZENhdGFsb2feed0oM9qoQOMCSJFX5qkd&pddocfullpath=%2Fshared%2Fdocument%2Fstatutes-legislation%2Furn%3AcontentItem%3A65D2-CDH3-CGX8-044N-00008-00&pdcontentcomponentid=234186&pdteaserkey=sr1&pditab=allpods&ecomp=8s65kkk&earg=sr1&prid=66f02b0a-c5ae-4162-9535-127751546807"
    )
    defined_for = StateCode.GA

    def formula(Person, period, parameters):
        person = person.members
        p = parameters(period).gov.states.ga.tax.income.agi.exclusions.military
        head = person("is_tax_unit_head", period)
        spouse = person("is_tax_unit_spouse", period)
        military_age = person("age", period) < p.age

        return (head | spouse) & military_age
