#!/bin/bash

function usage
{
	echo "Usage:"
	echo $0 "<ORIGINAL FILE> <SAVE DIR>"
	echo ""
}

DS=`date +%Y.%m.%d-%H.%M`
echo "TIMESTAMP:" $DS

if [ "$1" == "" ] ; then
	echo "P1 est vide"
	usage
else
	echo "P1 est présent"

	if [ -e "$1" ] ; then
		echo "P1 existe"
		FS=`readlink -f $1`
		echo $FS
		BS1=${FS//\//-}
		echo $BS1
		BS2=${BS1/-/}.bck-$DS
		echo $BS2

		if [ "$2" == "" ] ; then
        		echo "P2 est vide"
		else
        		echo "P2 est présent"

			if [ -d "$2" ] ; then
                		echo "P2 existe"
				echo cp $1 $2/$BS2
				cp $1 $2/$BS2
			else
				echo "P2 n'existe pas"
			fi
		fi
	else
		echo "P1 n'existe pas"
	fi
fi
