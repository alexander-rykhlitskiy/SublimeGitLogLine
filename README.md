# Sublime Text plugin: GitLogLine

Shows log for selected line.

## Install

Thanks to [https://github.com/kemayo/sublime-text-git/wiki](https://github.com/kemayo/sublime-text-git/wiki) for documenting these steps originally.

First, you need to have `git` installed and in your `$PATH`. Afterwards you may need to restart Sublime Text 3 before the plugin will work.

### Linux (Ubuntu like distros)

```bash
cd ~/.config/sublime-text-3/Packages/
git clone git@github.com:alexander-rykhlitskiy/SublimeGitLogLine.git GitLogLine
```

### OSX

```bash
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
git clone git@github.com:alexander-rykhlitskiy/SublimeGitLogLine.git GitLogLine
```

### Windows 7:

    Copy the directory to: "C:\Users\<username>\AppData\Roaming\Sublime Text 3\Packages"

### Windows XP:

    Copy the directory to: "C:\Documents and Settings\<username>\Application Data\Sublime Text 3\Packages"

## Usage

- Bring up the Command Palette (Control+Shift+p on Linux/Windows, Command+Shift+p on OS X).
- Select `Git Log: current line`

## TODO

Make log follow renames
