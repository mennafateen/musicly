# coding=utf-8
import sqlite3
sql = sqlite3.connect('music.db')
cur = sql.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS playlist (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
description TEXT
)''')
sql.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS band (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT
)''')
sql.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS artist (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
date_of_birth DATE,
band INT,
FOREIGN KEY(band) REFERENCES band(id)
)''')
sql.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS album (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
band INT,
artist INT,
num_of_songs INT,
FOREIGN KEY(band) REFERENCES band(id),
FOREIGN KEY(artist) REFERENCES artist(id)    
)''')
sql.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS song (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
release_date DATE,
length TIME,
genre TEXT,
album INT,
band INT,
lyrics TEXT,
path TEXT,
FOREIGN KEY(album) REFERENCES album(id),
FOREIGN KEY(band) REFERENCES band(id)
)''')
sql.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS artist_song (
artist INT,
song INT,
FOREIGN KEY(artist) REFERENCES artist(id),
FOREIGN KEY(song) REFERENCES song(id)
)''')
cur.execute('''CREATE TABLE IF NOT EXISTS song_playlist (
song INT,
playlist INT,
FOREIGN KEY(song) REFERENCES song(id),
FOREIGN KEY(playlist) REFERENCES playlist(id)
)''')


cur.execute('INSERT INTO band(name) \
VALUES ("Native Deen")')
sql.commit()
cur.execute('INSERT INTO band(name) \
VALUES ("Raihan")')
sql.commit()

'''
res = cur.execute("SELECT * FROM band")
for row in res:
    print "ID: ", row[0]
    print "Name: ", row[1]
'''

cur.execute('INSERT INTO artist(name, date_of_birth, band) \
VALUES ("Joshua Salaam", "1994:02:01", 1)')
cur.execute('INSERT INTO artist(name, date_of_birth, band) \
VALUES ("Naeem Mohammed", "1993:08:29", 1)')
cur.execute('INSERT INTO artist(name, date_of_birth, band) \
VALUES ("AbdulMalik Ahmed", "1993:09:13", 1)')

cur.execute('INSERT INTO artist(name, date_of_birth, band) \
VALUES ("Che Amran Idris", "1978:01:09", 2)')
cur.execute('INSERT INTO artist(name, date_of_birth, band) \
VALUES ("Abu Bakar Yatim", "1973:08:22", 2)')
cur.execute('INSERT INTO artist(name, date_of_birth, band) \
VALUES ("Amran Ibrahim", "1980:01:28", 2)')


cur.execute('INSERT INTO artist(name, date_of_birth) \
VALUES ("Harris J.", "1997:05:02")')
cur.execute('INSERT INTO artist(name, date_of_birth) \
VALUES ("Raef", "1982:08:08")')
cur.execute('INSERT INTO artist(name, date_of_birth) \
VALUES ("Maher Zain", "1981:07:16")')
cur.execute('INSERT INTO artist(name, date_of_birth) \
VALUES ("Sami Yusuf", "1976:03:15")')

'''
res = cur.execute("SELECT * FROM artist")
for row in res:
    print "ID: ", row[0]
    print "Name: ", row[1]
    print "DOB: ", row[2]
    print "band: ", row[3]
'''
cur.execute('INSERT INTO album(name, band, num_of_songs) \
VALUES ("Not Afraid To Stand Alone", 1, 16)')
cur.execute('INSERT INTO album(name, band, num_of_songs) \
VALUES ("Syukur", 2, 11)')

cur.execute('INSERT INTO album(name, artist, num_of_songs) \
VALUES ("Thank You Allah", 9, 14)')
cur.execute('INSERT INTO album(name, artist, num_of_songs) \
VALUES ("Salam", 7, 12)')
cur.execute('INSERT INTO album(name, artist, num_of_songs) \
VALUES ("The Path", 8, 16)')
cur.execute('INSERT INTO album(name, artist, num_of_songs) \
VALUES ("Al-Mualim", 10, 10)')



# songs
cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, band, path) \
VALUES ("Stand Alone", "2011:11:18", "I am not afraid to stand alone.\
I am not afraid to stand alone. If Allah is by my side\
I am not afraid to stand alone. Everything will be alright\
I am not afraid to stand alone. Gonna keep my head up high\
Single mother raising her children\
Now she’s a Muslim\
Started praying and wearing a headscarf\
Was a healing for her heart\
Struggling with no one to lean on\
But with prayer she would be strong\
Got a job but then she was laid off\
Got a better education and it paid off\
Got a call for a job that she dreamed of\
Close by, great pay -she was in love – they said…\
They brought her in, said she’s the number one pick\
You got the job, but you gotta lose the outfit”\
It’s a tough position that they put me in\
Cause Ive been struggling with my two children\
But I’ll continue looking for a job again\
My faith in my religion now will never bend\
Chorus\
Peer pressure, they were insisting\
And I was resisting\
Some days I felt I would give in\
Just wanted to fit in\
I know when I’m praying and fasting’\
They be teasing and laughing\
So I called to my Lord for the power\
For the strength every day, every hour…\
Then one day there’s a new Muslim teacher\
Single mom and the people respect her\
Just seeing her strength I get stronger\
They can break my will no longer\
You don’t see me sweating when they’re jokes’re cracking\
Never see me cussing’ with my pants saggin’\
I aint never running yo I’m still standing\
I ride with Allah to the very end\
Chorus\
I am not afraid to stand alone…\
Now, I’m a tough one, who can bear their blows\
The rest play dumb, they don’t dare say no\
Scared of being shunned, but its clear they know\
I aint never gonna run, I aint scared no more.\
Man, these sisters be resolute\
Never stressed when the rest say they wasn’t cute\
And the get the respect of the other youth\
Come best with the dress yo and that’s the truth\
These sisters are strong gonna hand it down\
So me I’m a brotha gotta stand my ground\
I aint gonna shudder, when the gangs around\
Peer pressure whatever, its my planet now\
Others may fall, I’mma hold my own\
With Allah’s help I’ll be strong as stone\
And I’mma be brave and let Al Islam be shown\
Cause you I know I not afraid to stand alone", "00:04:06", "Urban", 1, 1, "not_afraid.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, band, path) \
VALUES ("Talaa Badru", "2011:11:18", "He eyes slowly rising \
Sunrise warms the horizon \n\
Sand dunes form in the distant\n\
He’s up and out in an instant\n\
The crowd there, all were waiting\
Watching and, anticipating\
A man appears from afar\
Could it be the one sent by Allah\
He shouts “Here comes the prophet!”\
His face is a light that drives out the darkness\
Words are alive – his message is living\
Joy everywhere, our voices are singing\
Chorus", "00:03:18", "Pop", 1, 1, "talaa_badru.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, band, path) \
VALUES ("25 Rasul", "2015:10:23", "Assolaatu alannabi \
Wassalaamu alarrosul \
Wal ambiya il mursaliin\
Kulluhum mukromun\
Selawat keatas nabi\
Sejahtera keatas rasul\
Nabi nabi yang diutuskan\ Mereka semua adalah mulia\
Adam, \
Idris, \
Nuh, \
Hud, \
Soleh \
Ibrahim, \
Luth, \
Ismail \
Ishak, \
Yaqub, \
Yusuf, \
Ayub, \
Syuaib\
Musa, \
Harun, \
Zulkifli\
Daud, \
Sulaiman\
Ilyas\
Ilyasa,\
Yunus, \
Zakaria,\
Yahya,\
Isa,\
Wal akhiru khotimul ambiyaa\
Muhammad al musthofa\
Assolaatu alannabi \
Wassalaamu alarrosul \
Wal ambiya il mursaliin\
Kulluhum mukromun\
Selawat keatas nabi \
Sejahtera keatas rasul \
Nabi - nabi yang diutuskan \
Mereka semua adalah mulia\
Terangkan hati kami ya Allah\
seperti hati rasulMU ya Allah", "00:05:12", "Arabic",2,2, "25_rasul.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, path) \
VALUES ("Salam Alikum", "2011:11:18", "You can try and turn off the sun\
Im still going to shine away, yeah\
And tell everyone\
We’re having some fun today\
We can go wherever you want to\
And do whatever you like\
Let’s just have a real good time\
Assalamu Alaikum, Alaikum yeah!\
Assalamu Alaikum, Alaikum yeah!\
Assalamu Alaikum, Alaikum yeah!\
Assalamu Alaikum, Alaikum yeah!\
I just want to spread love and peace\
And all of my happiness, yeah\
To everyone that I meet\
Cause Im feeling spectacular\
I love it when we love one another\
Give thanks everyday\
For this life, living with a smile on our face\
Assalamu Alaikum, Alaikum yeah!\
Assalamu Alaikum, Alaikum yeah!\
Assalamu Alaikum, Alaikum yeah!\
Assalamu Alaikum, Alaikum yeah!\
Spread peace on the earth\
Cherish the love that is around us\
Spread peace on the earth\
Treasure the love, let it surround us\
Always be kind, always remind one another", "00:03:18", "Pop", 4, "salam.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album,  path) \
VALUES ("Rasool Allah", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", 4,  "rasool_allah.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, path) \
VALUES ("I Promise", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", 4, "i_promise.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, path) \
VALUES ("The One", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", 4, "the_one.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, path) \
VALUES ("Let Me Breathe", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", 4, "let_me_breathe.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, path) \
VALUES ("You Are My Life", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", 4, "you_are_my_life.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album,  path) \
VALUES ("Baraka Allah", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", 3, "barakallahh.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, path) \
VALUES ("Price Tag", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", 5, "price_tag.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, path) \
VALUES ("Subhanallah", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop",3, "subhanallah.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, path) \
VALUES ("The Chosen One", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", 3, "the_chosen_one.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, path) \
VALUES ("Ya Nabi", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", 3, "ya_nabi.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, path) \
VALUES ("Allahu", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", 6, "allahu.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, path) \
VALUES ("Hasbi Rabbi", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", 6, "hasbi_rabbi.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, path) \
VALUES ("Ya Mostafa", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", 6, "ya_mostafa.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, album, path) \
VALUES ("Ya Rasulallah", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", 6, "ya_rasulallah.wav")')

cur.execute('INSERT INTO song(name, release_date, lyrics, length, genre, path) \
VALUES ("So Real", "2011:11:18", "Oh, you came into this life\
Brought up as an orphan child\
Through a time of deep despair, O Muhammad!\
Your days at work began\
As a fair and honest man\
You showed just how much you cared\
And one night in that cave\
When the Archangel came\
And your life in this world\
Would never be the same\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Eyes that could light up any soul\
You became the Chosen One\
To proclaim the word of God, O Muhammad!\
In the brightness of the sun\
Or the stillness of the night\
You would never ever stop\
Being kind, giving hope\
And serenity and love\
To a divided world\
That didnt have enough\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
I’ll never leave your way\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
I really love you\
Rasool’Allah habib’Allah\
Peace be upon you\
Rasool’Allah habib’Allah\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
Rasool’Allah habib’Allah\
Your light is always showing me the way\
Rasool’Allah habib’Allah\
I’m longing for the day I see your face\
You brighten up my day\
And in my heart you’ll stay\
With every breath I take\
O Muhammad I will never leave your way", "00:03:18", "Pop", "so_real.wav")')

cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (7,4)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (7,5)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (7,6)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (7,7)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (7,8)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (7,9)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (9,10)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (8,11)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (9,12)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (9,13)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (9,14)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (10,15)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (10,16)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (10,17)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (10,18)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (8,19)')
cur.execute('INSERT INTO artist_song(artist, song)\
VALUES (9,19)')

cur.execute('INSERT INTO playlist(name, description) \
VALUES ("Just For Fun", "This is mainly a test playlist")')

cur.execute('INSERT INTO song_playlist(song, playlist) \
VALUES(1,1)')
cur.execute('INSERT INTO song_playlist(song, playlist) \
VALUES(5,1)')
cur.execute('INSERT INTO song_playlist(song, playlist) \
VALUES(6,1)')
cur.execute('INSERT INTO song_playlist(song, playlist) \
VALUES(9,1)')
cur.execute('INSERT INTO song_playlist(song, playlist) \
VALUES(10,1)')

sql.commit()
res = cur.execute("SELECT * FROM artist")
for row in res:
    print "ID: ", row[0]
    print "Name: ", row[1]
    print "DOB: ", row[2]
    print "band: ", row[3]
res = cur.execute("SELECT * FROM band")
for row in res:
    print "ID:", row[0]
    print "Name: ", row[1]


sql.commit()
sql.close()



