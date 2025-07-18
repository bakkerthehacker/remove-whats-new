#!/usr/bin/env python

# Patch steam css files while keeping the length the same to prevent changes being overridden

import glob
import re

classes_to_replace = [
  b'libraryhome_UpdatesContainer_.....',
  b'gamepadhomewhatsnew_LibraryHomeWhatsNew_.....',

  # these start with the last few chars from the previous css classes
  b'._17uEBe5Ri8TMsnfELvs8-N',
  b'.rvYRfhjWoi57GShuRcAwP',
]
css_path_globs = [
  # Linux
  '/home/*/.steam/steam/steamui/css/chunk*.css',
  # MacOS
  '/Users/*/Library/Application Support/Steam/steamui/css/chunk*.css',
  # Windows
  r'C:\Program Files (x86)\Steam\steamui\css\chunk*.css',
]
new_style = b'display: none !important;'


def replace_style(match):
  print()
  print(b'found class: ' + match['class_name'])
  print('with style:')
  print(match['class_style'])

  padding_length = len(match['class_style']) - len(new_style)

  if padding_length < 0:
    raise Exception('cannot replace existing style with longer style')

  print('replacing with style:')
  print(new_style)

  return match['class_name'] + b'{' + new_style + (b' ' * padding_length) + b'}'


def main():
  css_globs = [
    css_glob
    for css_path_glob in css_path_globs
    for css_glob in glob.glob(css_path_glob)
  ]

  if len(css_globs) == 0:
    raise Exception('did not find any css file')

  if len(css_globs) > 5:
    raise Exception('found too many css files:\n' + '\n'.join(css_globs))

  for found_css in css_globs:
    print()
    print('found css file ' + found_css)

    read_file = open(found_css, 'rb')
    css_string = read_file.read()
    read_file.close()

    for class_name in classes_to_replace:
      print()
      print(b'looking for ' + class_name)

      css_string = re.sub(
        b'(?P<class_name>' + class_name + b')' + br'\{(?P<class_style>[^}]*?)\}',
        replace_style,
        css_string,
        count=1,
      )

    write_file = open(found_css, 'wb')
    write_file.write(css_string)
    write_file.close()


if __name__ == '__main__':
  main()
