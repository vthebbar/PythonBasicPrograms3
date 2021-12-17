Basic Python  programs to illustrate the python programming concepts:
===================================================================

Topics:

1. Zip Function
2. Lambda Function
3. Read and Write file (With and Without Context manager)
4. Assert in python - Used to verify the test result (To Check condition is true or false)
5. Exception handling - try, except, else, finally , raise
6. Constructor and Inheritance of constructor
7. Method overriding
8. Inheritance - Single level, multi level, multiple and Hybrid. Advantage: code re-usability (inherit method and properties)
9. Class, Object and Constructor
10. What is Modules and Packages In Python -> Module is a python file (file with .py extension)
        Modules can be inbuilt, user defined or external
        Packages - are combination of multiple modules.
       Python inbuilt modules - example- calendar, os, math ...
11. *args and **kwargs  (Arbitrary argument and Arbitrary keyword argument) - used for passing variable number of parameters
      *args will receive values as tuple
      **kwargs will receive values as dictionary

      we can use both *args and **kwargs in same function as arguments
      We can also use argument, *args and **kwargs in same function as arguments

12. Functions in Python - with return value, with default arguments, with different arguments
    Function is a block of code/set of statements with performs specific task/activity.
    Advantages : Re-usability and readability

    We can also pass parameters to functions as key=value pair.

    Passing list as parameter is possible.

13.  while loop
      While loop is used to run piece of code multiple times, While loop is used when we do not know how many times
      code need to be run. (Example - run code to get response as long as server is up and running)
      While loop runs as long as given condition is true and once condition is false contorl comes out of the loop
      Need to initialize a loop variable before while loop and need to increment or decrement variable inside the loop
      While loop can be used with else, break, continue, pass

14. for loop

    For loop is used for running a piece of code multiple times. When we are using for loop we know how many times code..
    ..to be run
    else statement can be used with for loop
    Use of range(start,end),  Use of nested for loop


15. Python Intro
    High level, interpreted , general purpose programming language.
    portable, dynamically typed(No need to explicitly mention dat atype), extensible, object oriented, free/open source


16. Data Types in Python
    Numbers -> Integers (int), float (float), complex (complex)
    Boolean (bool) -> True, False
    Strings - str
    Lists - list
    Dictionary - dict
    Tuples - tup
    Sets - set

    Power of operator->2 power 8  => 2**8

    Note: each data type in python is a class

17. Strings
    Note: Strings are immutable
     Built in string methods
     Escape sequence characters
     Indexing
     Slicing
     Format method
     Format string literal f-string
     Step count  (string reversal [::-1]

18. Lists  []
     List is a collection of values/objects. Lists are indexed, Lists are ordered, Lists allow duplicate elements.
     List size is dynamic.(no need to specify size)
     Creating list.
     List methods - append, insert,remove, pop, sort,,Count, reverse ...
     Slicing
     Add list into another list.
     List of lists is allowed
     Note: When extend list with string, it will append character by character


19.  Sets  { }
        Set is collection of values (objects)
        It is unordered collection. i.e it does not have index.
        It does not allow duplicates.
        # Using set() constructor*

        Methods - > add(x), pop()-removes rand element,remove(x), discard(x) , len(myset), myset.clear(), myset.copy(),

        convert list to set -> set1 = set(list1)
        Convert tuple to set -> set2 = set(tup1)

 20. Dictionary {key : "Value"}

        Dictionary is a collection of items.
        Each item in dictionary is a key-value pair.
        It is dynamic in nature(i.e no need to declare size)
        It is unordered (i.e no index numbers)
        We can fetch values using key.
        Key in dictionary must be unqiue but values can be duplicate.

        Using dictionary constructor dict() to create dictionary:  mydict= dict(key="value",...)
        OR by passing key value pair as a list of tuples.
        mydict = dict([(key1,value1),(key2,value2)...])

         -List inside dictionary
         -Dictionary inside dictionary
         -Accessing elements in nested dictionary-> dict_name.get(key).get(key)
           OR  dict_name["key"]["key"]

        -> Add, update, delete(pop and popitem) values in dictionary
            add ->   dict_name["new_key"] = "value"
            Update -> dict_name["existing_key"] ="new value"
            delete - >  dict_name.pop("key")
                    -> dict_name.popitem()  -> removes element in last in First Out (LIFO) order

            -> len
            -> dict_name.keys()  -> to get keys only
            -> dict_name.values()  -> to get onyl values
            -> dict_name.items()  -> to get key-value pair  in the form of tuples

            -> How to delete specific key -value pair  -> del dict_name["key"]

            -> to delete entire dictionary  ->  del dict_name

              -> keys are case sensitive

               * ->Another way to creating dictionary:
              mydict =dict(10="python", 20="java")

                *-> One more way to create dictionary using list of tuples
                mydict = dict([(1,"Python"),(2,"java")])

21 . Tuples ( )
        -> Tuples are collections of values/objects
        -> Tuples are immutable
        -> Tuples are ordered and indexed

        -> Indexing, slicing, tuple unpacking

        -> Another way to create tuple is using tuple() constructor
            ex: tup1 = tuple([1,2,3,4])
        -> Methods - count() , index()

        ->Convert tuple into list using constructor
        -> Convert tuple into set  using constructor


        *Another way to create tuple:
            tup2 =("Raj")
            len(tup2)  = 3 -> when string is passed and there is only one value in tuple,
            it will consider character by character

             if we use , count will change
             tup2=("Raj",)
             len(tup2)=1


           * Tuple unpacking:

           *Using tuple constructor to create tuple
           t1 =tuple([1,2,3,4,])


            * Tuple unpacking:
            a,b,c,d = t1


 22 .  If, elif, else
        -> Single line if else.

       print("do something") if a>b else print("do something else")



