# @ Symbol
``@ symbol is decorator syntax.``
    A decorator is a function (or callable) that:
    Takes another function or class as input
    Modifies or enhances its behavior
    Returns the modified function or class
``General rule for @ in Python``
    | Context       | Meaning                             |
    | ------------- | ----------------------------------- |
    | `@decorator`  | Modify function or class definition |
    | Above `def`   | Decorates a function                |
    | Above `class` | Decorates a class                   |
    | Multiple `@`  | Applied **top-down**                |
