from dataclasses import (
    dataclass,
    field,
)
from typing import (
    List,
    Optional,
)

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "https://api.medunigraz.at/pke/schema"


@dataclass
class VortragenderType:
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "NAME",
            "type": "Attribute",
        },
    )
    typ: Optional[str] = field(
        default=None,
        metadata={
            "name": "TYP",
            "type": "Attribute",
        },
    )


@dataclass
class TerminType:
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    typ: Optional[int] = field(
        default=None,
        metadata={
            "name": "TYP",
            "type": "Attribute",
        },
    )
    typ_txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "TYP_TXT",
            "type": "Attribute",
        },
    )
    kennung: Optional[str] = field(
        default=None,
        metadata={
            "name": "KENNUNG",
            "type": "Attribute",
        },
    )
    titel: Optional[str] = field(
        default=None,
        metadata={
            "name": "TITEL",
            "type": "Attribute",
        },
    )
    datum: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DATUM",
            "type": "Attribute",
            "format": "%Y-%m-%dT%H:%M:%S",
        },
    )
    zeit_von: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ZEIT_VON",
            "type": "Attribute",
            "format": "%Y-%m-%dT%H:%M:%S",
        },
    )
    zeit_bis: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ZEIT_BIS",
            "type": "Attribute",
            "format": "%Y-%m-%dT%H:%M:%S",
        },
    )
    gebaeude: Optional[str] = field(
        default=None,
        metadata={
            "name": "GEBAEUDE",
            "type": "Attribute",
        },
    )
    raum: Optional[str] = field(
        default=None,
        metadata={
            "name": "RAUM",
            "type": "Attribute",
        },
    )
    raum_bez: Optional[str] = field(
        default=None,
        metadata={
            "name": "RAUM_BEZ",
            "type": "Attribute",
        },
    )
    terminart: Optional[str] = field(
        default=None,
        metadata={
            "name": "TERMINART",
            "type": "Attribute",
        },
    )
    vortragender: List[VortragenderType] = field(
        default_factory=list,
        metadata={
            "name": "VORTRAGENDER",
            "type": "Element",
            "namespace": "https://api.medunigraz.at/pke/schema",
        },
    )


@dataclass
class MedienMonTerminetype:
    class Meta:
        name = "MEDIEN_MON_TERMINEType"

    termin: List[TerminType] = field(
        default_factory=list,
        metadata={
            "name": "TERMIN",
            "type": "Element",
            "namespace": "https://api.medunigraz.at/pke/schema",
        },
    )


@dataclass
class MedienMonTermine(MedienMonTerminetype):
    class Meta:
        name = "MEDIEN_MON_TERMINE"
        namespace = "https://api.medunigraz.at/pke/schema"
