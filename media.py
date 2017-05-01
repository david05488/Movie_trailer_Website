"""This module defines 3 classes (Media, Serie and Documentary) where
Documentary extends of Serie and Serie extends of Media. Each class
has a method (show_details) which returns a defined class info"""


class Media():
    def __init__(self, media_title, media_storyline, poster_image,
                 trailer_youtube):
        self.title = media_title
        self.storyline = media_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_details(self):
        return self.storyline


class Serie(Media):  # Extends of Media
    def __init__(self, media_title, media_storyline, poster_image,
                 trailer_youtube, season, episodes):
        Media.__init__(self, media_title, media_storyline, poster_image,
                       trailer_youtube)
        self.season_number = season
        self.season_episodes_number = episodes

    def show_details(self):  # Override method "show_details" inside
        # Media class
        details = self.title + " " + self.season_number + ": " \
                  + self.season_episodes_number
        return details


class Documentary(Serie):  # Extends of Serie
    def __init__(self, media_title, media_storyline, poster_image,
                 trailer_youtube, season, episodes, available_on):
        Serie.__init__(self, media_title, media_storyline, poster_image,
                       trailer_youtube, season, episodes)
        self.where_to_watch = available_on

    def show_details(self):  # Override method "show_details" inside
        # Serie class
        details = self.title + " " + self.where_to_watch
        return details
