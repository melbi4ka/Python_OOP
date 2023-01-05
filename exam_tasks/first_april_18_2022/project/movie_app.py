from project import user
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []


    def register_user(self, username: str, age: int):
        for user in self.users_collection:
            if user.username == username:
                raise Exception ("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{new_user.username} registered successfully."


    def upload_movie(self, username, movie: Movie):
        if all ([usr.username != username for usr in self.users_collection]):
            raise Exception("This user does not exist!")
        for usr in self.users_collection:
            if usr.username == username and username != movie.owner.username:
                raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for mvi in self.movies_collection:
            if mvi == movie:
                raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        for usr in self.users_collection:
            if usr.username == username:
                usr.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie: Movie, **kwargs):

        if movie not in self.movies_collection:
            raise Exception (f"The movie {movie.title} is not uploaded!")
        for usr in self.users_collection:
            if usr.username == username and username != movie.owner.username:
                raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for k,v in kwargs.items():
            new = v
            if k == "title":
               movie.title = new
            elif k == "year":
                movie.year = new
            elif k == "age_restriction":
                movie.age_restriction = new
        return f"{username} successfully edited {movie.title} movie."


    def delete_movie(self, username, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception (f"The movie {movie.title} is not uploaded!")
        for usr in self.users_collection:
            if usr.username == username and username != movie.owner.username:
                raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        for usr in self.users_collection:
            if usr.username == username:
                usr.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie: Movie):
        if any([usr.username == username for usr in self.users_collection]):
            if username == movie.owner.username:
                raise Exception(f"{username} is the owner of the movie {movie.title}!")
        for usr in self.users_collection:
            if usr.username == username:
                if movie in usr.movies_liked:
                    raise Exception(f"{username} already liked the movie {movie.title}!")
                else:
                    usr.movies_liked.append(movie)
                    movie.likes += 1
                    return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie: Movie):
        for usr in self.users_collection:
            if usr.username == username:
                if all([mvi!=movie for mvi in usr.movies_liked]):
                    raise Exception (f"{username} has not liked the movie {movie.title}!")
                else:
                    usr.movies_liked.remove(movie)
                    movie.likes -= 1
                    return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        sorted_movie_collection = sorted(self.movies_collection, key = lambda x: (-x.year, x.title))
        result = []
        for movie in sorted_movie_collection:
            result.append(movie.details())
        return "\n".join(result)

    def __str__(self):
        if not self.users_collection:
            result = "All users: No users." + "\n"
        else:
            result = f"All users: {', '.join([usr.username for usr in self.users_collection])}\n"
        if not self.movies_collection:
            result += "All movies: No movies."
        else:
            result += f"All movies: {', '.join([mve.title for mve in self.movies_collection])}"
        return result






