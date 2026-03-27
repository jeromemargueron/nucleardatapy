#!/bin/bash
for filename in 2024-*/*.dat; do
    echo $filename
    sed 's/D/E/g' $filename > $filename'_new'
    mv $filename'_new' $filename
done
