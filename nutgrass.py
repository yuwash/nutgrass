from iotqatools import cb_utils


def AttributeType(name):
    """ Return an attribute class for the given type

    >>> attributes = AttributeType('int')\\
    ...     .get_attributes_creation_from_dict(
    ...             {'color': 0xffffff, 'background-color': 0})
    >>> expected = [
    ...     {'type': 'int', 'name': 'color', 'value': 16777215},
    ...     {'type': 'int', 'name': 'background-color', 'value': 0}]
    >>> attributes.get_attributes() == expected
    True
    """

    class Attribute:

        def __init__(self, name):
            self.name = name

        def add_to_attributes_creation(self, dest, value):
            dest.add_attribute(
                attribute_name=self.name, attribute_type=self.type_name,
                value=value)

        def get_attributes_creation(self, value):
            result = cb_utils.AttributesCreation()
            self.add_to_attributes_creation(result, value)
            return result

        @classmethod
        def add_to_attributes_creation_from_dict(cls, dest, values):
            for name in values:
                cls(name).add_to_attributes_creation(dest, values[name])

        @classmethod
        def get_attributes_creation_from_dict(cls, values):
            result = cb_utils.AttributesCreation()
            cls.add_to_attributes_creation_from_dict(result, values)
            return result

    Attribute.type_name = name
    return Attribute


ATTRIBUTE_TYPES = {'integer': int, 'float': float, 'string': str}


def dict_from_attributes_creation(attributes_creation):
    return {a["name"]: ATTRIBUTE_TYPES.get(a["type"], str)(a["value"]) for a in
            attributes_creation.get_attributes()}


def add_to_attributes_creation_from_context_element_attributes(
        dest, context_element_attributes):
    for a in context_element_attributes:
        AttributeType(a["type"])(a["name"]).add_to_attributes_creation(
                dest, a["value"])


def attributes_creation_from_context_element_attributes(
        context_element_attributes):
    result = cb_utils.AttributesCreation()
    add_to_attributes_creation_from_context_element_attributes(
            result, context_element_attributes)
    return result


def EntityType(name):
    """ Return an entity class for the given type

    >>> entity = EntityType('mouse')('Mickey')
    >>> entity.get_entities_consults().get_entities()
    [{'type': 'mouse', 'id': 'Mickey', 'isPattern': 'false'}]
    """

    class Entity:

        def __init__(self, name):
            """
            :param name: actually the id of entity, but avoiding naming
                conflict with python builtin
            """
            self.name = name

        def add_to_entities_consults(self, dest):
            dest.add_entity(entity_id=self.name, entity_type=self.type_name)

        def get_entities_consults(self):
            result = cb_utils.EntitiesConsults()
            self.add_to_entities_consults(result)
            return result

    Entity.type_name = name
    return Entity


class ContextElementsFactory:
    """ Factory for iotqatools.cb_utils.ContextElements with the given
    entity and attributes
    """
    def __init__(self, entity, attributes_creation):
        """
        :param entity: needs to be of an entity class created through
            EntityType
        :param attributes: needs to be of class
            cb_utils.AttributesCreation
        """
        self.entity = entity
        self.attributes_creation = attributes_creation

    def add_to_context_elements(self, dest):
        dest.add_context_element(
                entity_id=self.entity.name,
                entity_type=self.entity.type_name,
                attributes=self.attributes_creation)

    def get_context_elements(self):
        """
        >>> entity = EntityType('mouse')('Mickey')
        >>> attributes = AttributeType('int')\\
        ...     .get_attributes_creation_from_dict(
        ...             {'color': 0xffffff, 'background-color': 0})
        >>> context_elements = ContextElementsFactory(entity, attributes)\\
        ...     .get_context_elements()
        >>> expected = [{
        ...     'attributes': [
        ...         {'type': 'int', 'name': 'color', 'value': 16777215},
        ...         {'type': 'int', 'name': 'background-color', 'value': 0}],
        ...     'type': 'mouse', 'id': 'Mickey', 'isPattern': 'false'}]
        >>> context_elements.get_context_elements() == expected
        True
        """
        result = cb_utils.ContextElements()
        self.add_to_context_elements(result)
        return result

    @classmethod
    def list_from_context_elements(cls, context_elements):
        return [cls(
            EntityType(e["type"])(e["id"]),
            attributes_creation_from_context_element_attributes(
                e["attributes"])
            ) for e in context_elements.get_context_elements()]


# use ContextElementsFactory.get_context_elements instead!
# def entities_from_context_elements(context_elements):
#   return [EntityType(e["type"])(e["id"]) for e in
#           context_elements.get_context_elements()]
