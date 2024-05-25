# EruPad

https://www.microsoft.com/store/productId/9NL2Z6GQRC74?ocid=pdpshare

EruPad is a notepad app that implements only the minimum features necessary as a notepad, and provides additional features as separate extensions.

To install and use extensions in EruPad, you need to do the following steps in advance.

## Prerequisites
1. Place IronPython 3.4.1 StdLib in any location

    Download IronPython.StdLib.3.4.1.zip from the following link and unzip it to any location.
    https://github.com/IronLanguages/ironpython3/releases

1. Set the path of IronPython StdLib

    Launch EruPad, select `Tools` > `Settings` > `User Settings` from the menu bar, and add the following settings.

    ```json
    {
        "extension.stdlib_path": "<Folder path where StdLib is placed>"
    }
    ```

1. Install ExtensionManager

    Select `Help` > `About` from the EruPad menu bar, and click on the `Install ExtensionManager extension` link at the bottom of the screen.

1. Restart EruPad

## Installing extensions

EruPad extensions are published in this repository.

You can install various extensions by following these steps.

1. Launch ExtensionManager in EruPad

    Press `Ctrl` + `Shift` + `X` keys simultaneously to launch ExtensionManager.

1. Install the package.json of the target extension.

    Drag and drop the package.json file located at the root of the extension directory structure into the ExtensionManager screen.

1. Restart EruPad.

## About package.json

It is always located at the root of the extension directory structure.
The contents of package.json are created with reference to vscode's extension manifest.
