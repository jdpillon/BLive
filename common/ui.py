# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


# Script copyright (C) 2012 Thomas Achtner (offtools)

# FIXME: max. Port number in game property is 10000

import bpy

###############################################
#
#       Network Setup Panel
#
###############################################

# TODO: only start / reload / stop button
class BLive_PT_network_setup(bpy.types.Panel):
    bl_label = "BLive Network"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"

    #@classmethod
    #def poll(self, context):
        #pass

    def draw(self, context):
        layout = self.layout
        bs = context.window_manager.blive_settings
        server = bs.server
        port = bs.server

        row = layout.row()
        row.label("Blive Server Settings")
        row = layout.row()

        flow = row.column_flow(columns=2, align=False)
        flow.label("Server:")
        flow.label("Port:")
        flow.prop(bs, "server", text="")
        flow.prop(bs, "port", text="")

        row = layout.row()
        row.operator("blive.start_gameengine", text="Start Gameengine")
        row = layout.row()
        row.operator("blive.reload_gameengine", text="Reload Gameengine")
        row = layout.row()
        row.operator("blive.stop_gameengine", text="Stop Gameengine")

def register():
    print("settings.ui.register")
    bpy.utils.register_class(BLive_PT_network_setup)

def unregister():
    print("settings.ui.unregister")
    bpy.utils.unregister_class(BLive_PT_network_setup)
