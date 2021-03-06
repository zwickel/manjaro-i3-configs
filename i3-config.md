# do this in i3 config file: ~/.i3/config
manjaro alias to open it with nano is 'con' in terminal

change window title font:

```
# Font for window titles. Will also be used by the bar unless a different font
# is used in the bar {} block below.
font Consolas-8:xft:URWGothic-Book 11
```

change workspace icons with font awesome:
add font awesome to i3bar:
```
bar {
	...
	font pango:DejaVu Sans Mono, Awesome 8
	...
}
```

- to change the icons take a look at the font awesome cheatsheet at http://fontawesome.io/cheatsheet/
- then set the icons as the following example shows for the first workspace, which is set to the fa-terminal icon
	for completeness I will place here the config for all workspaces
- also the 9th workspace is created in this part ;-)
```
# Workspace names
...
# fa-terminal
set $ws1 "1:&#xf120;"
# fa-globe
set $ws2 "2:&#xf0ac;"
# fa-folder-o
set $ws3 "3:&#xf114;"
# fa-code
set $ws4 "4:&#xf121;"
# fa-file-text-o
set $ws5 "5:&#xf0f6;"
# fa-question-circle
set $ws6 "6:&#xf059;"
set $ws7 "7:&#xf059;"
# fa-music
set $ws8 "8:&#xf025;"
# fa-comments-o
set $ws9 "9:&#xf0e6;"
...

# switch to workspace
...
bindsym $mod+9 workspace $ws9

# Move focused container to workspace
...
bindsym $mod+Ctrl+9 move container to workspace $ws9

# Move to workspace with focused container
...
bindysm $mod+Shift+9 move container to workspace; workspace $ws9
```

#### change background coclor of selected workspace

`set $i3_color4		#107c10		# #16a085`

#### open applications on specific workspace

```
# Open applications on specific workspace
assign [class="Opera"] $ws2
assign [class="Thunderbird"] $ws2
assign [class="Pcmanfm"] $ws3
assign [class="ranger"] $ws3 -- not working with either 'r' or 'R' :-(/)
assign [class="Code"] $ws4
assign [class="okular"] $ws5
assign [class="mocp"] $ws8
assign [class="whatsapp"] $ws9
assign [class="Telegram"] $ws9
```

#### change binding for lockscreen

```
# Lock screen
bindsym $mod+Escape exec --no-startup-id blurlock
```

#### use conky with xbox-color

```
# Autostart applications
...
exec --no-startup-id start_conky_xbox
...
```

#### Set the colors for the borders of the container...

```
# Theme colors
# class				border  backgr. text    indic.   child_border
  client.focused		#556064 #556064 #5dc21e #FDF6E3
  client.focused_inactive	#2F3D44 #2F3D44 #107c10 #454948
  client.unfocused		#2F3D44 #2F3D44 #107c10 #454948
  client.urgent			#CB4B16 #FDF6E3 #107c10 #268BD2
  client.placeholder		#000000 #0c0c0c #ffffff #000000

  client.background		#2B2C2B
```


#### Setting the gaps a bit smaller

```
#############################
### settings for i3-gaps: ###
#############################

# Set inner/outer gaps
gaps inner 5
gaps outer -2
```

