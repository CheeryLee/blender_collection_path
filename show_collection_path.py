#
# Copyright (c) 2021 Alexander "CheeryLee" Pluzhnikov
# 
# This file is part of blender_collection_path.
# 
# blender_collection_path is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# blender_collection_path is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with blender_collection_path.  If not, see <http://www.gnu.org/licenses/>.
#

import bpy
import blf


draw_handler = None
font_size = 11
font_dpi = 72
font_id = 0
font_shadow_alpha = 0.6
version = bpy.app.version


def draw_callback(self, context):
    init_offset = get_init_display_offset()
    offset_x = init_offset[0]
    offset_y = bpy.context.region.height - init_offset[1]
    area = bpy.context.area
    tools_region = None
    header_region = None

    if area.spaces[0].overlay.show_overlays == False:
        return

    for region in area.regions:
        if region.type == 'TOOLS':
            tools_region = region
        elif region.type == 'HEADER':
            header_region = region

    if bpy.context.region.y != header_region.y:
        offset_y -= header_region.height

    if area.spaces[0].show_region_toolbar and tools_region != None:
        offset_x += tools_region.width

    if version >= (2, 90, 0) and area.spaces[0].overlay.show_stats:
        offset_y -= 108

    blf.position(font_id, offset_x, offset_y, 0)
    blf.size(font_id, font_size, font_dpi)
    blf.enable(font_id, blf.SHADOW)
    blf.shadow(font_id, 3, 0, 0, 0, font_shadow_alpha)
    blf.shadow_offset(font_id, 1, -2)
    blf.draw(font_id, get_collection_string(bpy.context.view_layer.objects.active))


def get_init_display_offset() -> tuple:
    if version >= (2, 80, 0) and version < (2, 90, 0):
        return (20, 63)
    elif version >= (2, 90, 0):
        return (10, 58)


def get_collection_string(obj) -> str:
    if obj is None:
        return ""

    if obj.users_collection[0] is bpy.context.scene.collection:
        return "Scene Collection  >  " + obj.name

    return get_collection_tree(obj.users_collection[0].name, bpy.context.scene.collection, "Scene Collection") + obj.name

    
def get_collection_tree(obj_collection_name, collection, path) -> str:
    if obj_collection_name in collection.children.keys():
        return path + "  >  " + obj_collection_name + "  >  "

    for child in collection.children:
        path = path + "  >  " + child.name
        return get_collection_tree(obj_collection_name, child, path)

    return ""


def register():
    draw_handler = bpy.types.SpaceView3D.draw_handler_add(draw_callback, (None, None), 'WINDOW', 'POST_PIXEL')


def unregister():
    bpy.types.SpaceView3D.draw_handler_remove(draw_handler, 'WINDOW')