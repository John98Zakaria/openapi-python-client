from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.an_enum import AnEnum
from ..models.an_int_enum import AnIntEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelWithUnionProperty")


@attr.s(auto_attribs=True)
class ModelWithUnionProperty:
    """
    Attributes:
        a_property (Union[AnEnum, AnIntEnum, Unset]):
    """

    a_property: Union[AnEnum, AnIntEnum, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        a_property: Union[Unset, int, str]
        if isinstance(self.a_property, Unset):
            a_property = UNSET
        elif isinstance(self.a_property, AnEnum):
            a_property = UNSET
            if not isinstance(self.a_property, Unset):
                a_property = self.a_property.value

        else:
            a_property = UNSET
            if not isinstance(self.a_property, Unset):
                a_property = self.a_property.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if a_property is not UNSET:
            field_dict["a_property"] = a_property

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_a_property(data: object) -> Union[AnEnum, AnIntEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _a_property_type_0 = data
                a_property_type_0: Union[Unset, AnEnum]
                if isinstance(_a_property_type_0, Unset):
                    a_property_type_0 = UNSET
                else:
                    a_property_type_0 = AnEnum(_a_property_type_0)

                return a_property_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, int):
                raise TypeError()
            _a_property_type_1 = data
            a_property_type_1: Union[Unset, AnIntEnum]
            if isinstance(_a_property_type_1, Unset):
                a_property_type_1 = UNSET
            else:
                a_property_type_1 = AnIntEnum(_a_property_type_1)

            return a_property_type_1

        a_property = _parse_a_property(d.pop("a_property", UNSET))

        model_with_union_property = cls(
            a_property=a_property,
        )

        return model_with_union_property
