#!/bin/bash

PATH_TO_CKJM=$1
#finds all class files in the class folder
find class -name '*.class' -print | java -jar $PATH_TO_CKJM/ckjm-\${version}.jar > result.txt
