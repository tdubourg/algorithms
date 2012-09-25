#!/usr/bin/php
<?php

define("MAX", 100);
define("NVALUES", 10);
define("DBG", false);

$values = array();
for ($i=0; $i < NVALUES; $i++) { 
	$values[$i] = mt_rand(0, MAX);
}

function printarr(&$o)
{
	for ($i=0; $i < NVALUES; $i++) { 
		echo "{$o[$i]}\t";
	}
	echo "\n";
}

function &insertsort(&$values)
{
	for ($i=1; $i < NVALUES; $i++) {

		$curr = $values[$i];
		if (DBG === true) {
			printarr(&$values);
			echo "curr={$curr}\n";
		}
		for ($k=$i-1; $k >= 0 && $values[$k] > $curr; $k--) { 
			$values[$k+1] = $values[$k];
		}
		if (DBG === true) {
			echo "k={$k}, curr={$curr}\n";
		}
		$values[$k+1] = $curr;
		// for ($k=$i; $k > 0 && $values[$k] < $values[$k-1]; $k--) { 
		// 	$tmp = $values[$k];
		// 	$values[$k] = $values[$k-1];
		// 	$values[$k-1] = $tmp;
		// }
	}
	return $values;
}

echo "Before:\n";
for ($i=0; $i < NVALUES; $i++) { 
	echo "{$values[$i]}\t";
}

echo "\nAfter:\n";
$o =& insertsort($values);
printarr(&$o);

echo "\n";


?>