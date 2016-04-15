#https://www.openstreetmap.org/node/2389658224
# Upper Yosemite Falls, because it's so tall at 550 meters, more than 300 meters
assert_has_feature(
    12, 687, 1583, 'pois',
    { 'kind': 'waterfall', 'min_zoom': 12 })

#https://www.openstreetmap.org/node/2384221575
# Middle Yosemite Falls, 206 meters, more than 50 meters
assert_has_feature(
    13, 1374, 3166, 'pois',
    { 'kind': 'waterfall', 'min_zoom': 13 })

#https://www.openstreetmap.org/node/2389657981
# Lower Yosemite Falls, only 98 meters
assert_has_feature(
    13, 1374, 3167, 'pois',
    { 'kind': 'waterfall', 'min_zoom': 13 })

#https://www.openstreetmap.org/way/56539663
# Niagara Falls (Horseshoe Falls)
assert_has_feature(
    12, 1148, 1503, 'pois',
    { 'kind': 'waterfall', 'min_zoom': 12 })

# We had considered this for label_placement:yes, 
# but there are only 19 in all of North America
assert_no_matching_feature(
    12, 1148, 1503, 'water',
    { 'kind': 'waterfall' })
    
#https://www.openstreetmap.org/node/2375445789
# Alamere Falls (no height)
# Assume falls are important, show at zoom 14 default
assert_has_feature(
    14, 2604, 6322, 'pois',
    { 'kind': 'waterfall', 'min_zoom': 14 })
    
#http://www.openstreetmap.org/node/3257658773
# Abrigo Falls, 4.5 meters (less than 8 meters)
# Allow short waterfalls to be suppressed a zoom
assert_has_feature(
    15, 5265, 12645, 'pois',
    { 'kind': 'waterfall', 'min_zoom': 15 })