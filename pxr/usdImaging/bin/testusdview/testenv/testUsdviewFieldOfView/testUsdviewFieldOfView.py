#!/pxrpythonsubst
#
# Copyright 2017 Pixar
#
# Licensed under the Apache License, Version 2.0 (the "Apache License")
# with the following modification; you may not use this file except in
# compliance with the Apache License and the following modification to it:
# Section 6. Trademarks. is deleted and replaced with:
#
# 6. Trademarks. This License does not grant permission to use the trade
#    names, trademarks, service marks, or product names of the Licensor
#    and its affiliates, except as required to comply with Section 4(c) of
#    the License and to reproduce the content of the NOTICE file.
#
# You may obtain a copy of the Apache License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the Apache License with the above modification is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the Apache License for the specific
# language governing permissions and limitations under the Apache License.
#

# Remove any unwanted visuals from the view.
def _modifySettings(appController):
    appController._dataModel.viewSettings.showBBoxes = False
    appController._dataModel.viewSettings.showHUD = False

# Set the field of view and refresh the view.
def _setFOV(appController, fov):
    appController._dataModel.viewSettings.freeCamera.fov = fov
    appController._stageView.updateGL()

# Test 45 degree FOV.
def _test45Degree(appController):
    _setFOV(appController, 45)
    appController._takeShot("fov45.png")

# Test 60 degree FOV.
def _test60Degree(appController):
    _setFOV(appController, 60)
    appController._takeShot("fov60.png")

# Test 90 degree FOV.
def _test90Degree(appController):
    _setFOV(appController, 90)
    appController._takeShot("fov90.png")

# Test that the FOV setting work properly in usdview.
def testUsdviewInputFunction(appController):
    _modifySettings(appController)
    _test45Degree(appController)
    _test60Degree(appController)
    _test90Degree(appController)
