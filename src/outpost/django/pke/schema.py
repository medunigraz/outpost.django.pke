# src/outpost/django/pke/schema.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c62a48c0eea2a9fd928149c938e945eab4c45571
# Generated 2019-05-22 12:32:50.741544 by PyXB version 1.2.6 using Python 3.7.3.candidate.1
# Namespace https://api.medunigraz.at/pke/schema

from __future__ import unicode_literals

import io
import sys

import pyxb
import pyxb.binding
# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import pyxb.binding.saxer
import pyxb.utils.domutils
import pyxb.utils.six as _six
import pyxb.utils.utility

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f30eb0d2-7c7c-11e9-99b1-005056ad5801')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()


# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('https://api.medunigraz.at/pke/schema', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {https://api.medunigraz.at/pke/schema}MEDIEN_MON_TERMINEType with content type ELEMENT_ONLY
class MEDIEN_MON_TERMINEType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {https://api.medunigraz.at/pke/schema}MEDIEN_MON_TERMINEType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MEDIEN_MON_TERMINEType')
    _XSDLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 5, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {https://api.medunigraz.at/pke/schema}TERMIN uses Python identifier TERMIN
    __TERMIN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TERMIN'), 'TERMIN', '__httpsapi_medunigraz_atpkeschema_MEDIEN_MON_TERMINEType_httpsapi_medunigraz_atpkeschemaTERMIN', True, pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 7, 12), )

    
    TERMIN = property(__TERMIN.value, __TERMIN.set, None, None)

    _ElementMap.update({
        __TERMIN.name() : __TERMIN
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MEDIEN_MON_TERMINEType = MEDIEN_MON_TERMINEType
Namespace.addCategoryObject('typeBinding', 'MEDIEN_MON_TERMINEType', MEDIEN_MON_TERMINEType)


# Complex type {https://api.medunigraz.at/pke/schema}TerminType with content type ELEMENT_ONLY
class TerminType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {https://api.medunigraz.at/pke/schema}TerminType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TerminType')
    _XSDLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {https://api.medunigraz.at/pke/schema}VORTRAGENDER uses Python identifier VORTRAGENDER
    __VORTRAGENDER = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'VORTRAGENDER'), 'VORTRAGENDER', '__httpsapi_medunigraz_atpkeschema_TerminType_httpsapi_medunigraz_atpkeschemaVORTRAGENDER', True, pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 24, 12), )

    
    VORTRAGENDER = property(__VORTRAGENDER.value, __VORTRAGENDER.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__httpsapi_medunigraz_atpkeschema_TerminType_ID', pyxb.binding.datatypes.int)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 11, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 11, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute TYP uses Python identifier TYP
    __TYP = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TYP'), 'TYP', '__httpsapi_medunigraz_atpkeschema_TerminType_TYP', pyxb.binding.datatypes.int)
    __TYP._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 12, 8)
    __TYP._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 12, 8)
    
    TYP = property(__TYP.value, __TYP.set, None, None)

    
    # Attribute TYP_TXT uses Python identifier TYP_TXT
    __TYP_TXT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TYP_TXT'), 'TYP_TXT', '__httpsapi_medunigraz_atpkeschema_TerminType_TYP_TXT', pyxb.binding.datatypes.string)
    __TYP_TXT._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 13, 8)
    __TYP_TXT._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 13, 8)
    
    TYP_TXT = property(__TYP_TXT.value, __TYP_TXT.set, None, None)

    
    # Attribute KENNUNG uses Python identifier KENNUNG
    __KENNUNG = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'KENNUNG'), 'KENNUNG', '__httpsapi_medunigraz_atpkeschema_TerminType_KENNUNG', pyxb.binding.datatypes.string)
    __KENNUNG._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 14, 8)
    __KENNUNG._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 14, 8)
    
    KENNUNG = property(__KENNUNG.value, __KENNUNG.set, None, None)

    
    # Attribute TITEL uses Python identifier TITEL
    __TITEL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TITEL'), 'TITEL', '__httpsapi_medunigraz_atpkeschema_TerminType_TITEL', pyxb.binding.datatypes.string)
    __TITEL._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 15, 8)
    __TITEL._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 15, 8)
    
    TITEL = property(__TITEL.value, __TITEL.set, None, None)

    
    # Attribute DATUM uses Python identifier DATUM
    __DATUM = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DATUM'), 'DATUM', '__httpsapi_medunigraz_atpkeschema_TerminType_DATUM', pyxb.binding.datatypes.dateTime)
    __DATUM._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 16, 8)
    __DATUM._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 16, 8)
    
    DATUM = property(__DATUM.value, __DATUM.set, None, None)

    
    # Attribute ZEIT_VON uses Python identifier ZEIT_VON
    __ZEIT_VON = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ZEIT_VON'), 'ZEIT_VON', '__httpsapi_medunigraz_atpkeschema_TerminType_ZEIT_VON', pyxb.binding.datatypes.dateTime)
    __ZEIT_VON._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 17, 8)
    __ZEIT_VON._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 17, 8)
    
    ZEIT_VON = property(__ZEIT_VON.value, __ZEIT_VON.set, None, None)

    
    # Attribute ZEIT_BIS uses Python identifier ZEIT_BIS
    __ZEIT_BIS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ZEIT_BIS'), 'ZEIT_BIS', '__httpsapi_medunigraz_atpkeschema_TerminType_ZEIT_BIS', pyxb.binding.datatypes.dateTime)
    __ZEIT_BIS._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 18, 8)
    __ZEIT_BIS._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 18, 8)
    
    ZEIT_BIS = property(__ZEIT_BIS.value, __ZEIT_BIS.set, None, None)

    
    # Attribute GEBAEUDE uses Python identifier GEBAEUDE
    __GEBAEUDE = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GEBAEUDE'), 'GEBAEUDE', '__httpsapi_medunigraz_atpkeschema_TerminType_GEBAEUDE', pyxb.binding.datatypes.string)
    __GEBAEUDE._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 19, 8)
    __GEBAEUDE._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 19, 8)
    
    GEBAEUDE = property(__GEBAEUDE.value, __GEBAEUDE.set, None, None)

    
    # Attribute RAUM uses Python identifier RAUM
    __RAUM = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'RAUM'), 'RAUM', '__httpsapi_medunigraz_atpkeschema_TerminType_RAUM', pyxb.binding.datatypes.string)
    __RAUM._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 20, 8)
    __RAUM._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 20, 8)
    
    RAUM = property(__RAUM.value, __RAUM.set, None, None)

    
    # Attribute RAUM_BEZ uses Python identifier RAUM_BEZ
    __RAUM_BEZ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'RAUM_BEZ'), 'RAUM_BEZ', '__httpsapi_medunigraz_atpkeschema_TerminType_RAUM_BEZ', pyxb.binding.datatypes.string)
    __RAUM_BEZ._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 21, 8)
    __RAUM_BEZ._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 21, 8)
    
    RAUM_BEZ = property(__RAUM_BEZ.value, __RAUM_BEZ.set, None, None)

    
    # Attribute TERMINART uses Python identifier TERMINART
    __TERMINART = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TERMINART'), 'TERMINART', '__httpsapi_medunigraz_atpkeschema_TerminType_TERMINART', pyxb.binding.datatypes.string)
    __TERMINART._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 22, 8)
    __TERMINART._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 22, 8)
    
    TERMINART = property(__TERMINART.value, __TERMINART.set, None, None)

    _ElementMap.update({
        __VORTRAGENDER.name() : __VORTRAGENDER
    })
    _AttributeMap.update({
        __ID.name() : __ID,
        __TYP.name() : __TYP,
        __TYP_TXT.name() : __TYP_TXT,
        __KENNUNG.name() : __KENNUNG,
        __TITEL.name() : __TITEL,
        __DATUM.name() : __DATUM,
        __ZEIT_VON.name() : __ZEIT_VON,
        __ZEIT_BIS.name() : __ZEIT_BIS,
        __GEBAEUDE.name() : __GEBAEUDE,
        __RAUM.name() : __RAUM,
        __RAUM_BEZ.name() : __RAUM_BEZ,
        __TERMINART.name() : __TERMINART
    })
_module_typeBindings.TerminType = TerminType
Namespace.addCategoryObject('typeBinding', 'TerminType', TerminType)


# Complex type {https://api.medunigraz.at/pke/schema}VortragenderType with content type EMPTY
class VortragenderType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {https://api.medunigraz.at/pke/schema}VortragenderType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VortragenderType')
    _XSDLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 27, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__httpsapi_medunigraz_atpkeschema_VortragenderType_ID', pyxb.binding.datatypes.int)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 28, 8)
    __ID._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 28, 8)
    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Attribute NAME uses Python identifier NAME
    __NAME = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NAME'), 'NAME', '__httpsapi_medunigraz_atpkeschema_VortragenderType_NAME', pyxb.binding.datatypes.string)
    __NAME._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 29, 8)
    __NAME._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 29, 8)
    
    NAME = property(__NAME.value, __NAME.set, None, None)

    
    # Attribute TYP uses Python identifier TYP
    __TYP = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TYP'), 'TYP', '__httpsapi_medunigraz_atpkeschema_VortragenderType_TYP', pyxb.binding.datatypes.string)
    __TYP._DeclarationLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 30, 8)
    __TYP._UseLocation = pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 30, 8)
    
    TYP = property(__TYP.value, __TYP.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ID.name() : __ID,
        __NAME.name() : __NAME,
        __TYP.name() : __TYP
    })
_module_typeBindings.VortragenderType = VortragenderType
Namespace.addCategoryObject('typeBinding', 'VortragenderType', VortragenderType)


MEDIEN_MON_TERMINE = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MEDIEN_MON_TERMINE'), MEDIEN_MON_TERMINEType, location=pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 4, 4))
Namespace.addCategoryObject('elementBinding', MEDIEN_MON_TERMINE.name().localName(), MEDIEN_MON_TERMINE)



MEDIEN_MON_TERMINEType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TERMIN'), TerminType, scope=MEDIEN_MON_TERMINEType, location=pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 7, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 7, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MEDIEN_MON_TERMINEType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TERMIN')), pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 7, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MEDIEN_MON_TERMINEType._Automaton = _BuildAutomaton()




TerminType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'VORTRAGENDER'), VortragenderType, scope=TerminType, location=pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 24, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 24, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TerminType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'VORTRAGENDER')), pyxb.utils.utility.Location('/home/o_fladiscm/development/src/outpost/django/pke/schema.xsd', 24, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TerminType._Automaton = _BuildAutomaton_()
