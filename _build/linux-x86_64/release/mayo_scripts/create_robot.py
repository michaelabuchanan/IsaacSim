from isaacsim import SimulationApp

# This sample enables a livestream server to connect to when running headless
CONFIG = {
    "width": 1280,
    "height": 720,
    "window_width": 1920,
    "window_height": 1080,
    "headless": True,
    "hide_ui": False,  # Show the GUI
    "renderer": "RaytracedLighting",
    "display_options": 3286,  # Set display options to show default grid
}

# Start the omniverse application
simulation_app = SimulationApp(launch_config=CONFIG)

import argparse
import sys

import carb
import numpy as np
from isaacsim.core.api import World
from isaacsim.core.api.objects import DynamicCuboid
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.robot.manipulators import SingleManipulator
from isaacsim.robot.manipulators.examples.franka.controllers.pick_place_controller import PickPlaceController
from isaacsim.robot.manipulators.grippers import ParallelGripper
from isaacsim.storage.native import get_assets_root_path
from isaacsim.core.utils.extensions import enable_extension

# Default Livestream settings
simulation_app.set_setting("/app/window/drawMouse", True)
# Enable Livestream extension
enable_extension("omni.kit.livestream.webrtc")
enable_extension("isaacsim.robot_setup.wizard")
enable_extension("isaacsim.asset.exporter.urdf")

# world settings
my_world = World()
my_world.scene.add_default_ground_plane()
#my_world.get_physics_context().set_gravity(-385.827)

# set up OR scene
nuc_path = "omniverse://10.10.51.5"

cart_path = nuc_path + "/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Equipment/Carts/ServiceCart_A/ServiceCart_A01_01.usd"
cart = add_reference_to_stage(usd_path=cart_path, prim_path="/World/moving_cart")




while simulation_app.is_running():
    my_world.step(render=True)
    

simulation_app.close()