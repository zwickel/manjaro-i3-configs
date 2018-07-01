# ~/Documents/manjaro-config/dmenu-config.txt
here the color for selected dmenu-items is changed to xbox green

make changes in ~/.dmenurc:

```
## define the font for dmenu to be used
DMENU_FN="Consolas-8"

## background color for unselected menu-items
DMENU_NB="#2B2C2B"

## textcolor for unselected menu-items
DMENU_NF="#F9FAF9"

## background color for selected menu-items
DMENU_SB="#10c710"		# 16A085

## textcolor for selected menu-items
DMENU_SF="#F9FAF9"

## command for the terminal application to be used:
TERMINAL_CMD="terminal -e"

## export our variables
DMENU_OPTIONS="-fn $DMENU_FN -nb $DMENU_NB -nf $DMENU_NF -sf DMENU_SF -sb DMENU_SB"
```