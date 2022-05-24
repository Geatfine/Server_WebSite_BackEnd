class repository(object):
    def __init__(self, selector):
        if not adapter:
            raise ValueError(" Invalide repository implementation")
        self.client = adapter()

    def find_all(self, selector):
        return self.client.find_all(selector)

    def find(self, selector):
        return self.client.find(selector)

    def create(self, xoro):
        return self.client.create(xoro)

    def update(self, selector, xoro):
        return self.client.update(selector, xoro)

    def delete(self, selector):
        return self.client.delete(selector)



