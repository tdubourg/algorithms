<?php

define("MAX", 255); // ASCII TABLE

$values = array();
// for ($i=0; $i < NVALUES; $i++) { 
// 	$values[$i] = mt_rand(0, MAX);
// }

$values = explode(", ", "COW, DOG, SEA, RUG, ROW, MOB, BOX, TAB, BAR, EAR, TAR, DIG, BIG, TEA, NOW, FOX");
define("NVALUES", count($values));

function &csort(&$values, $d) # counting sort, stable sort, $d parameter is the digit number
{
	$c = array();
	for ($i=0; $i <= MAX; $i++) { 
		$c[] = 0;
	}

	$m = count($values);
	for ($i=0; $i < $m; $i++) { 
		$c[ord($values[$i][$d])]++;
	}
	
	for ($i=1; $i <= MAX; $i++) { 
		$c[$i] += $c[$i-1];
	}
	
	$o = array();
	for ($i=$m-1; $i >= 0; $i--) { 
		$o[$c[ord($values[$i][$d])]-1] = $values[$i];
		$c[ord($values[$i][$d])]--;
	}
	
	return $o;
}

function &radix_sort(&$values) {
	$l = strlen($values[0]); // Assuming they all have the same length
	for ($i=$l-1; $i >= 0; $i--) { 
		$values = &csort(&$values, $i);
	}
	return $values;
}

echo "Before:\n";
for ($i=0; $i < NVALUES; $i++) { 
	echo "{$values[$i]}\t";
}

echo "\nAfter one csort (last char):\n";
$o1 =& csort($values, 2);
for ($i=0; $i < NVALUES; $i++) { 
	echo "{$o1[$i]}\t";
}


echo "\nAfter radix-sort:\n";
$o =& radix_sort($values);
for ($i=0; $i < NVALUES; $i++) { 
	echo "{$o[$i]}\t";
}

echo "\n";

?>