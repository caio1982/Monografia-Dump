#!/bin/bash

sed '/@\(.*\){\(.*\),/!d;s//\2/' monografia.bib | while read c; do grep -q ${c} monografia.aux || echo cite ${c}; done

exit 0
