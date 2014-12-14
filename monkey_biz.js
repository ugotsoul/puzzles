git//Modified linked list, from a tutorial here: http://www.i-programmer.info/programming/javascript/5328-javascript-data-structures-the-linked-list.html
function List(){
	this.start=null;
	this.end=null;
};

//Creates the node in the double linked list (eg., it has reference points to the previous and next node in the list)
List.prototype.makeNode = function(){
	return {data: null, next: null, prev: null, index: null};
}


//Adds new nodes to the end of the linked list.
List.prototype.add = function(data){

	if(this.start==null){
		this.start=this.makeNode();
		this.start.index=0;
		this.end=this.start;
		this.end.index=1;
	}
	else{
		this.end.next=this.makeNode();
		this.end.next.index = this.end.index +1;
		this.end.next.prev = this.end;
		this.end=this.end.next;
	}
	
	this.end.data = data;
};

//Find a certain node at some data value.
List.prototype.findData = function(data){
	
	var currentNode = this.start;

	while (currentNode.data !== data){
		currentNode = this.getNext(currentNode);
	}

	return currentNode;
};

//Traverse the list forward by 1 node.
List.prototype.getNext = function(currentNode){

 	if (currentNode.next !== null){
		currentNode = currentNode.next;
		return currentNode;
	}
	else {
		//End of the linked list.
		return null;
	}
};

function monkeyBusiness(numOfLockers, numOfMonkeys){

	var list = new List();

	//Adds C amount of closed lockers as nodes to the linked list.
	for (var i = 1; i <= numOfLockers; i++){
		list.add('closed');
	}

	//Reference point to the beginning of the list.
	var currentNode = list.start;

	//For each monkey, checks all the lockers//nodes in the linked list.
	//If the monkey number is a divisor of the locker number, the monkey can alter the state of the locker
	for (var currentMonkey = 1; currentMonkey <= numOfMonkeys; currentMonkey++){
		for (var i=0; i < numOfLockers; i++){

			if (currentNode.index === numOfLockers){
				currentNode = list.start;
			}

			if (currentNode.index % currentMonkey === 0){
				
				if (currentNode.data === 'open'){
					currentNode.data = 'closed';
				}

				else {
					currentNode.data = 'open';
				}
			}

			//Move forward in the linked list to the next locker.
			currentNode = list.getNext(currentNode);
		}	
	}

	//Prints the final state of the closed lockers.
	var node = list.start;
	
	console.log('------------ List of Closed Lockers ------------');
	
	for (var i=0; i < numOfLockers; i++){
		
		if (node.data === 'closed'){
			console.log('Locker #:'+node.index+' is closed.');
		}		
	
		node = list.getNext(node);
	}
};

//Call the function, make those monkeys werk!
monkeyBusiness(100,100);