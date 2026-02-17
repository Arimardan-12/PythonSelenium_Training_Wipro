class RestaurantService:
    def __init__(self):
        self.restaurants = {}
        self.current_id = 1

    def add_restaurant(self, data):
        data['id'] = self.current_id
        data['enabled'] = True
        self.restaurants[self.current_id] = data
        self.current_id += 1
        return data

    def update_restaurant(self, rid, data):
        if rid in self.restaurants:
            self.restaurants[rid].update(data)
            return self.restaurants[rid]
        return None

    def disable_restaurant(self, rid):
        if rid in self.restaurants:
            self.restaurants[rid]['enabled'] = False
            return True
        return False

    def get_restaurant(self, rid):
        return self.restaurants.get(rid)

    def search_restaurants(self, name=None, location=None, dish=None, rating=None):
        results = []

        for restaurant in self.restaurants.values():
            restaurant_name = str(restaurant.get("name", ""))
            restaurant_location = str(restaurant.get("location", ""))

            if name and name.lower() not in restaurant_name.lower():
                continue

            if location and location.lower() not in restaurant_location.lower():
                continue

            if rating:
                try:
                    if float(restaurant.get("rating", 0)) < float(rating):
                        continue
                except:
                    pass

            # Dish filtering (if restaurant has dishes list)
            if dish:
                dishes = restaurant.get("dishes", [])
                if not any(dish.lower() in str(d.get("name", "")).lower() for d in dishes if isinstance(d, dict)):
                    continue

            results.append(restaurant)

        return results
