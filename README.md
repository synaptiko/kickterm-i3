What it is?
===========
- Replacement for heavy-weight drop-down terminals like Guake/Terminator
- Simple python script which uses 
..* `gnome-terminal` to set it own app id and class
..* `i3wm` to autostart and workspace and key binding assignment

What it isn't?
===============
- Full replacement of drop-down terminals
- Ambitious project

Why I did it?
=============
See the same section of my [previous kickterm project](https://github.com/synaptiko/kickterm)

Dependencies:
=============
- `i3wm`
- `python3`
- `gnome-terminal` or [`gnome-terminal-transparency`](https://aur.archlinux.org/packages/gnome-terminal-transparency)

How to use it?
==============
To fully enjoy it add the following into your i3 config file (e.g. `~/.config/i3/config`):
```
assign [class="Kickterm"] _
exec --no-startup-id /home/xy/SomeStuff/kickterm-i3/run.py

bindsym $mod+slash workspace _
workspace_auto_back_and_forth yes
```
