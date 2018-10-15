rooms = {
	"kitchen" : {
		"south" : "hall",
		"west" : "dining room",
		"item" : "knife"
	},
	"dining room" : {
		"east" : "kitchen"
	},
	"hall" : {
		"north" : "kitchen",
		"east" : "foyer",
		"south" : "bathroom",
		"west" : "family room"
	},
	"bathroom" : {
		"north" : "hall",
		'item' : 'key'
	},
	"family room" : {
		"east" : "hall",
		'item' : 'candlestick'
	},
	"foyer" : {
		"west" : "hall",
		"east" : "garden"
	},
	"garden" : {
		'west' : 'foyer'
		}
}
