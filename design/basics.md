# How to write a basic program in NyaScript?

* A NyaScript program always ends with ``sleep``
* A definition is written with the form ``owo typeKeyword name [additional stuff]`` 
    * Type keywords are as follows:
        * ``uwu``: (mutable) variable
            * Example: ``owo uwu my_variable = ["a", "bc", 2, [3, 4]]``
        * ``stay``: constant (or immutable) variable
            * Example: ``owo stay pi = 3.141592``
        * ``pat``: [function](./functions.md)
        * ``litterbox``: [class](./classes.md)
        * ``mew``: [object](./classes.md) (instance of a class, if you prefer)

* NyaScript does not use braces for code blocks, instead it uses the ``-> purrs some code here purrs nyanya`` syntax, where ``->`` begins the code block and ``nyanya`` ends it.

* here is how comments work in nyascript!

    * ``purr`` : is used to comment out a single line
    * ``purrs`` : is used to comment out multiple lines or to specify a delimited comment

        * Example:
        ```
        purr this is a single line comment!

        purrs wowow its a multiple
        comment! purrs
        
        meow(purrs this is going to be ignored by the language purrs "Hi!")
        ```
