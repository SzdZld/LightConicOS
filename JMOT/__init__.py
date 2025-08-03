import JMOT.connect, JMOT.control, JMOT.craft, JMOT.planet, JMOT.part, JMOT.extra

import importlib
import subprocess
import sys

__all__ = ['connect', 'control', 'craft', 'planet', 'part', 'extra']
__version__ = "0.2.a1"


REQUIRED_PACKAGES = {
    "numpy": None
}

def _install_package(package_name, version_spec=None):
    try:
        if version_spec:
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"{package_name}{version_spec}"])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "-q", package_name])
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