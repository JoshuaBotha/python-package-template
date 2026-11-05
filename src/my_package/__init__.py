"""my-package."""

from importlib.metadata import version

__version__ = version("my-package")
__all__ = ["__version__"]
