//modified linked list tutorial in javascript: http://www.i-programmer.info/programming/javascript/5328-javascript-data-structures-the-linked-list.html

function List(){
	this.start=null;
	this.end=null;
};

//creates the node in the double linked list (eg., it has reference points to the previous and next node in the list)
List.prototype.makeNode = function(){
	return {data: null, next: null} //prev: null, index: null};
}

List.prototype.add = function(data){

	var i = 1;

	if(this.start==null){
		//this is a new list, make a start node, then link it to the end node
		this.start=this.makeNode();
		this.end=this.start;
	}
	else{
		//this list exists, point the end of the list to the new node
		this.end.next=this.makeNode();
		this.end=this.end.next;
	}
	
	this.end.data = data;
};

List.prototype.circular = Function(){

	//find the end node, link the next node to the start node.
	this.end.next = this.start;

};

List.prototype.addAtIndex = function(index){};

List.prototype.removeByIndex = function(index){};


//find a certain node at D data value
List.prototype.findData = function(data){
	
	var currentNode = this.start;

	while (currentNode.data !== data){
		currentNode = this.getNext(currentNode);
	}

	return currentNode;
};

//find a certain node at N index value
List.prototype.findIndex = function(index){
	
	var currentNode = this.start;

	while (currentNode.index !== index){
		currentNode = this.getNext(currentNode);
	}
	return currentNode;
};

List.prototype.count = function(){
	var n = 1;
	var currentNode = this.start;

 	while (currentNode.next !== null){
		//console.log(current.next);
		n++
		currentNode = currentNode.next;
	}
	return n;
};

//traverse the list by 1 node
List.prototype.getNext = function(currentNode){

 	if (currentNode.next !== null){
		currentNode = currentNode.next;
		return currentNode;
	}
	else {
		//End of the line
		return null;
	}
};

List.prototype.print = function(){

	var currentNode = this.start;
	console.log("--- Start Of List ---");
	while (currentNode.next !== null){
		console.log('------------------------');
		console.log('List Node Index: '+currentNode.index);
		console.log('List Node Data: '+currentNode.data);
		currentNode = this.getNext(currentNode);
	}
	return "--- End Of List ---";
};

//insert a node at the start of the list
List.prototype.prepend = function(data){
	var tempNode = this.makeNode();
	tempNode.next = this.start;
	this.start = tempNode;
	tempNode.data = data;
};


function rudeChairs(numOfChairs, numOfPeople){

	var list = new List();

	for (var i = 1; i <= numOfChairs; i++){
		list.add(i);
	}

	var emptyChairs = 0;
	var currentNode = list.start;

	return console.log(list);
}

rudeChairs(100,100);