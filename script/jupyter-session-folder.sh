#!/bin/bash

execute() {

    path="$1"
    format="ipynb"

    for file in $path
        do
            if ls $file | cut -f 2 | grep -q $format; then
                jupyter nbconvert --inplace --execute $file 
            fi
        done

        # To execute notebooks in parallel
        # wait
}

if [[ $# -ne 0 ]]; then
    execute "$1"
else
    echo 'Usage: jupyter-session-folder.sh {folder}'
fi
