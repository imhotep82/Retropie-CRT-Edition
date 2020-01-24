#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
paths_lib.py.

https://github.com/krahsdevil/crt-for-retropie/

Copyright (C)  2018/2019 -krahs- - https://github.com/krahsdevil/
Copyright (C)  2019 dskywalk - http://david.dantoine.org

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 2 of the License, or (at your option) any
later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License along
with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import os

TMP_LAUNCHER_PATH = "/dev/shm"

# retropie path setup
RETROPIE_PATH = "/opt/retropie"
RETROPIECFG_PATH = os.path.join(RETROPIE_PATH, "configs")
RETROPIEEMU_PATH = os.path.join(RETROPIE_PATH, "emulators")

# emulationstation path setup
ESCFG_PATH = os.path.join(RETROPIECFG_PATH, "all/emulationstation")

# CRT main software paths
CRTROOT_PATH = os.path.join(RETROPIECFG_PATH, "all/CRT")
CRTBIN_PATH = os.path.join(CRTROOT_PATH, "bin")

# CRT main additional software path (configs, resources, modules)
CRTCONTENT_PATH = os.path.join(CRTBIN_PATH, "ScreenUtilityFiles")

# CRT configurations
CRTCONFIG_PATH = os.path.join(CRTCONTENT_PATH, "config_files")

# CRT resources
CRTRESOURCES_PATH = os.path.join(CRTCONTENT_PATH, "resources")
CRTASSETS_PATH = os.path.join(CRTRESOURCES_PATH, "assets")
CRTLAUNCHIMAGES_SET_PATH = os.path.join(CRTASSETS_PATH, "screen_emulationstation/CRTResources/launch_images_modes")
CRTICONS_SET_PATH = os.path.join(CRTASSETS_PATH, "screen_emulationstation/CRTResources/crt_icons")
CRTFONTS_PATH = os.path.join(CRTASSETS_PATH, "screen_fonts")
CRTADDONS_PATH = os.path.join(CRTRESOURCES_PATH, "addons")

# CRT scripts modules
CRTMODULES_PATH = os.path.join(CRTCONTENT_PATH, "bin")

# raspbian path setup
BOOTCFG_FILE = "/boot/config.txt"