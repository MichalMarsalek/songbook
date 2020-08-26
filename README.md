# pisnicky-akordy.cz songbook
Generates a PDF songbook from pisnicky-akordy.cz
Targeting czech users pisnicky-akordy.cz catalouges mainly songs (with chords) in czech (but some in english or slovak too).
There's a feature on pisnicky-akordy.cz that lets users print a single song to a PDF file, perhaps with a set transposition of chords.  
This script parses a human readable list of songs like

```
#České
Chinaski
	Tabáček
	Klára/3

#Anglické
OneRepublic
	Counting stars/1
Green Day
	Boulevard of broken dreams
```


downloads a PDF for each of the songs and then merges all those PDFs.  
Line comments start with `#` and empty lines are ignored.
Left-flushed text signifies a name of an artist. Such a line is followed by a list of songs by this artist, each on its own line starting with exactly one tabulator.
One can transpose a song by `k` halftones by postfixing the line with `/k`.

**Caution**  
All that the mapping from human names to URLs is doing is stripping any accents or commas, converting to lowercase and replacing spaces with hyphens. Be sure to check that the song is actually on pisnikcy-akordy.cz and that the name of the artist and the song is the same as it is on pisnicky-akordy.cz.  
The main drawback of this method is that the PDFs are huge. To mitigate this I recommend using [this service](https://www.pdf2go.com/compress-pdf).

##Dependencies
pdfrw