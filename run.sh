#!/bin/bash

# Set the input and output directories
INPUT_DIR=/data/pdf-input
OUTPUT_DIR=/data/pdf-output

# Map the directories to the paths inside the container
mkdir -p $INPUT_DIR
mkdir -p $OUTPUT_DIR

# Check if the first argument is provided (maximum files to process)
if [ -z "$1" ]; then
    # If no argument is provided, default to 100 files
    MAX_FILES=100
else
    MAX_FILES=$1
fi

# Run the Python app with the argument for the number of files to process
python app.py $MAX_FILES
