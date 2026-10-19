"""Shared path constants for the Deep-Live-Cam project."""

import os
import sys


def _app_dir() -> str:
    """Directory that survives PyInstaller one-file extraction (temp dir is wiped).

    Priority: $DLC_HOME > dir of the frozen executable > repo root (source runs).
    """
    env = os.environ.get("DLC_HOME")
    if env:
        return env
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = _app_dir()
MODELS_DIR = os.path.join(APP_DIR, "models")
