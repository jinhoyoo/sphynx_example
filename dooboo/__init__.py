# -*- coding: utf-8 -*-


class BaseEngine:
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attribute and property types -- if given -- should be specified according
    to `PEP 484`_, though `PEP 484`_ conformance isn't required or enforced.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (Optional[int]): Description of `attr2`.


    .. _PEP 484:
       https://www.python.org/dev/peps/pep-0484/

    """
    def query(keyword):
        pass
