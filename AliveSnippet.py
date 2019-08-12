import sublime
import sublime_plugin

import sys
import os.path

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

is_python3 = sys.version_info[0] > 2

def init():
  "Init Alive Snippet plugin"
  globals()['settings'] = sublime.load_settings('AliveSnippet.sublime-settings')
  snippets = settings.get('snippets');
  for r, d, f in os.walk(BASE_PATH+'/alive_snippets/'):
    for file in f:
      newFile = file.replace(".sublime-snippet__", ".sublime-snippet")
      os.rename(BASE_PATH+'/alive_snippets/'+file, BASE_PATH+'/alive_snippets/'+newFile) ;
  for k,v in snippets.items():
    if not v:
      fileSnippet = BASE_PATH+'/alive_snippets/'+k+'.sublime-snippet';
      newFile = fileSnippet.replace(".sublime-snippet", ".sublime-snippet__")
      os.rename(fileSnippet, newFile) ;

def plugin_loaded():
  sublime.set_timeout(init, 200)

##################
# Init plugin
if not is_python3:
  init()