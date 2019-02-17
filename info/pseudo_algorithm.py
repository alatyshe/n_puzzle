========================================================================
========================================================================
FIRST VERSION
========================================================================
========================================================================

OPEN // the set of nodes to be evaluated
CLOSED // the set of nodes already evaluated

add the start node to OPEN

loop
	current = node in OPEN with the lowest f_cost
	remove current from OPEN
	add corrent to CLOSED

	if current is the target node // path has been found
		return

	foreach neighbour of the current node
		if neighbour is not traversable or neighbour is in CLOSED
			skip to the next neighbour

		if new path to neighbour is shorter OR neighbour is not in OPEN
			set f_cost of neighbour
			set parent of neighbour to current

			if neighbour is not in OPEN
 				add neighbour to OPEN



========================================================================
========================================================================
SECOND VERSION
========================================================================
========================================================================

set opened
set closed

bool succes

While (opened != empty) and  (succes == false) do
	state e // elem from opened
	if is_final(e)
		succes = true
	else
		opened = opened - e
		closed = closed + e

		foreach state s in e do
			if (s != opened) and (s != closed)
				opened = opened + s
				predecessor(s) <- e
				g(s) <- g(e) + C(e-->s)

			else // s is in 'opened' or in 'closed' 
				if g(s) + h(s) > g(e) + C(e-->s) + h(s)
				// i.e. f value > 'potentially new' f value
					Than g(s) <- g(e) + C(e-->s)
						predecessor(s) <- e
						if s in closed
							closed = closed - s
							opened = opened + s





							
