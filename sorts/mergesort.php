#!/usr/bin/php
<?php
###
# Author: TD
# License: GPLv3
####

$DBG = false;

function msort($arr) # Note : Sorting in ascending order
{
	global $DBG;
	$l = count($arr);
	if ($DBG) {
		echo "Working on an array of length={$l}\n";
	}
	if ($l == 1) {

		return $arr;
	}

	$middle = floor($l/2);
	$left = array_slice($arr, 0, $middle);
	$right = array_slice($arr, $middle, $l-$middle);

	if ($DBG) {
		echo "Left slice:\n";
		printarr($left);

		echo "Right slice:\n";
		printarr($right);
	}

	$left = msort($left);
	$right = msort($right);

	return merge($left, $right);
}

function merge($l, $r)
{
	global $DBG;

	if ($DBG) {
		echo "Currently merging arrays: \n";
		printarr($l);
		printarr($r);
	}
	$pl = 0;
	$pr = 0;
	$ll = count($l);
	$lr = count($r);
	$o = array();
	while (true) {
		if ($pl < $ll && $pr < $lr) {
			if ($l[$pl] > $r[$pr]) {
				$o[] = $r[$pr++];
			} else {
				$o[] = $l[$pl++];
			}
		} else if ($pr < $lr) {
			for (; $pr < $lr; $pr++) { 
				$o[] = $r[$pr];
			}
			break; # The end
		} else if($pl < $ll) {
			for (; $pl < $ll; $pl++) { 
				$o[] = $l[$pl];
			}
			break; # The end
		}
	}
	return $o;
}

define("MAX", 100);
define("NVALUES", 10);

$values = array();
for ($i=0; $i < NVALUES; $i++) { 
	$values[$i] = mt_rand(0, MAX);
}

function printarr(&$o)
{
	$max = count($o);
	for ($i=0; $i < $max; $i++) { 
		echo "{$o[$i]}\t";
	}
	echo "\n";
}

echo "Before:\n";
printarr(&$values);

echo "\nAfter:\n";
$o = msort($values);
printarr($o);

echo "\n";


?>