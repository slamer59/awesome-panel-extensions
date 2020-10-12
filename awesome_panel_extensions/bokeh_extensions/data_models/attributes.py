from bokeh.core.properties import Bool, String

from awesome_panel_extensions.bokeh_extensions.data_models.parameter_model import ParameterModel


class AttributeModel(ParameterModel):
    attribute = String()


class BooleanAttribute(AttributeModel):
    """Example implementation of a Custom Bokeh Model"""

    value = Bool()


class StringAttribute(AttributeModel):
    """Example implementation of a Custom Bokeh Model"""

    value = String()