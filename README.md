# File Color Tag 1.0.0

**File Color Tag** is a Nautilus extension for GNOME that brings macOS-style color tags to Linux.  
It allows you to mark files and folders with color-coded tags directly from the right-click context menu, improving visual organization and quick identification.

## ✨ Features

- Apply color tags to any file or folder
- Toggle tags on/off with a click
- Multiple tags supported simultaneously
- Compatible with all Nautilus file systems (including symbolic links and mounted volumes)
- Uses visually colored dots in the menu, just like macOS

## 🖼️ Preview

Right-click on a file → **Set color TAG...**  
You’ll see a list of color tags like 🔴 Red, 🟢 Green, etc.  
Clicking a tag again removes it.

## 📦 Installation

1. **Copy the extension to Nautilus' extensions folder**

   ```bash
   mkdir -p ~/.local/share/nautilus-python/extensions/
   cp file_color_tag.py ~/.local/share/nautilus-python/extensions/
   ```


3. **Restart Nautilus**

   ```bash
   nautilus -q
   ```

## 🐧 Requirements

- Nautilus 43+ with Python support
- Python 3.x
- `nautilus-python` and `python3-gi` installed (usually available via package manager)

   For Ubuntu/Debian:

   ```bash
   sudo apt install nautilus-python python3-gi
   ```

## 🔄 Uninstallation

```bash
rm ~/.local/share/nautilus-python/extensions/file_color_tag.py
nautilus -q
```

Optionally remove icons:

```bash
rm ~/.icons/hicolor/48x48/emblems/emblem-colors-*.png
gtk-update-icon-cache ~/.icons/hicolor/48x48/emblems/
```

## 📖 License

MIT License – use it freely and modify it as you wish.

---

Inspired by macOS Finder's tag system, but made for the Linux desktop.
