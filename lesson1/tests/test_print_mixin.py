import pytest
from lesson1.print_mixin import PrintMixin

def test_print_called_on_init(capsys):
    class Dummy(PrintMixin):
        def __init__(self, a, b):
            self.a = a
            self.b = b
            super().__init__()

    d = Dummy(1, 2)
    captured = capsys.readouterr()
    assert "Dummy(a=1, b=2)" in captured.out

def test_repr_with_init_params():
    class Dummy(PrintMixin):
        def __init__(self, x, y):
            self.x = x
            self.y = y
            super().__init__()

    d = Dummy(10, 20)
    repr_str = repr(d)
    assert "Dummy(" in repr_str
    assert "x=10" in repr_str
    assert "y=20" in repr_str

def test_repr_includes_additional_attrs():
    class Dummy(PrintMixin):
        def __init__(self, a):
            self.a = a
            super().__init__()
            self.extra = "extra"

    d = Dummy(5)
    repr_str = repr(d)
    assert "a=5" in repr_str
    assert "extra='extra'" in repr_str

def test_repr_handles_missing_signature():
    class Dummy(PrintMixin):
        __init__ = lambda self: None  # нарушаем сигнатуру

    d = Dummy()
    repr_str = repr(d)
    assert "Dummy()" in repr_str