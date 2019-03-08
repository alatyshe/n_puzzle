var json = JSON.parse(document.getElementById('searcher').getAttribute("data-json"));

var size = Math.pow(json['size'], 2);
var array = json['elements'];


var puzzle = {
	Stop: false,
	Step: 0,
	Move: {up: -json['size'], left: -1, down: json['size'], right: 1},
	order: array,

	go: function(move) {
		this.hole = this.order.indexOf(0);
		var index = this.hole + move;
 		if (!this.order[index]) return false;
		if (move === puzzle.Move.left || move === puzzle.Move.right)
		if (Math.floor(this.hole/json['size']) !== Math.floor(index/json['size'])) return false;
		this.swap(index, this.hole);
		this.hole = index;
		return true;
	},

	swap: function(i1, i2) {
		var t = this.order[i1];
		this.order[i1] = this.order[i2];
		this.order[i2] = t;
	},
};


const sleep = (milliseconds) => {
	return new Promise(resolve => setTimeout(resolve, milliseconds))
};


var box = document.body.appendChild(document.createElement('div'));

for (var i = 0; i < size; i++) {
	box.appendChild(document.createElement('div'));
}


function draw() {
	for (var i = 0, tile; tile = box.childNodes[i], i < size; i++) {
		tile.textContent = puzzle.order[i]; tile.style.visibility = puzzle.order[i] ? 'visible' : 'hidden';
	}
}


const moving = async(sequence) => {
	for (; puzzle.Step < sequence.length; puzzle.Step++) {

		if (!puzzle.Stop) {
			try {
				var pause = document.getElementById("slider").elements.level.value;
			}
			catch (TypeError) {
				var pause = 1500;
			} 

			if (puzzle.go(puzzle.Move[{39: 'left', 37: 'right', 40: 'up', 38: 'down'}[sequence[puzzle.Step]]])) {

				draw();
				var move = document.getElementById('move');
				move.style.display = 'block';
				move.textContent = {37: 'left', 38: 'up', 39: 'right', 40: 'down'}[sequence[puzzle.Step]];
			}
			await sleep(pause);
		}
		else { break; }
	}
	if (puzzle.Step == sequence.length) {
		var move = document.getElementById('move');
		move.style.display = 'block';
		move.textContent = "Done"
	}
};


function start() {
	if (json['move']) {
		moving(json['move']);
	}	
}


draw();
