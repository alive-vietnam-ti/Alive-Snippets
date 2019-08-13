```
   _____  .__  .__                 _________      .__                      __          
  /  _  \ |  | |__|__  __ ____    /   _____/ ____ |__|_____ ______   _____/  |_  ______
 /  /_\  \|  | |  \  \/ // __ \   \_____  \ /    \|  \____ \\____ \_/ __ \   __\/  ___/
/    |    \  |_|  |\   /\  ___/   /        \   |  \  |  |_> >  |_> >  ___/|  |  \___ \ 
\____|__  /____/__| \_/  \___  > /_______  /___|  /__|   __/|   __/ \___  >__| /____  >
        \/                   \/          \/     \/   |__|   |__|        \/          \/ 
```

Alive Web Vietnam Company Snippets and Keymaps for Sublime Text v1.0.8
====================================================================

This is a collection of Sublime Text snippets and Keymaps for the [Alive Web Vietnam Company](https://alive-web.vn/)
Feel free to Fork the snippet repo and submit a
pull request: https://github.com/alivevietnam/alive-sublime-snippets

## Change logs:

### 1.0.8:

- Add more 8 snippets for template mixins scss
- Add settings features, you can disable snippets what you don't need
- Add menu commands settings
- Add main menu settings

## Installation

### Recommended

Install this package with [Package Control](https://sublime.wbond.net/):
1. Install Package Control in Sublime.
2. Press `Cmd` + `Shift` + `P` (OSX) or `Ctrl` + `Shift` + `P` (Windows/Linux)
3. Select Install Package
4. Search 'Alive Sublime Snippets'

### Manual

Copy this folder to the `Packages` folder of your Sublime Text installation.

Mac users: Library/Application Support/Sublime Text/Packages

## Snippets

### HTML Snippets
|STT|Snippet|Output|
|-------|-------|------|
| `01` | `picsource` | `<picture><source srcset="${2}" media="(max-width: 767px)"><source srcset="${1}"><img src="${1}" alt="${3}"></picture>` |
| `02` | `initowlcarousel` | `Insert full install owlcarousel library into html/php file` |
| `03` | `wppagenavi` | `Insert full layout html of wp-pagenavi into html/php file` |


### SCSS/CSS Snippets
|STT|Snippet|Output|
|-------|-------|------|
| `04` | `minscreen` | `@include min-screen(${1:768}px) {${2}}` |
| `05` | `maxscreen` | `@include max-screen(${1:767}px) {${2}}` |
| `06` | `iar` | `@include aspect-ratio(${1:width}, ${2:height});` |
| `07` | `iborderradius` | `@include border-radius(${1:radius}, ${2:''});` |
| `08` | `iclearfix` | `@include clearfix();` |
| `09` | `ifz` | `@include font-size(${1:14});` |
| `10` | `imultilineellipsis` | `@include multiLineEllipsis(${1:linecount});` |
| `11` | `ipc` | `@include PC {${1}}` |
| `12` | `isp` | `@include SP {${1}}` |
| `13` | `itransform` | `@include transform_c(${1:content});` |
| `14` | `itransition` | `@include transition_c(${1:content}, ${2:''});` |


### JS Snippets
|STT|Snippet|Output|
|-------|-------|------|
| `15` | `csl` | `console.log(${1});` |
| `16` | `rf` | `return false;` |
| `17` | `owlcarousel` | `$(".js-carousel")` |
| `18` | `matchheight` | `$(".js-matchHeight").matchHeight();` |
| `19` | `smoothscroll` | `$(".js-smoothscroll").smoothscroll();` |


### PHP Snippets
|STT|Snippet|Output|
|-------|-------|------|
| `20` | `showerrors` | `ini_set('display_errors', 1); ini_set('display_startup_errors', 1); error_reporting(E_ALL); ?>` |
| `21` | `performance` | `Insert code to measure website (php) performance` |
| `22` | `prepr` | `echo '<pre>'; print_r($1); echo '</pre>'; ?>` |
| `23` | `hidprint` | `echo '<!-- alive print '; print_r($1); echo ' -->';` |
| `24` | `catchthatimage` | `catch_that_image($noimg = true);` |
| `25` | `getfirstimage` | `get_first_image($content, $noimg = true);` |
| `26` | `currentpageurl` | `curPageURL();` |
| `27` | `cutstring` | `cutString($str, $len, $moreStr = "...");` |
| `28` | `getarrurl` | `getArrUrl($_GET['args']);` |
| `29` | `getcurl` | `get_curl($url);` |
| `30` | `thumbcrop` | `thumbCrop($img, $w, $h, $zc=1, $a=false, $cc=false);` |
| `31` | `uaclass` | `Insert ua.class code` |
| `32` | `wpposttypearchive` | `wp_post_type_archive($post_type, $home_url="", $havecount=false);` |

## Keymaps

|STT|Keymap|Function|
|-------|-------|------|
| `01` | `super+shift+enter` | `<br>` |
| `02` | `super+b` | `<strong>${0:$SELECTION}</strong>` |
| `03` | `ctrl+super+b` | `changing build shortcut` |
| `04` | `command+shift+down` | `goto definition` |
| `05` | `command+shift+r` | `reveal in side bar` |
| `06` | `super+shift+c` | `toggle side bar` |
| `07` | `super+shift+x` | `toggle minimap` |

--------------------------

Enjoy and have a great day!

techteam[at]alive-vietnam
