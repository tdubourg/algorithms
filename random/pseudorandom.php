#!/usr/bin/php
<?php
###
# Author: TD
# License: GPLv3
####

function myrand($max=1000000) {
	static $R = 0;
	static $a = 3;
	static $c = 7;
	
	$Rn = ($a * $R + $c) % $max;
	$R = $Rn;
	return $Rn;
}

for ($i=0; $i < 50; $i++) { 
	echo myrand()."\n";
}

?>