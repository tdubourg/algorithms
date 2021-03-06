#!/usr/bin/php
<?php
###
# Author: TD
# License: GPLv3
####

define("MAX", 1000);
define("NVALUES", 100);

$values = array();
for ($i=0; $i < NVALUES; $i++) { 
	$values[$i] = mt_rand(0, MAX);
}

function &csort(&$values)
{
	$c = array();
	for ($i=0; $i <= MAX; $i++) { 
		$c[] = 0;
	}

	$m = count($values);
	for ($i=0; $i < $m; $i++) { 
		$c[$values[$i]]++;
	}
	
	for ($i=1; $i <= MAX; $i++) { 
		$c[$i] += $c[$i-1];
	}
	
	$o = array();
	for ($i=$m-1; $i >= 0; $i--) { 
		$position = $c[$values[$i]]-1; # position starting at 0
		// If you want to sort in reverse order, use the following line instead: 
		// $position = $m-1-($c[$values[$i]]-1);
		$o[$position] = $values[$i];
		$c[$values[$i]]--;
	}
	
	return $o;
}

echo "Before:\n";
for ($i=0; $i < NVALUES; $i++) { 
	echo "{$values[$i]}\t";
}

echo "\nAfter:\n";
$o =& csort($values);
for ($i=0; $i < NVALUES; $i++) { 
	echo "{$o[$i]}\t";
}

echo "\n";

?>