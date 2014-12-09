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

var list = new List();

for (var i = 1; i <= 10; i++){
	list.add(i);
};

console.log(list.end.data);