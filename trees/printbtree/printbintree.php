<?php

require_once "colorcli.class.php";

define('H', 5);
define('FUCK', mt_rand(0, 100)); # This constant is called FUCK because FUCK the fact you cannot assign the return of a function to a local static variable (making local static variable pretty stupidely useless or forcing us to do thing kind of trick instead...FUCK)

/**
* 
*/
class Node
{
	function __construct($val, $depth)
	{
		$this->val = $val;
		$this->l = null;
		$this->r = null;
		$this->d = $depth;
	}
}

function printtree(&$node, $hmax) # BFS
{
	$q = array($node);
	do {
		$a = array_shift($q); # pop_front()
		disp($a, $hmax);
		if ($a->l) {
			$q[] = $a->l; # push
		}
		
		if ($a->r) {
			$q[] = $a->r; # push
		}
	} while(!empty($q));
}

function colorMyString($str, $level)
{
	$colors = ColorCLI::getForegroundColors();
	$color = $colors[($level + FUCK) % count(ColorCLI::$foreground_colors)];
	if ($color == 'black') {
		$color = $colors[($level + 2 * FUCK) % count(ColorCLI::$foreground_colors)];
	}
	
	return ColorCLI::getColoredString($str, $color);
}

function disp($node, $hmax)
{
	static $prev_depth = -1;
	$out='';

	$m = (pow(2, $hmax-$node->d + 1));
	
	if ($prev_depth != $node->d) {  # depth changed, so new line required + leading spaces (that are half as many as the spaces between the nodes themselves)
		$out .= "\n({$node->d})";
		for ($i=0; $i < $m/2; $i++) { 
			$out .= "\t";
		}
		$prev_depth = $node->d;
	} else {
		for ($i=0; $i < $m; $i++) { 
			$out .= "\t";
		}
	}

	$out .= $node->val;
	
	echo colorMyString($out, $node->d);
	
	// Another way which works as well:
	// $m = (pow(2, $hmax-$node->d));
	
	// if ($prev_depth != $node->d) {
	// 	echo "\n({$node->d})";
	// 	$prev_depth = $node->d;
	// }
	
	// for ($i=0; $i < $m; $i++) { 
	// 	echo "\t";
	// }
	
	// echo $node->val;
	
	// for ($i=0; $i < $m; $i++) { 
	// 	echo "\t";
	// }
}

function &build_tree(&$parent)
{
	if ($parent->d >= H) {
		return $parent;
	}
	$parent->l = new Node(mt_rand(0, 50), $parent->d+1);
	$parent->r = new Node(mt_rand(0, 50), $parent->d+1);
	build_tree(&$parent->l);
	build_tree(&$parent->r);
	return $parent;
}

$root = new Node(0, 1);
$root =& build_tree(&$root);

printtree(&$root, H);


echo "\n";

?>