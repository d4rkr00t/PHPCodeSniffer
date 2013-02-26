# PHPCodeSniffer
Inspect php file with PHPCodeSniffer and show results.

Example:

    --------------------------------------------------------------------------------
    FOUND 9 ERROR(S) AFFECTING 4 LINE(S)
    --------------------------------------------------------------------------------
      1 | ERROR | Missing file doc comment
      5 | ERROR | Missing @category tag in class comment
      5 | ERROR | Missing @package tag in class comment
      5 | ERROR | Missing @author tag in class comment
      5 | ERROR | Missing @license tag in class comment
      5 | ERROR | Missing @link tag in class comment
      9 | ERROR | Missing function doc comment
      9 | ERROR | Constants must be uppercase; expected ARGUMENT but found argument
     11 | ERROR | Perl-style comments are not allowed. Use "// Comment." or "/*
        |       | comment */" instead.
    --------------------------------------------------------------------------------

## Installation
Note with either method, you may need to restart Sublime Text 2 for the plugin to load.

You must install PHPCodeSniffer!

### Package Control
 TODO: Add to Package Control

### Manual
Clone git repo to Sublime packages dir.

    git clone git://github.com/d4rkr00t/PHPCodeSniffer.git PHPCodeSniffer

After installing plugin, configure path to phpcs executable file:

    {
        "phpcs":{
            "osx": "phpcs",
            "windows": "phpcs",
            "linux": "phpcs"
        }
    }

## Usage
In php file press cmd+p and find "PHPCodeSniffer - Inspect File" command.