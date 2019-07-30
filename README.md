# KoikatuSaveDataEdit

GUI for editing koikatu save file

## installation (Windows 10)

Download this Repo (e.g. C:\Git\KoikatsuSaveDataEdit)

Open Powershell as Admin
Intall Chocolatey 
```Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))```

Run the following commands using the package manager:
```
> choco install python
```

Install Python Dependencies:

```
> pip install pillow
? pip install msgpack
```
Copy Save File to Repo Directory (e.g. C:\Git\KoikatsuSaveDataEdit)

Edit the save:

```
> python gui.py file01.dat
```

## usage

Run gui.py (or gui.exe) with save file. Python 3.6 required.

```
> python gui.py file01.dat
```

## install (for execute gui.py)

Copy *.py and resource_ja.json.
And you have to install dependency packages.

```
$ pip3 install pillow
$ pip3 install msgpack
```

## build

This project is built with [PyInstaller](http://www.pyinstaller.org/) on Winodws.
You have to install dependency packages(See requirements.txt) before build.


## thanks

This program uses some codes from following repositories.

* https://github.com/106-/KoikatuCharaLoader
* https://gist.github.com/EugeneBakin/76c8f9bcec5b390e45df

It is based on Code changes pointed out here:
* http://hongfire.com/forum/forum/hentai-lair/hf-modding-translation/5990340-illusion-koikatu-koikatsu-%E3%82%B3%E3%82%A4%E3%82%AB%E3%83%84%EF%BC%81-mods-no-discussion-allowed/page5
