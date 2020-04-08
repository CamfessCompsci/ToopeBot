#!/bin/bash
FILES=./ansi/*
for f in $FILES
do
	 iconv -f "windows-1252" -t "UTF-8" $f | sponge $f
done
