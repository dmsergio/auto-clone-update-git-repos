"""Top-level package for Auto Git fetch."""

__app_name__ = "autoclonegit"
__version__ = "0.1.0"


(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    PERMISSION_ERROR,
    YAML_ERROR,
) = range(5)


ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    PERMISSION_ERROR: "permission error",
}
