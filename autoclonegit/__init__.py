"""Top-level package for Auto Git fetch."""

__app_name__ = "autoclonegit"
__version__ = "0.1.0"


(
    SUCCESS,
    FILE_ERROR,
    PERMISSION_ERROR,
    YAML_ERROR,
) = range(4)


ERRORS = {
    FILE_ERROR: "file not found",
    PERMISSION_ERROR: "permission error",
}
