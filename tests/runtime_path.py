import importlib.util
import os
from types import ModuleType


def load_gateway(name: str) -> ModuleType:
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../runtime/gateway", f"{name}.py"))
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
