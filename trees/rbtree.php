#!/usr/bin/php
<?php
###
# Author: TD
# License: GPLv3
####

define('RED', 1);
define('BLACK', 0);

/**
* 
*/
class Node
{
   
    function __construct($parent, $value, $left=null, $right=null, $color=RED)
    {
        $this->p = $parent;
        $this->v = $value;
        $this->l = $left;
        $this->r = $right;
        $this->c = $color;
    }
}

class Tree {
    protected $NIL;
    
    function __construct($root_value) {
        $this->root = new Node(null, $root_value);
        $this->root->c = BLACK;
        $this->NIL = new Node($this->root, null, $this->root, $this->root, BLACK);
        $this->root->l = $this->NIL;
        $this->root->r = $this->NIL;
        $this->root->p = $this->NIL;
    }
    
    function insert($value) {
    	$node = new Node($this->NIL, $value, $this->NIL, $this->NIL);
        $prev = null;
        $curr = $this->root;
        while($curr !== $this->NIL) {
        	// echo "Pouet\n";
            if($node->v < $curr->v) {
                $prev = $curr;
                $curr = $curr->l;
            } else if($node->v > $curr->v) {
                $prev = $curr;
                $curr = $curr->r;
            } else {
                return false; // Cannot insert, already present in the tree
            }
        }
        if($prev === $this->NIL) {
            $this->set_root($node); 
        } else if($node->v > $prev->v) {
            $prev->r = $node;
        } else {
            $prev->l = $node;
        }
        $node->p = $prev;
        $node->c = RED;
        $node->l = $this->NIL;
        $node->r = $this->NIL;
        
        $this->insert_fixup($node);
        return true;
    }
    
    function insert_fixup($node) {
        while($node->p->c == RED) {
        	// echo "Tralala\n";
            if($node->p === $node->p->p->l) { # parent is a left child
                $y = $node->p->p->r;
                if($y->c == RED) {
                    $node->p->c = BLACK;
                    $y->c = BLACK;
                    $node->p->p->c = RED;
                    $node = $node->p->p;
                } else {
	                if($node === $node->p->r) { # z is a right child
	                    $node = $node->p;
	                    $this->left_rotate($node);
	                }
                    $node->p->c = BLACK;
                    $node->p->p->c = RED;
                    $this->right_rotate($node->p->p);
                }
            } else { # parent is a right child
                $y = $node->p->p->l;
                if($y->c == RED) {
                    $node->p->c = BLACK;
                    $y->c = BLACK;
                    $node->p->p->c = RED;
                    $node = $node->p->p;
                } else {
                	if($node === $node->p->l) {
	                    $node = $node->p;
	                    $this->right_rotate($node);
                    }
                    $node->p->c = BLACK;
                    $node->p->p->c = RED;
                    $this->left_rotate($node->p->p);
                }
            }
        }
        $this->root->c = BLACK;
    }
    
    function left_rotate($x) {
        echo "Left rotate\n";
        $y = $x->r;
        $x->r = $y->l;
        if($y->l !== $this->NIL) {
            $y->l->p = $x;
        }
        $y->p = $x->p;
        if($x->p === $this->NIL) {
            $this->set_root($y);
        } else if($x->p->l === $x) { # x is a left child
            $x->p->l = $y;
        } else {
            $x->p->r = $y;
        }
        $y->l = $x;
        $x->p = $y;
    }
    
    function right_rotate($x) {
    	echo "Right rotate\n";
        $y = $x->l;
        $x->l = $y->r;
        if($y->r !== $this->NIL) {
            $y->r->p = $x;
        }
        $y->p = $x->p;
        if($x->p === $this->NIL) {
            $this->set_root($y);
        } else if($x->p->r === $x) { # x is a right child
            $x->p->r = $y;
        } else {
            $x->p->l = $y;
        }
        $y->r = $x;
        $x->p = $y;
    }
    
    
    function set_root($y) {
        $this->root = $y;
        $this->root->p = $this->NIL;
        $y->l->p = $this->root;
        $y->r->p = $this->root;
    }
    
    function delete_fixup($node) {}
    
    function search($value) {}
    
    function delete($value) {
    	
    }
    
    function printh() {
    	$this->_printh($this->root, 0);
    	echo "\n(NIL->c={$this->NIL->c})\n";
    }
    
    protected function _printh($node, $h) {
    	echo "\n";
    	for ($i=0; $i < $h; $i++) { 
    		echo "\t";
    	}
    	echo "- ({$node->v}, {$node->c})";
    	if ($node->l !== $this->NIL) {
    		$this->_printh($node->l, $h+1);
    	}
    	if ($node->r !== $this->NIL) {
    		$this->_printh($node->r, $h+1);
    	}
    }
}

$t = new Tree(5);
$t->insert(3);
$t->insert(2);
// $t->insert(6);
// $t->insert(2.5);
// $t->insert(-2);
// $t->insert(-3);
// $t->insert(-4);

// for ($i=0; $i < 40; $i++) { 
// 	$t->insert(mt_rand(-100, 100));
// }

$t->printh();

?>