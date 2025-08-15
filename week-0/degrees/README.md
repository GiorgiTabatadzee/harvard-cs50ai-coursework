Six Degrees of Separation: Kevin Bacon

This project explores the "Six Degrees of Kevin Bacon" concept, which suggests that any actor in Hollywood can be connected to Kevin Bacon within six steps. Each step consists of finding a movie that two actors both starred in.

The goal of this program is to find the shortest path between any two actors by identifying a sequence of movies that connects them. For example, the shortest path between Jennifer Lawrence and Tom Hanks is 2: Jennifer Lawrence is connected to Kevin Bacon through X-Men: First Class, and Kevin Bacon is connected to Tom Hanks through Apollo 13.

The problem is framed as a search problem, where each actor is a state and the movies act as actions that move from one actor to another. Using breadth-first search, the program can compute the shortest path between two actors efficiently.

Dataset

The project includes two datasets: small and large. Each dataset contains three CSV files:

people.csv: Lists each person with a unique ID, name, and birth year.

movies.csv: Lists each movie with a unique ID, title, and release year.

stars.csv: Establishes the relationship between people and movies. Each row contains a person_id and movie_id, indicating that the person starred in that movie.

For example, in the small dataset, Kevin Bacon appears in stars.csv as starring in A Few Good Men.

Program Structure

The names dictionary maps actor names to their IDs, handling cases where multiple actors share the same name.

The people dictionary maps each person’s ID to their name, birth year, and the set of movies they have starred in.

The movies dictionary maps each movie’s ID to its title, year, and the set of actors who starred in it.

The load_data function loads this information from the CSV files into memory.

The program’s main function loads the data, prompts the user to enter two actor names, resolves their IDs using person_id_for_name, and then calls shortest_path to find the shortest connection between them. The resulting path is printed, showing which actors starred together in which movies.

The shortest_path function implements the core search algorithm and is responsible for returning the shortest sequence of (movie, actor) pairs connecting the source actor to the target.
