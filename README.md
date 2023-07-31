# AutoGit

## Install

```shell
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ python -m autogit --version
```

## How to use it?

- yaml file with the following structure:

    ```yaml
    l10n-es:
        origin: https://github.com/OCA/l10n-es
        branch: 16.0
        depth: 1

    stock-logistics-workflow:
        origin: https://github.com/OCA/stock-logistics-workflow
        branch: 16.0
        depth: 1

    # etc
    ```

- Clone the repositories in a specific location:

    ```shell
    (venv) $ python -m autogit clone /location/of/my/repos.yaml -d /home/me/my-repos/
    ```

    - Directory content before to run the script:

        ```shell
        my-repos
        ├─── .
        └─── ..
        ```

    - Directory content after to run the script:

        ```shell
        my-repos
        ├─── .
        ├─── ..
        ├─── l10n-es/
        └─── stock-logistics-workflow/
        ```

