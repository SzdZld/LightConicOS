import importlib
import subprocess
import sys

REQUIRED_PACKAGES = {
    "numpy": None
}

def _install_package(package_name, version_spec=None):
    try:
        if version_spec:
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"{package_name}{version_spec}"])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}: {e}")
        raise

def _validate_dependencies():
    for package, version_spec in REQUIRED_PACKAGES.items():
        try:
            module = importlib.import_module(package)
            if version_spec:
                version = getattr(module, "__version__", None)
                if version and not eval(f"'{version}' {version_spec}"):
                    _install_package(package, version_spec)
        except ImportError:
            _install_package(package, version_spec)

_validate_dependencies()

import JMOT.connect, JMOT.craft, JMOT.planet, JMOT.part, JMOT.extra, JMOT.time, JMOT.control, JMOT.misc
__all__ = ['connect', 'craft', 'planet', 'part', 'extra', 'time', 'control', 'misc']
__version__ = "0.3.a1"

__pdoc__ = {
    '_verify': False,
    '_send_message_with_length': False,
    '_receive_message_with_length': False,
    '_convert_value': False,
    '_parse_message_to_list': False,
    '_send_message': False,
    '_CONTROL_SIGNAL': False,
    '_CRAFT_INFO_SIGNAL': False,
    '_CRAFT_FUEL_SIGNAL': False,
    '_CRAFT_PERFORMANCE_SIGNAL': False,
    '_CRAFT_POSITION_SIGNAL': False,
    '_CRAFT_ATTITUDE_SIGNAL': False,
    '_CRAFT_VELOCITY_SIGNAL': False,
    '_CRAFT_ORBIT_SIGNAL': False,
    '_CRAFT_INPUT_SIGNAL': False,
    '_CRAFT_STATUS_SIGNAL': False,
    '_MISC_CONVERT_SIGNALS': False,
    '_MISC_CAMERA_SIGNALS': False,
    '_MISC_FUNK_SIGNALS': False,
    '_PLANET_INFO_SIGNALS': False,
    '_PLANET_ATMOSPHERE_SIGNALS': False,
    '_PLANET_ORBIT_SIGNALS': False,
    '_PART_SIGNALS': False,
    '_TIME_SIGNALS': False
}