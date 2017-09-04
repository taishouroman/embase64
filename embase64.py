# -*- encoding: utf-8 -*-

"""Embed images into a svg file with base64
"""

import base64;
import imghdr;
import os;
import xml.etree.ElementTree;


def __encode_img2base64(imgdata):
	"""Encode image data with base64

	Args:
		imgdata (bytes, str): Byte stream of an image file

	Returns:
		(str): Base64 string
	"""
	b64 = base64.b64encode(imgdata);
	return b64.decode('ascii');


def __get_imgdata(filepath):
	"""Load a image file and return byte stream

	Args:
		filepath (str): Image file path to be loaded

	Returns:
		(bytes, str): Byte stream of the image file
	"""
	fs = open(filepath, 'rb');
	buf = fs.read();
	fs.close();
	return buf;


def __get_imgpath(svgfilepath, imgfilepath):
	"""Return a image path

	Args:
		svgfilepath (str): svg file path
		imgfilepath (str): Image file path

	Returns:
		(str): Normalized image file path
	"""
	svgdir = os.path.dirname(os.path.abspath(svgfilepath));
	fp = svgdir + '/' + imgfilepath;
	return os.path.abspath(fp);


def __get_URI_head(imgdata):
	"""Return URI header string

	Args:
		imgdata (bytes, str): Byte stream of an image file

	Returns:
		(str): Header string of data URI scheme
	"""
	fmt = imghdr.what('', imgdata);
	return 'data:image/' + fmt + ';base64,';


def embed(filepath):
	"""Embed image files into the svg file with base64

	Args:
		filepath (str): svg file path

	Returns:
		(ElementTree): xml structure of the svg file which images are embedded
	"""
	if not isinstance(filepath, str):
		raise TypeError('\'filepath\' must be str; passed {0}'.format(type(filepath)));

	tree = xml.etree.ElementTree.parse(filepath);
	replace(filepath, tree.getroot());
	return tree;


def replace(svgfilepath, node):
	"""Replace image files with base64 recursively

	Args:
		svgfilepath (str):     svg file path
		node        (Element): xml element node

	Returns:
		Nothing
	"""
	if not isinstance(svgfilepath, str):
		raise TypeError('\'svgfilepath\' must be str; passed {0}'.format(type(filepath)));
	if not isinstance(node, xml.etree.ElementTree.Element):
		raise TypeError('\'node\' must be xml.etree.ElementTree.Element; passed {0}'.format(type(filepath)));

	if 1 <= len(node):
		for n in node:
			replace(svgfilepath, n);

	if 'image' in node.tag:
		for (k, v) in node.attrib.items():
			if 'href' in k:
				buf = __get_imgdata(__get_imgpath(svgfilepath, v));
				uri_head = __get_URI_head(buf);
				uri_data = __encode_img2base64(buf);
				node.attrib[k] = uri_head + uri_data;
