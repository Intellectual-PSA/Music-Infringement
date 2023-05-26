class MusicPiece:
    def __init__(self, title, creation_date):
        self.title = title
        self.creation_date = creation_date
        self.alleged_infringements = []

    def report_infringement(self, infringer_name, date, details):
        self.alleged_infringements.append({
            'infringer_name': infringer_name,
            'date': date,
            'details': details,
        })

class SongWriter:
    def __init__(self, name):
        self.name = name
        self.works = []

    def create_piece(self, title, creation_date):
        piece = MusicPiece(title, creation_date)
        self.works.append(piece)
        return piece

    def list_works(self):
        for work in self.works:
            print(f'Title: {work.title}, Creation Date: {work.creation_date}')
            if work.alleged_infringements:
                print('  Reported Infringements:')
                for infringement in work.alleged_infringements:
                    print(f'    Infringer Name: {infringement["infringer_name"]}, Date: {infringement["date"]}, Details: {infringement["details"]}')

# Sample usage
if __name__ == "__main__":
    songwriter = SongWriter("John Doe")

    song1 = songwriter.create_piece("Song Title 1", "2023-01-01")
    song1.report_infringement("Singer A", "2023-02-01", "Singer A performed this song without permission")

    song2 = songwriter.create_piece("Song Title 2", "2023-03-01")
    song2.report_infringement("Singer B", "2023-04-01", "Singer B claimed this song as their own")

    songwriter.list_works()
