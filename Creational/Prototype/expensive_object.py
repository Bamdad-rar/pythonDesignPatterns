


class Website:
    def __init__(self,name,domain,url,**kwargs):
        self.name = name
        self.domain = domain
        self.url = url
        
        for item in kwargs:
            setattr(self, item, kwargs[item])

    def __str__(self):
        result = []
        for item in vars(self):
            result.append(f"{item}={vars(self).get(item)}")
        return " ".join(result)
