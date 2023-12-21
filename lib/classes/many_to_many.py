class NationalPark:

    def __init__(self, name):
        if not isinstance(name, str) or not (3 <= len(name)):
            raise ValueError("Name must be a string greater or equal to 3 characters")
        
        if hasattr(self, "_name"):
            raise AttributeError("Name is immutable and cannot be changed after instantiation.")
        
        self._name = name
        self._trips = []
        self._visitors = set()

    @property
    def name(self):
        return self._name
        
    def trips(self):
        return self._trips
    
    def visitors(self):
        return list(self._visitors)
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        visit_counts = {}
        for trip in self._trips:
            visitor = trip.visitor
            visit_counts[visitor] = visit_counts.get(visitor, 0) + 1
        return max(visit_counts, key=visit_counts.get)


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(start_date, str) or not (7 <= len(start_date)):
            raise ValueError('Start Date must be a string greater or equal to 7 characters')
        
        if not isinstance(end_date, str) or not (7 <= len(end_date)):
            raise ValueError('End Date must be a string greater or equal to 7 characters')
        
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        visitor._trips.append(self)
        national_park._trips.append(self)
        national_park._visitors.add(self.visitor)
        visitor._national_park.add(self.national_park)
        Trip.all.append(self)
    
    @property  
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, new_date):
        if not isinstance(new_date, str):
            raise ValueError("Start Date must be a string.")
        self._start_date = new_date

    @property  
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, new_date):
        if not isinstance(new_date, str):
            raise ValueError("End Date must be a string.")
        self._end_date = new_date

    def visitor(self):
        return self.visitor
    
    def national_park(self):
        return self.national_park


class Visitor:

    def __init__(self, name):
        if not isinstance(name, str) or not (1<= len(name) <= 15):
            raise ValueError('Name must be a string between 1 and 15 characters')
        
        self.name = name
        self._trips = []
        self._national_park = set()
        

    @property  
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Visitor name must be a string.")
        self._name = new_name
        
    def trips(self):
        return self._trips
    
    def national_parks(self):
        return list(self._national_park)
    
    def total_visits_at_park(self, park):
        return sum(1 for trip in self._trips if trip.national_park == park)