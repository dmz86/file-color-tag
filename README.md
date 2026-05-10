# File Color Tag 2.0.0

**File Color Tag** is a Nautilus extension for GNOME that brings macOS-style color labels to Linux.  
It allows you to mark files and folders with color-coded labels directly from the right-click context menu, improving visual organization and quick identification.

## ✨ Features

- 🎨 Apply color labels to any file or folder
- 🔄 Toggle labels on/off with a single click
- 🏷️ Multiple labels supported simultaneously
- 🌍 Built-in i18n support (English, Italian — easily extensible)
- 🔧 Auto-detects Nautilus API version (compatible with Ubuntu 24.04 and 26.04+)
- 📂 Compatible with all Nautilus file systems (including symbolic links and mounted volumes)
- 🍎 Uses visually colored dots in the menu, just like macOS

## 🖼️ Preview

Right-click on a file → **Color label** (or **Etichetta colore** in Italian)  
You'll see a list of color labels like 🔴 Red, 🟢 Green, 🔵 Blue, etc.  
Clicking a label again removes it.

## 📦 Installation

1. **Install dependencies** (Ubuntu/Debian)

   ```bash
   sudo apt install nautilus-python python3-gi
   ```

2. **Copy the extension to Nautilus' extensions folder**

   ```bash
   mkdir -p ~/.local/share/nautilus-python/extensions/
   cp file_color_tag.py ~/.local/share/nautilus-python/extensions/
   ```

3. **Restart Nautilus**

   ```bash
   nautilus -q
   ```

The emblem icons are auto-generated on first use — no manual setup required.

## 🐧 Requirements

- **Nautilus 43+** with Python extension support (API 4.0 or 4.1)
- **Python 3.x**
- `nautilus-python` (or `python3-nautilus`) and `python3-gi`

### Tested on

| Distribution     | GNOME | Nautilus | API  | Status |
|------------------|-------|---------|------|--------|
| Ubuntu 24.04 LTS | 46    | 46.x    | 4.0  | ✅      |
| Ubuntu 26.04 LTS | 50    | 50.x    | 4.1  | ✅      |

## 🌍 Translations

The extension auto-detects the system language and uses the appropriate translation.  
Currently supported:

| Language | Code |
|----------|------|
| English  | `en` (default) |
| Italian  | `it` |

### Adding a new language

Edit `file_color_tag.py` and add a new entry to the `_TRANSLATIONS` dictionary:

```python
_TRANSLATIONS = {
    "it": { ... },
    "fr": {
        "Color label": "Étiquette couleur",
        "Assign a color label to the selected items": "Attribuer une étiquette couleur aux éléments sélectionnés",
        "Toggle color": "Basculer la couleur",
        "Remove all labels": "Supprimer toutes les étiquettes",
        "Remove all color labels from the selected items": "Supprime toutes les étiquettes couleur des éléments sélectionnés",
        "Icons installed and icon cache updated": "Icônes installées et cache des icônes mis à jour",
        "Red": "Rouge",
        "Orange": "Orange",
        "Yellow": "Jaune",
        "Green": "Vert",
        "Blue": "Bleu",
        "Violet": "Violet",
        "Brown": "Marron",
        "Grey": "Gris",
        "White": "Blanc",
    },
}
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

## 📋 Changelog

### 2.0.0
- Multi-version Nautilus API support (4.0 / 4.1)
- Built-in i18n with Italian translation
- Optimized data structures and code refactoring
- Improved menu labels and tooltips
- Removed unnecessary GTK 3.0 dependency
- Python 3.15+ compatibility (no deprecated API)

### 1.0.0
- Initial release
- Color tagging via emblems
- 9 colors with emoji indicators

## 📖 License

MIT License – use it freely and modify it as you wish.

---

Inspired by macOS Finder's tag system, but made for the Linux desktop.
