rooms = {
	"kitchen" : {
		"south" : "hall",
		"west" : "dining room"
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
		"north" : "hall"
	},
	"family room" : {
		"east" : "hall",
		'up' : 'second floor bedroom'
	},
	"foyer" : {
		"west" : "hall"
	},
	"garden" : {
		'west' : 'foyer'
	},
	'second floor bedroom' : {
		'down' : 'family room',
		'east' : 'second floor patio'
	},
	'second floor patio' : {
		'west' : 'second floor bedroom'
	}
}
items = {
	"kitchen" : {
		"item" : "knife"
	},
	"dining room" : {
	},
	"hall" : {
	},
	"bathroom" : {
		'monster' : 'Glob Monster'
	},
	"family room" : {
		
	},
	"foyer" : {
		'item' : 'candlestick'
	},
	"garden" : {
		
	},
	'second floor bedroom' : {
		'item' : 'key'
	},
	'second floor patio' : {
		'monster' : 'Bird Man'
	}
}
