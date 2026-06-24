from setuptools import setup
from setuptools.extension import Extension
from Cython.Distutils import build_ext

import glob
import sys

source_files = ["enet.pyx"]

_enet_files = glob.glob("enet/*.c")

if not _enet_files:
    print("The enet/ submodule is empty")
    print("If you didn't clone with --recursive, fetch with:")
    print("    git submodule update --init --recursive")
    print("See the README for more instructions")
    sys.exit(1)

source_files.extend(_enet_files)

define_macros = [('HAS_POLL', None),
                 ('HAS_FCNTL', None),
                 ('HAS_MSGHDR_FLAGS', None),
                 ('HAS_SOCKLEN_T', None) ]

libraries = []

if sys.platform == 'win32':
    define_macros.extend([('WIN32', None)])
    libraries.extend(['ws2_32', 'Winmm'])

if sys.platform != 'darwin':
    define_macros.extend([('HAS_GETHOSTBYNAME_R', None), ('HAS_GETHOSTBYADDR_R', None)])

ext_modules = [
    Extension(
        "enet",
        extra_compile_args=["-O3"],
        sources=source_files,
        include_dirs=["enet/include/"],
        define_macros=define_macros,
        libraries=libraries)]

setup(
  name = 'enet',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
