from daftlistings import Daft, Location, SearchType, PropertyType
from datetime import datetime
import json

daft = Daft()
daft.set_location(Location.DUBLIN)
daft.set_search_type(SearchType.RESIDENTIAL_RENT)
daft.set_property_type(PropertyType.APARTMENT)
daft.set_min_price(500)
daft.set_max_price(10_000)

listings = daft.search(max_pages=1)

for listing in listings:
    print(listing.title)