# Obsidian G Drive

This project provides a Python script that automates the process of uploading images from a local Obsidian vault to Google Drive and replacing the local image paths with their corresponding Google Drive links. The image files are then removed from the vault. 

---

## Usage

To use this script, follow the steps below:

1. Clone the repository to your local machine
2. Install the required dependencies by running `pip install -r requirements.txt`
3. [Setup your Google Service API](https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf)

    Post setup, your settigns.yaml file should look like the following,

    ```yaml
        client_config_backend: settings
        client_config:
        client_id: <YOUR CLIENT ID>
        client_secret: <YOUR CLIENT SECRET>
        save_credentials: True

        save_credentials_backend: file
        save_credentials_file: credentials.json

        get_refresh_token: True
        oauth_scope:
        - https://www.googleapis.com/auth/drive.file

    ```

    Note: The client_secret.json file will be generated when you run the program for the first time. It will be used for automatic authentication.

4. Create a config.yml file as below,
    ```yml
        drive_parent_id: <ID OF YOUR GOOGLE DRIVE FOLDER>
        base_path: /path/to/Obsidian/vault/
        paths_to_exclude:
            - '/path/to/exclude1/'
            - '/path/to/exclude2/'
    ```

5. Run the script by running `python main.py`

---

## Contributing:

Contributions to this project are always welcome. If you have any suggestions or improvements, please open an issue or submit a pull request.

---

## License

This project is licensed under the [GNU GPLv3 License](https://github.com/Nishanth-Gobi/Obsidian-G-Drive/blob/main/license).
