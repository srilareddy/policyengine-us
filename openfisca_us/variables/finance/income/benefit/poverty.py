from openfisca_core.model_api import *
from openfisca_us.entities import *
from openfisca_us.tools.general import *


class spm_unit_poverty_guideline(Variable):
    value_type = float
    entity = SPMUnit
    label = u"Federal poverty guideline for the SPM unit"
    definition_period = YEAR

    def formula(spm_unit, period, parameters):
        n = spm_unit.nb_persons()
        state_group = spm_unit("state_group")
        p_fpg = parameters(period).benefit.poverty.fpg
        p1 = p_fpg.first_person[state_group]
        pn = p_fpg.additional_person[state_group]
        return p1 + pn * (n - 1)
