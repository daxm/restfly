import pytest
from restfly.iterator import APIIterator

class ExampleIterator(APIIterator):
    def _get_page(self):
        self.total = 100
        self.limit = 10
        self.page = [{'id': i + self.offset} for i in range(10)]
        self.offset += self.limit

def test_iterator():
    items = ExampleIterator(None)
    last_item = None
    for item in items:
        last_item = item
    assert last_item == {'id': 99}
    assert items.total == 100
    assert items.count == 100
    assert items.num_pages == 10
    assert items.page_count == 10
    assert items.page == [
        {'id': 90},
        {'id': 91},
        {'id': 92},
        {'id': 93},
        {'id': 94},
        {'id': 95},
        {'id': 96},
        {'id': 97},
        {'id': 98},
        {'id': 99}
    ]

def test_iterator_max_items():
    items = ExampleIterator(None, max_items=15)
    last_item = None
    for item in items:
        last_item = item
    assert last_item == {'id': 14}
    assert items.total == 100
    assert items.count == 15
    assert items.num_pages == 2
    assert items.page_count == 5
    assert items.page == [
        {'id': 10},
        {'id': 11},
        {'id': 12},
        {'id': 13},
        {'id': 14},
        {'id': 15},
        {'id': 16},
        {'id': 17},
        {'id': 18},
        {'id': 19}
    ]

def test_iterator_max_pages():
    items = ExampleIterator(None, max_pages=2)
    last_item = None
    for item in items:
        last_item = item
    assert last_item == {'id': 19}
    assert items.total == 100
    assert items.count == 20
    assert items.num_pages == 2
    assert items.page_count == 10
    assert items.page == [
        {'id': 10},
        {'id': 11},
        {'id': 12},
        {'id': 13},
        {'id': 14},
        {'id': 15},
        {'id': 16},
        {'id': 17},
        {'id': 18},
        {'id': 19}
    ]