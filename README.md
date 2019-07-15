Alive Web Vietnam Company Snippets for Sublime Text
================================================

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
|Snippet|Output|
|-------|------|
| `picsource` | `<picture><source srcset="${2}" media="(max-width: 767px)"><source srcset="${1}"><img src="${1}" alt="${3}"></picture>` |


### SCSS/CSS Snippets
|Snippet|Output|
|-------|------|
| `minscreen` | `@include min-screen(${1:768}px) {${2}}` |
| `mscreen` | `@include max-screen(${1:767}px) {${2}}` |


### JS Snippets
|Snippet|Output|
|-------|------|
| `csl` | `console.log(${1});` |
| `rf` | `return false;` |


### PHP Snippets

|Snippet|Output|
|-------|------|
| `showerrors` | `ini_set('display_errors', 1); ini_set('display_startup_errors', 1); error_reporting(E_ALL); ?>` |
| `prepr` | `echo '<pre>'; print_r($1); echo '</pre>'; ?>` |