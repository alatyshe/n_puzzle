Start=initial node;
Goal=final node;
open_list.insert(Start);	//list of type node
closed_list=empty set;		//list of type node
Start.g=0;
Start.h=heuristic(Start); Start.f=Start.g+Start.h;

function A*()                                             //Driver function
{
	while(!open_list.empty())	//run until open list is empty
	{
		process=open_list(node with min(f));
		if(process==Goal)
			return (function path(process));              //path to goal found
		open_list.remove(process);
		closed_list.insert(process);
		foreach(node in nextnodes(process))          //run for all the nodes possible from current
		{
			if(closed_list.count(node)!=0)             //Does not exist in closed list
				skip this loop once;
			if(open_list.count(node)==0)               //Does not exist in open list
				open_list.insert(node)
			else
			{
				actual_node=open_list.find(node);       //if exists find node in open_list
				if(node.g<actual_node.g)                  //better g score for same node found
				{
					actual_node.g=node.g;
					actual_node.f=node.f;
					actual_node.parent=node.parent;//change parent to better(earlier parent)
				}
			}
		}
	}
	print(“Not possible to reach goal”);
}

function nextnodes(node) {
	return list of all possible next nodes from node;
}

function path(node) {
	construct the path from node to start using node.parent;
}

