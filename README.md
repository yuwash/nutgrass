# nutgrass

[![Build Status](https://api.travis-ci.org/yuwash/nutgrass.svg?branch=master)](https://travis-ci.org/yuwash/nutgrass)

Simple NGSI utility

Currently Python3 is not supported, because this depends on
[iotqatools](https://github.com/telefonicaid/iotqatools) that doesn't.

## Installation
As iotqatools is not available from PyPI, you need to do this:

```sh
# before: git clone this repository and cd to the directory
pip install -r requirements.txt
```

## API

### ContextElementsFactory

```python
class ContextElementsFactory
 |  Factory for iotqatools.cb_utils.ContextElements with the given
 |  entity and attributes
 |
 |  Methods defined here:
 |
 |  __init__(self, entity, attributes_creation)
 |      :param entity: needs to be of an entity class created through
 |          EntityType
 |      :param attributes: needs to be of class
 |          cb_utils.AttributesCreation
 |
 |  add_to_context_elements(self, dest)
 |
 |  get_context_elements(self)
 |      >>> entity = EntityType('mouse')('Mickey')
 |      >>> attributes = AttributeType('int')\
 |      ...     .get_attributes_creation_from_dict(
 |      ...             {'color': 0xffffff, 'background-color': 0})
 |      >>> context_elements = ContextElementsFactory(entity, attributes)\
 |      ...     .get_context_elements()
 |      >>> expected = [{
 |      ...     'attributes': [
 |      ...         {'type': 'int', 'name': 'color', 'value': 16777215},
 |      ...         {'type': 'int', 'name': 'background-color', 'value': 0}],
 |      ...     'type': 'mouse', 'id': 'Mickey', 'isPattern': 'false'}]
 |      >>> context_elements.get_context_elements() == expected
 |      True
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  list_from_context_elements(cls, context_elements) from __builtin__.classobj
```

### Functions

```python
AttributeType(name)
    Return an attribute class for the given type

    >>> attributes = AttributeType('int')\
    ...     .get_attributes_creation_from_dict(
    ...             {'color': 0xffffff, 'background-color': 0})
    >>> expected = [
    ...     {'type': 'int', 'name': 'color', 'value': 16777215},
    ...     {'type': 'int', 'name': 'background-color', 'value': 0}]
    >>> attributes.get_attributes() == expected
    True

EntityType(name)
    Return an entity class for the given type

    >>> entity = EntityType('mouse')('Mickey')
    >>> entity.get_entities_consults().get_entities()
    [{'type': 'mouse', 'id': 'Mickey', 'isPattern': 'false'}]

add_to_attributes_creation_from_context_element_attributes(dest, context_element_attributes)

attributes_creation_from_context_element_attributes(context_element_attributes)

dict_from_attributes_creation(attributes_creation)
```
