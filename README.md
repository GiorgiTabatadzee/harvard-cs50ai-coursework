Six Degrees of Separation

This project is part of Harvard's CS50 Introduction to Artificial Intelligence with Python. It explores the concept of "six degrees of separation" by finding the shortest connection between two actors based on the movies they have starred in together. The program loads data from CSV files containing information about people, movies, and the actors in those movies, and then uses a search algorithm to determine the shortest path connecting any two actors.

The program can resolve ambiguities when multiple actors share the same name, and it prints out both the number of degrees of separation and the movies that connect the actors along the way. You can run the program from the command line and choose between a small dataset for testing or a large dataset for more extensive connections.

This project was implemented entirely in Python and uses breadth-first search to guarantee that the shortest path is found. It demonstrates practical applications of search algorithms and working with real-world datasets.
