# ~/Documents/manjaro-config/conky-config.txt

set background conky to xbox colors and use theme

1. create new conky config files for background
	```sh
	cd /usr/share/conky/
	cp conky1.10_shortcuts_maia conky1.10_shortcuts_xbox
	cp conky_maia conky_xbox
	cp conky_shortcuts_live_maia conky_shortcuts_live_xbox
	```
	- in each copied file change the value of color2 (to 107c10) and default_color (to 5dc21e)

2. create bash file to start the new created conky config files
	```sh
	cd /usr/bin/
	cp start_conky_maia start_conky_xbox
	```
	- in start_conky_xbox change replace eacht occurrence of maia with xbox

3. tell i3 to start start_conky_xbox instead of start_conky_maia
	- go to ~/.i3/config
	- search for the line 'exec --no-startup-id start_conky_maia' and comment it out
	- add a line below 'exec --no-startup-id start_conky_xbox'


...reboot
