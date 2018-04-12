import pathlib
import platform

import pkg_resources

BASE_PATH = pathlib.Path("bin")
EXE_NAME_TMPL = "nucamino-{os}-{arch}{ext}"
EXTENSIONS = {
    "windows": ".exe",
}


def path():
    os = platform.system().lower()
    arch_name, _ = platform.architecture()
    if '32' in arch_name:
        arch = '386'
    else:
        arch = 'amd64'
    ext = EXTENSIONS.get(os, "")
    exe_name = EXE_NAME_TMPL.format(
        os=os,
        arch=arch,
        ext=ext,
    )
    resource_path = BASE_PATH / exe_name
    return pkg_resources.resource_filename(
        "pynucamino",
        str(resource_path),
    )
