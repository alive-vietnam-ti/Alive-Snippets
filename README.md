```
   _____               .____    .__                 _________      .__                      __          
  /  _  \      .__     |    |   |__|__  __ ____    /   _____/ ____ |__|_____ ______   _____/  |_  ______
 /  /_\  \   __|  |___ |    |   |  \  \/ // __ \   \_____  \ /    \|  \____ \\____ \_/ __ \   __\/  ___/
/    |    \ /__    __/ |    |___|  |\   /\  ___/   /        \   |  \  |  |_> >  |_> >  ___/|  |  \___ \ 
\____|__  /    |__|    |_______ \__| \_/  \___  > /_______  /___|  /__|   __/|   __/ \___  >__| /____  >
        \/                     \/             \/          \/     \/   |__|   |__|        \/          \/ 
```

Alive Web Vietnam Company Snippets for Sublime Text
====================================================================

This is a collection of Sublime Text snippets for the [Alive Web Vietnam Company](https://alive-web.vn/)

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


### SCSS/CSS Snippets
|STT|Snippet|Output|
|-------|-------|------|
| `03` | `minscreen` | `@include min-screen(${1:768}px) {${2}}` |
| `04` | `maxscreen` | `@include max-screen(${1:767}px) {${2}}` |


### JS Snippets
|STT|Snippet|Output|
|-------|-------|------|
| `05` | `csl` | `console.log(${1});` |
| `06` | `rf` | `return false;` |
| `07` | `owlcarousel` | `$(".js-carousel")` |
| `08` | `matchheight` | `$(".js-matchHeight").matchHeight();` |
| `09` | `smoothscroll` | `$(".js-smoothscroll").smoothscroll();` |


### PHP Snippets
|STT|Snippet|Output|
|-------|-------|------|
| `10` | `showerrors` | `ini_set('display_errors', 1); ini_set('display_startup_errors', 1); error_reporting(E_ALL); ?>` |
| `11` | `performance` | `Insert code to measure website (php) performance` |
| `12` | `prepr` | `echo '<pre>'; print_r($1); echo '</pre>'; ?>` |
| `13` | `hidprint` | `echo '<!-- alive print '; print_r($1); echo ' -->';` |
| `14` | `catchthatimage` | `catch_that_image($noimg = true);` |
| `15` | `getfirstimage` | `get_first_image($content, $noimg = true);` |
| `16` | `currentpageurl` | `curPageURL();` |
| `17` | `cutstring` | `cutString($str, $len, $moreStr = "...");` |
| `18` | `getarrurl` | `getArrUrl($_GET['args']);` |
| `19` | `getcurl` | `get_curl($url);` |
| `20` | `thumbcrop` | `thumbCrop($img, $w, $h, $zc=1, $a=false, $cc=false);` |
| `21` | `uaclass` | `Insert ua.class code` |
| `22` | `wpposttypearchive` | `wp_post_type_archive($post_type, $home_url="", $havecount=false);` |

--------------------------

Enjoy and have a great day!
techteam[at]alive-vietnam