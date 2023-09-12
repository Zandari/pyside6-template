#!/bin/bash

FILES="src/widgets/forms/*.ui"
echo "Converting..."
for f in $FILES
do
  pyside6-uic $f -o ${f::(-3)}_form.py
done
echo "Done"
