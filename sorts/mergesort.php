// <?php

// $values = array();
// $DBG = true;

// function msort(&$values, $p, $q)
// {
// 	if ($q <= $p) {
// 		return $values;
// 	}
// 	if ($q-$p == 1) {
// 		if ($values[$p] > $values[$q]) {
// 			$tmp = $values[$p];
// 			$values[$p] = $values[$q];
// 			$values[$q] = $tmp;
// 		}
// 	} else {
// 		$middle = $p+floor(($p-$q)/2);
// 		$a = msort(&$values, $p, $middle);
// 		$b = msort(&$values, $middle+1, $q);
// 	}
// }

// ?>