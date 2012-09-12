<?php

$values = array();
$DBG = true;

function quick() {
	global $values, $DBG;
	return quick_sort(0, count($values)-1);
}

function quick_sort($p, $r)
{
	global $values, $DBG;
	if ($DBG) {
		echo "quick_sort(".$p.", ".$r.")\n";
	}
	if ($p < $r) {
		$q = partition($p, $r);
		quick_sort($p, $q-1);
		quick_sort($q+1, $r);
	}
}

function partition($p, $r) {
	global $values;
	$x = $values[$r];
	$i = $p-1;
	for ($j=$p; $j < $r; $j++) { 
		if ($values[$j] <= $x) {
			$i++;
			$tmp = $values[$i];
			$values[$i] = $values[$j];
			$values[$j] = $tmp;
		}
	}
	$tmp = $values[$i+1];
	$values[$i+1] = $values[$r];
	$values[$r] = $tmp;
	
	return ($i+1);
}

for ($i=0; $i < 10; $i++) { 
	$values[$i] = mt_rand(-100, 100);
}

echo "Before:\n";
for ($i=0; $i < count($values); $i++) { 
	echo "{$values[$i]}\t";
}

echo "\nAfter:\n";
quick();
for ($i=0; $i < count($values); $i++) { 
	echo "{$values[$i]}\t";
}

echo "\n";

?>