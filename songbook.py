from pdfrw import PdfReader, PdfWriter
import requests
import unicodedata

def download(path):
    """
    Parses a input file and downloads PDF the source file is pointing to.
    Args:
        path (str): Path to the text file (see README) containing the list of songs.

    Yields:
        Bytestream of the PDF of the single song.

    """
    with open(path, mode="r", encoding="utf-8") as file:
        for line in file.read().splitlines():
            line = line.split("#")[0]
            if not line:
                continue
            if line[0] != "\t":
                interpret = urlize(line)
                continue
            else:
                song = urlize(line[1:])
                shift = 0
                if "/" in song:
                    song, shift, *_ = song.split("/")
            url = f"https://pisnicky-akordy.cz/{interpret}/{song}?format=pdf&posun={shift}"            
            try:
                r = requests.get(url)
                if "pdf" not in r.headers.get("content-type"):
                    raise Error
                yield r.content
                print(f"{interpret}/{song}/{shift} ok")
            except:
                print(f"{interpret}/{song}/{shift} failed")
                            

def merge(pdfs):
    """
    Merges PDF and saves the result to disk (songbook.pdf).

    Each pdf is saved temporarily to disk (temp.pdf).

    Args:
        pdfs (Iterable): Bytestreams containing pdfs.


    """
    writer = PdfWriter()
    for pdf in pdfs:
        with open("temp.pdf", "wb") as f:
            f.write(pdf)
        writer.addpages(PdfReader("temp.pdf").pages)
    writer.write("songbook.pdf")

def urlize(text):
    """
    Converts a human readable name of an artist or a song to its url form.

    That is, all accents as well as commas are removed, words are converted
    to lowercase and spaces are replaced with hyphens.

    Args:
        text (str): Name to be converted.

    Returns:
        str: Url form of text.

    """
    text = str(unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode("utf-8"))
    text = text.replace(" ", "-").replace(",", "")
    return text.lower()

#Runs the process of downloading and merging the songs.
merge(download("songs.txt"))
