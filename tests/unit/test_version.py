import my_package


def test_version_matches_installed_metadata():
    from importlib.metadata import version

    assert my_package.__version__ == version("my-package")
