class SearchStrategy:

    def find_jobs(self):
        pass


class SkillSearch(SearchStrategy):

    def find_jobs(self):
        return "Python Developer jobs found"


class LocationSearch(SearchStrategy):

    def find_jobs(self):
        return "Jobs available in Kochi"


class SalarySearch(SearchStrategy):

    def find_jobs(self):
        return "Jobs above ₹8 LPA found"


class JobSearch:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def search_jobs(self):
        print(self.strategy.find_jobs())