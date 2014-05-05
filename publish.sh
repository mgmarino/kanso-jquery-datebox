#!/bin/bash
MODULENAME=jquery-mobile-datebox
CWD=`pwd`
PUBLISHDIR=${CWD}/publish
mkdir ${PUBLISHDIR} 
mkdir ${PUBLISHDIR}/css 
cp README.md kanso.json ${MODULENAME}.js ${PUBLISHDIR} 
cp ${MODULENAME}.css ${PUBLISHDIR}/css
cp -R image ${PUBLISHDIR}/css/
cd ${PUBLISHDIR}
kanso publish
cd ${CWD} 
rm -rf ${PUBLISHDIR} 

