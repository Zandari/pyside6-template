#!/bin/bash

FILES="src/widgets/forms/*.qrc"
echo "Converting..."
for f in $FILES
do
  echo $(basename -- $f)
  # pyside6-rcc $f -o ${f::(-4)}_rc.py
  base=$(basename -- $f)
  pyside6-rcc $f -o src/${base::(-4)}_rc.py
done
echo "Done"
