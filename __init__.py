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
from . import show_collection_path


bl_info = {
    "name": "Show Collection Path",
    "author": "Alexander Pluzhnikov",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D",
    "description": "Shows full collection path where object is in",
    "wiki_url": "https://github.com/CheeryLee/blender_collection_path",
    "category": "3D View"
}


def register():
    show_collection_path.register()
    print("Addon \"Show Collection Path\" enabled")


def unregister():
    show_collection_path.unregister()
    print("Addon \"Show Collection Path\" disabled")


if __name__ == "__main__":
    register()