# Style Check
a Sublime Text 3 Package to check English writing style

## Description
This tool help you check grammar and style when writing scientific/professional articles. 

[style-check.rb](http://www.cs.umd.edu/~nspring/software/style-check-readme.html) is a great command line tool for such purpose. However, it is more convenient to integrate it into my favorite text editor. This package is a wrapper around the ruleset used in style-check.rb.

## Installation
* Download and unpack into your sublime text 3 packages folder, or
* Git clone into your sublime text 3 packages folder
 ```git clone https://github.com/chrishan/style-check.git```

## How to Use
1. Open console with ctrl + `
1. Select some text in the editor or put cursor under a word to check
1. Run the style_correct command
  * via hotkey ctrl+alt+g
  * via right-click context menu > Google Spell Check
  * via Command Pallet, ctrl+shift+p (command+shift+p in OSX) > Style Check
1. Browse the console for the style suggestions


## TODO
- [ ] More easy-to-use [interface](https://github.com/bradrobertson/sublime-packages/blob/master/Default/mark.py)
- [ ] Learn from other packages ([this](https://github.com/vaisaghvt/CheckTypos))
- [ ] Rules from posts by other professional writters
- [ ] Rules from [English Language & Usage Stack Exchange](http://english.stackexchange.com/)



## Finally
* I learned how to create this package by studying another Sublime text package - [google-spell-check](https://github.com/noahcoad/google-spell-check/)