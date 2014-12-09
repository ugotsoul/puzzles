//linked list tutorial in javascript: http://www.i-programmer.info/programming/javascript/5328-javascript-data-structures-the-linked-list.html

function List(){
	this.start=null;
	this.end=null;
};

List.prototype.makeNode = function(){
	return {data: null, next: null};
}

List.prototype.add = function(data){
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

//find a certain node at some data point
List.prototype.find = function(data){
	
	var currentNode = this.start;

	while (currentNode.data !== data){
		currentNode = this.getNext(currentNode);
	}

	return currentNode;

};

List.prototype.delete = function(data){

};

List.prototype.count = function(){
	var n = 1;
	var currentNode = this.start;

 	while (currentNode.next !== null){
		//console.log(current.next);
		n++
		currentNode = currentNode.next;
	}

	return 'List Length: '+n;
};

//traverse the list
List.prototype.getNext = function(currentNode){

 	if (currentNode.next !== null){
		//console.log(current.next);
		currentNode = currentNode.next;
		return currentNode;
	}

	else {
		return 'End of the list.';
	}

};

//insert a node at the start
List.prototype.prepend = function(data){
	var tempNode = this.makeNode();
	tempNode.next = this.start;
	this.start = tempNode;
	tempNode.data = data;
};

var list = new List();

for (var i = 1; i <= 10; i++){
	list.add(i);
};

console.log(list.find(5));