#!/usr/bin/php
<?php
###
# Author: TD
# License: GPLv3
####

// Algorithm: 
// L ← Empty list that will contain the sorted elements
// S ← Set of all nodes with no incoming edges
// while S is non-empty do
//     remove a node n from S
//     insert n i$from L
//     for each node m with an edge e from n$from m do
//         remove edge e from the graph
//         if m has no other incoming edges then
//             insert m into S
// if graph has edges then
//     return error (graph has at least one cycle)
// else 
//     return L (a topologically sorted order)

error_reporting(E_ALL &~ E_NOTICE & ~E_WARNING);

// Edges are represented in $to as $to[end][start]
// Then to check there is no incoming edge we just have to check $to[node] is empty

$to = array();
$from = array();

function build($str)
{
	global $to, $from, $nodes;
	$lines = explode("\n", $str);
	foreach ($lines as $line) {
		if(!empty($line)) {
			list($n1, $dir, $n2) = explode(",", $line);
			$n1 = intval($n1);
			$n2 = intval($n2);
			echo "{$n1}, {$dir}, {$n2}\n";
			if ($dir == 'l') {
                $from[$n2][$n1] = true;
                $to[$n1][$n2] = true;
            } else if ($dir == 'r') {
                $from[$n1][$n2] = true;
                $to[$n2][$n1] = true;
            }
			
			$nodes[$n1] = true;
			$nodes[$n2] = true;
		}
	}
	return ;
}

function topo_sort()
{
	global $to, $from, $nodes;
	$start = array();
    // Populating the $start list of nodes without incoming edge
	foreach($nodes as $k => $unused) {
		$v = $from[$k];
		if(empty($v)) { # if no incoming edge to this node
            $start[] = $k;
        }
    }
    
    echo "\nContent of the \$start array: \n";
    var_dump($start);
    
    // Topological sort
    $L = array();
    while(!empty($start)) { # As long as we have a node with no incoming edge
    	$ready = false;
    	$a = array_shift($start);
    	echo "Examining relations of {$a}\n";
    	$L[] = $a;
    	foreach($to[$a] as $v => $unused) {
    		echo "\tLeft relation with {$v}\n";
            unset($from[$v][$a]); // deleting the current edge
            
            if(empty($from[$v])) {
            	$start[] = $v;
            } else {
            	echo "After deleting the edge, from Left relations of {$v} are:\n";
            	var_dump($from[$v]);
            }
        }
    }
    return $L;
}

build(file_get_contents("php://stdin"));

echo "\nContent of the \$from array: \n";
var_dump($from);
echo "\nContent of the \$to array: \n";
var_dump($to);
echo "\nContent of the \$nodes array: \n";
var_dump($nodes);


$l = topo_sort();

echo "Result: \n";
foreach ($l as $value) {
	echo "\t{$value}";
}

echo "\n";

?>