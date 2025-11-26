#!/usr/bin/env python3
"""
Bootstrapper: attempts to run the Jarvis app located at Jarvis/jarvis.py.

Behaviour:
 - import Jarvis.jarvis and try calling a known entry function:
   ['main','run','run_jarvis','start','listen']
 - if none found, fallback to executing the Jarvis/jarvis.py as a script (__main__).
This keeps it flexible without changing your existing jarvis.py too much.
"""

import sys
import importlib
import os
from types import ModuleType

MODULE_PATH = "Jarvis.jarvis"
FALLBACK_NAMES = ["main", "run", "run_jarvis", "start", "listen"]

def call_first_callable(mod: ModuleType, names):
    for n in names:
        fn = getattr(mod, n, None)
        if callable(fn):
            print(f"[main.py] Calling entry function: {n}()")
            try:
                fn()
            except TypeError:
                # maybe function expects args; call without args anyway
                fn()
            return True
    return False

def exec_fallback(filepath):
    print(f"[main.py] No known entry found — executing file as __main__: {filepath}")
    with open(filepath, "rb") as f:
        code = compile(f.read(), filepath, "exec")
        globs = {"__name__": "__main__", "__file__": filepath}
        exec(code, globs)

def main():
    try:
        mod = importlib.import_module(MODULE_PATH)
    except Exception as e:
        print(f"[main.py] ERROR: failed to import {MODULE_PATH}: {e}", file=sys.stderr)
        # fallback: try executing the file directly
        possible = os.path.join(os.path.dirname(__file__), "Jarvis", "jarvis.py")
        if os.path.exists(possible):
            exec_fallback(possible)
            return
        sys.exit(1)

    if call_first_callable(mod, FALLBACK_NAMES):
        return

    # No entry function found — fallback to executing file as script
    possible = os.path.join(os.path.dirname(__file__), "Jarvis", "jarvis.py")
    if os.path.exists(possible):
        exec_fallback(possible)
        return

    print("[main.py] ERROR: Could not run the Jarvis app — no entrypoint found.", file=sys.stderr)
    sys.exit(2)

if __name__ == "__main__":
    main()
