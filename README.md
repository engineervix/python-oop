# README

> Learning OOP in Python, via [this course](https://realpython.com/courses/inheritance-composition-python/)

## When to use Inheritance over Composition ...

1. Use inheritance over composition in Python to model a clear **is a** relationship. 
    * First, justify the relationship between the derived class and its base. Then, reverse the relationship and try to justify it. If you can justify the relationship in both directions, then you should not use inheritance between them.
2. Use inheritance over composition to leverage both the interface and implementation of those base classes.
3. Use inheritance over composition to provide mixin features to several unrelated classes where there is only one implementation of that feature. This could be like a utility, such as a method to represent the object as a dictionary.

## When to use Composition over Inheritance ...

1. Use composition over inheritance to model a **has a** relationship that leverages the implementation of the component class.
2. Use composition over inheritance to create components that can be reused by multiple classes in your Python application.
3. Use composition over inheritance to implement groups of behaviors and policies that can be applied interchangeably to other classes to customize their behavior. 
4. Use composition over inheritance to enable run-time behavior changes without affecting existing classes.