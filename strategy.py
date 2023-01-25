from abc import ABC, abstractmethod

ALLOWED_EXTENSIONS = ["html", 'csv', 'mp3', 'mp4', 'txt']


class AbstractRenderer(ABC):
    @abstractmethod
    def render(self):
        pass


class HTMLRenderer(AbstractRenderer):
    def render(self):
        print("Render using HTMLRenderer")


class MP3Renderer(AbstractRenderer):
    def render(self):
        print("Render using MP3 streamer")


class MP4Renderer(AbstractRenderer):
    def render(self):
        print("Render using MP4 streamer")


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    @property
    def extension(self):
        return self.filename.split('.')[-1]

    @classmethod
    def create(cls, filename):
        if filename.split('.')[-1] not in ALLOWED_EXTENSIONS:
            print("File extension not allowed")
        return cls(filename)

    def render(self):
        handler_dict = {
            "html": HTMLRenderer,
            'mp3': MP3Renderer,
            'mp4': MP4Renderer
        }
        handler = handler_dict[self.extension]
        return handler().render()


if __name__ == "__main__":
    f1 = FileHandler.create('document.pdf')
    f2 = FileHandler.create('document.html')
    f3 = FileHandler.create('music.mp3')
    f4 = FileHandler.create('video.mp4')

    files_list = [f2, f3, f4]

    for file_name in files_list:
        file_name.render()
