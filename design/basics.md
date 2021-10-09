# How to write a basic program in NyaScript?

* A NyaScript program always ends with ``sleep nya``
* A definition is written with the form ``owo typeKeyword name [additional stuff]`` 
    * Type keywords are as follows:
        * ``uwu``: (mutable) variable
            * Example: ``owo uwu myVariable = ["a", "bc", 2, [3, 4]]``
        * ``stay``: constant (or immutable) variable
            * Example: ``owo stay pi = 3.141592``
        * ``pat``: function
            * Example:
            ```
                owo pat fib(n) ->
                    mya? n <= 0 ->
                        meow "Incorrect input"
                    nya- First Fibonacci number is 0
                    mya?? n == 1 ->
                        gib 0
                    nya- Second Fibonacci number is 1
                    mya?? n == 2 ->
                        gib 1
                    mya ->
                        gib (fib n-1)+(fib n-2)
                    nyanya
                nyanya
            ```
        * ``litterbox``: class
            * Example:
            ```
                owo litterbox Counter ->
                    owo litter(init, max) nya-- this is the constructor --nya ->
                        owo my num = init
                        owo my max = max
                    nyanya
                    owo pat count() ->
                        if my.num < my.max
                            incwease my.num
                        nyanya
                        gib my.num
                    nyanya
                nyanya
            ```
        * ``mew``: object (instance of a class, if you prefer)
            * Example: ``owo mew counter = Counter 0 10``

* NyaScript does not use braces for code blocks, instead it uses the ``-> nya-- some code here --nya nyanya`` syntax, where ``->`` begins the code block and ``nyanya`` ends it.

* here is how comments work in nyascript!

    * ``purr`` : is used to comment out a single line
    * ``purrs`` : is used to comment out multiple lines

        * Example:
        ```
        purr this is a single line comment!

        purrs wowow its a multiple
        comment! purrs
        ```