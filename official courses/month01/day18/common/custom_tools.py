class IterableHelper:
    @staticmethod
    def find_all(literable,func):
        for item in literable:
            if func(item):
                yield item

    @staticmethod
    def find(literable,func):
        for item in literable:
            if func(item):
                return item

    @staticmethod
    def select(literable,func):
        for item in literable:
            yield func(item)

    @staticmethod
    def delete_all(literable,func):
        for i in range(len(literable)-1,-1,-1):
            if func(literable[i]):
                del literable[i]

    @staticmethod
    def get_count(literable, func):
        count = 0
        for item in literable:
            if func(item):
                count += 1
        return count

    @staticmethod
    def is_exists(literable, func):
        for item in literable:
            if func(item):
                return True
        return False