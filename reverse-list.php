// Does not work
// <?php

// class Node {
// 	public $next;
// 	__construct($value) {
// 		$this->v = $value;
// 	}
// };

// class List {
// 	__construct() {
// 		$this->l = 0;
// 	}
	
// 	public function add($value)
// 	{
// 		$node = new Node($value);
// 		if ($this->l == 0) {
// 			$this->head = $node;
// 			$this->queue = $node;
// 		} else {
// 			$this->queue->next = $node;
// 			$this->queue = $node;
// 		}
// 		$this->l++;
// 	}
// 	public function empty()
// 	{
// 		return $this->l == 0;
// 	}
// };


// function reverse($l)
// {
// 	if ($l->empty() || $l->l < 2) {
// 		return $l;
// 	} else if ($l <= 3) {
// 		$left = reverse_left($l->head);
// 		$l->head = $left;
// 		if ($l->l == 3) {
// 			$l->queue = $l->head->next->next;
// 		} else {
// 			$l->queue = $l->head->next;
// 		}
// 	}
// 	$left = reverse_left($l->head);
// 	$right = reverse(
// 		reverse_right($l->head->next->next->next);
// 	$right->next = $left;
// 	$l->
// }

// function reverse_right($l) {
// 	if ($l->empty() || $l->l < 2) {
// 		return $l;
// 	}
// }

// function reverse_left($l)
// {
// 	if ($l->empty() || $l->l < 2) {
// 		return $l;
// 	}
// }

// ?>