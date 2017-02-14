import webbrowser

class Video():
    '''This calls provides a way to store video related infomation'''
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    '''This class provides a way to store movie related infomation'''

    
    # http://www2.lib.uchicago.edu/keith/courses/python/class/5/
    # https://docs.python.org/2/reference/datamodel.html
    '''
    Attribute   Type    Read/Write  Description
    __dict__    dictionary  R/W The class name space.
    __name__    string  R/O The name of the class.
    __bases__   tuple of classes    R/O The classes from which this class inherits.
    __doc__ string OR None  R/W The class documentation string.
    __module__  string  R/W The name of the module in which this class was defined.

    '''
    # modify module name
    __module__ = 'Hello'
    
    def __init__(self, movie_title, duration, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, duration)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
        

    
