# -*- coding: utf-8 -*-

import arcpy

from ags_tools.CompositeSourceCreator import CompositeSourceCreator


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "CSF/PRF Toolbox"
        self.alias = "CSF/PRF Toolbox"

        self.tools = [CompositeSourceCreator]
