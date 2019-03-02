var json = JSON.parse(document.getElementById('searcher').getAttribute("data-json"));

var size = Math.pow(json['size'], 2);
var array = json['elements'];


var puzzle = {
	Move: {up: -json['size'], left: -1, down: json['size'], right: 1},
	order: array,

	isCompleted: function() {
		return !this.order.some(function(item, i) { return item > 0 && item-1 !== i; });
	},

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

	solvable: function(a) {
	for (var kDisorder = 0, i = 1, len = a.length-1; i < len; i++)
		for (var j = i-1; j >= 0; j--) {
			if (a[j] > a[i]) kDisorder++;
		}
		return !(kDisorder % 2);
	}
};

if (!puzzle.solvable(puzzle.order)) {
	puzzle.swap(0, 1);
}

const sleep = (milliseconds) => {
	return new Promise(resolve => setTimeout(resolve, milliseconds))
};

var box = document.body.appendChild(document.createElement('div'));

for (var i = 0; i < size; i++) {
	box.appendChild(document.createElement('div'));
}

window.addEventListener('keydown', function(e) {
	if (puzzle.go(puzzle.Move[{39: 'left', 37: 'right', 40: 'up', 38: 'down'}[e.keyCode]])) {
		draw();

		let move = document.getElementById('move');
		move.style.display = 'block';
		move.textContent = {37: 'left', 38: 'up', 39: 'right', 40: 'down'}[e.keyCode];

		if (puzzle.isCompleted()) {
			box.style.backgroundColor = "gold";
			window.removeEventListener('keydown', arguments.callee);
		}
	}
});

function draw() {
	for (var i = 0, tile; tile = box.childNodes[i], i < size; i++) {
		tile.textContent = puzzle.order[i]; tile.style.visibility = puzzle.order[i] ? 'visible' : 'hidden';
	}
}

const moving = async(sequence) => {
	for (var j = 0; j < sequence.length; j++) {

		if (puzzle.go(puzzle.Move[{39: 'left', 37: 'right', 40: 'up', 38: 'down'}[sequence[j]]])) {
			// alert(move);

			draw();
			// var move = document.getElementById('move');
			// move.style.display = 'block';
			// move.textContent = {37: 'left', 38: 'up', 39: 'right', 40: 'down'}[sequence[j]];

			// if (puzzle.isCompleted()) {
			//     box.style.backgroundColor = "gold";
			// }
		}
		await sleep(1000);
	}
};

if (json['move']) {
	moving(json['move']);
}

draw();
