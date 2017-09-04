# Embed images into a svg file with base64 #
This process embeds images into a svg file with base64 encoding.

## Preparation ##
1. Put this directory under a Python module search path.
2. Copy or move 'embase64' to a directory which is set PATH.

## Usage ##
From a terminal, run eigher of following commands:
```sh
$ python embase64 [OPTIONS]... FILE...
$ embase64 [OPTIONS]... FILE...
```

From Python interpreter or Python module, use like following:
```python
>>> import embase64;
>>> import xml.etree.ElementTree;
>>> tree = embase64.embed('/path/to/file.svg');
```

## Command line options ##
<pre>
usage: embase64 [OPTION]... FILE...

Embed images with base64

positional arguments:
  FILE         Input files path

optional arguments:
  -h, --help   show this help message and exit
  --overwrite  Overwrite original files

If a FILE is '-', or there is no FILE and stdin is not a tty, read standard input.
</pre>