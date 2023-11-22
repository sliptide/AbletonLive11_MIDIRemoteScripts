#Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control/__init__.py
from __future__ import absolute_import, print_function, unicode_literals
from .TouchOSC_EC4 import TouchOSC_EC4
from _Framework.Capabilities import controller_id, inport, outport, CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[52], model_name=u'Launch Control'),
     PORTS_KEY: [inport('TouchOSC Bridge', props=[NOTES_CC, SCRIPT]), outport('TouchOSC Bridge', props=[NOTES_CC, SCRIPT])]}


def create_instance(c_instance):
    return TouchOSC_EC4(c_instance)
