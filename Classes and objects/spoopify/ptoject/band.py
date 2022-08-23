from project.album import Album


class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return f"Album has been published. It cannot be removed."
                self.albums.remove(album)
                return f"Album {album_name} has been removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        x = "\n"
        result = f"Band {self.name}{x}"
        for album in self.albums:
            result += f"{album.details()}{x}"
        return result.strip()
        

