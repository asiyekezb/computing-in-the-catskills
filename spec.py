class Spec:
    def __init__(self, data):
        self.data = data
        bbox = data['bbox']
        self.north = bbox['north']
        self.south = bbox['south']
        self.east = bbox['east']
        self.west = bbox['west']
        self.num_peaks = data['num_peaks']
        self.max_peaks_per_hike = data['max_peaks_per_hike']
        self.invalid_parking_ids = set(data.get('invalid_parking_ids', []))
        self.bad_lot_walks = [{a, b} for a, b in data.get('bad_lot_walks', [])]
        self.edges_to_toss = [(a, b) for a, b in data.get('edges_to_toss', [])]
        self.forced_clusters = [set(x) for x in data.get('forced_clusters', [])]
        self.roads_that_are_trails = set(data.get('roads_that_are_trails', []))

    def is_in_bbox(self, lon: float, lat: float):
        return self.south <= lat <= self.north and self.west <= lon <= self.east
