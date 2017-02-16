# rmacro
Powerful and easy macro utility. Has support for razer keyboards and custom functions.

## Features
- Play macros anywhere.
- Simple setup through the config file.
- Remembers your macros through shutdowns.
- Can map any key to any other keys (one or multiple).

## Keyboard support
Supports any keyboard, but is preconfigured for the Razer Blackwidow Chroma.

**For the razer macro keys to work, you must install the razer linux driver first.**

## Installation
- First of all, clone this repo. `git clone https://github.com/jlndk/rmacro`
- Then run the installation script `chmod +x install.sh && ./install.sh`
- Run `rmacro.py` or use your prefered way of autostarting it on boot.

## Usage
After the program is installed you can edit the macro by changing the `config.json` file.
An example could look like this:
```json
{
  "keymap": {
      "191": 172,
      "192": 123,
      "193": 122,
      "194": [
          43, 26, 46, 46, 32
      ],
      "195": 0
  }
}

```

The first number on each line (the index) is the keycode of the key you want to press. The second number (the value) is the keycode of the key you want to be pressed. Alternativly you can pass a list of keycodes surrounded by `[]` if you want multiple keys to be pressed sequentially.

For more advanced functions, such as media keys, some special keycodes are provided. All of these are listed on [this wiki page](https://github.com/jlndk/rmacro)

To get these keycodes you can use the provided `keyutil.py` program.

**After the config file is updated, the program must be restarted for the changes to take effect. Alternativly you can just restart your computer if you're unsure how to restart the program.**

## Credit
The general code (listen to and send keys) is based of [https://github.com/igorbb/MacroW](https://github.com/igorbb/MacroW).
