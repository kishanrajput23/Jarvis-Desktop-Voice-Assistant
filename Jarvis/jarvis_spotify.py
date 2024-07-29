import spotipy
import webbrowser


def play_song(track):
    #user will have to input their own details here
    username = ''
    client_Id = ''
    secret = ''
    redirect = "http://google.com/callback/"

    #login to spotify using provided details
    oauth = spotipy.SpotifyOAuth(client_Id, secret, redirect)
    token_dict = oauth.get_access_token()
    token  = token_dict['access_token']
    spotify = spotipy.Spotify(auth=token)
    user_name = spotify.current_user()

    #find top result from search request and play song
    #song = "DNA"
    results = spotify.search(track, 1, 0, 'track')
    song_dict = results['tracks']
    song_items = song_dict['items']
    song = song_items[0]['external_urls']['spotify']
    webbrowser.open(song)
