"""Top-level package for Auto Git fetch."""

__app_name__ = "autogit"
__version__ = "0.1.0"


(
    SUCCESS,
    FILE_ERROR,
    DEST_FOLDER_ERROR,
    PERMISSION_ERROR,
    YAML_ERROR,
) = range(5)


ERRORS = {
    FILE_ERROR: "File not found",
    DEST_FOLDER_ERROR: "Folder not found",
    PERMISSION_ERROR: "Permission error",
}
