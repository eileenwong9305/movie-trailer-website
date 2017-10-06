import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href="https://fonts.googleapis.com/css?family=Fugaz+One" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        .page-title{
            color: white;
            font-size: 24px;
            font-family: 'Fugaz One', cursive;
            text-shadow: 2px 2px 4px #424242;
        }
        .poster-tile{
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .poster-tile:hover {
            background-color: #eee;
            opacity: 0.7;
            transition: 0.3s;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

        /* View Info and Watch Trailer Button */
        .btn-md {
            padding: 5px 10px;
        }

        /* The Modal Information (title) */
        .modal-movie-title {
            font-weight: bold;
        }

        /* The Modal Image (background) */
        .modalImg {
            display: none; /* Hidden by default */
            position: fixed; /* Stay in place */
            padding-top: 40px; /* Location of the box */
            width: 100%; /* Full width */
            height: 100%; /* Full height */
            overflow: auto; /* Enable scroll if needed */
            background-color: rgb(0,0,0); /* Fallback color */
            background-color: rgba(0,0,0,0.9); /* Black w/ opacity */
        }

        /* Modal Image Content (image) */
        .content-center {
            display: block;
            margin: auto;
            width: 60%;
        }

        /* The Modal Image Close Button */
        .close-icon {
            color: #f1f1f1;
            font-size: 40px;
            font-weight: bold;
            transition: 0.3s;
        }
        .close-icon:hover,
        .close-icon:focus {
            color: #bbb;
            text-decoration: none;
            cursor: pointer;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-trailer', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
            $('.movie-tile').hide().first().show("fast", function showNext() {
                $(this).next("div").show("fast", showNext);
            });
        });

        // Insert movie information into more info modal content
        $(document).ready(function(){
            $('#info').on('show.bs.modal',function (event) {
                var button = $(event.relatedTarget); // Button that triggered the modal
                var modal = $(this);
                // Extract and insert movie information into modal body
                modal.find('.modal-movie-title').text( button.data('title'));
                modal.find('.mod-movie-storyline').text(button.data('storyline'));
                modal.find('.mod-movie-rating').text(button.data('rating'));
                modal.find('.mod-movie-genre').text(button.data('genre'));
                modal.find('.mod-movie-director').text(button.data('director'));
                modal.find('.mod-movie-screenwriter').text(button.data('screenwriter'));
                modal.find('.mod-movie-date').text(button.data('release-date'));
                modal.find('.mod-movie-runtime').text(button.data('runtime')+" min");
                modal.find('.mod-movie-poster').attr('src',button.data('poster'));
            });
        });

        // Enlarge poster image when clicked
        $(document).ready(function(){
            $('#myModalImage').on('show.bs.modal',function (event) {
                var imgClick = $(event.relatedTarget);
                $(this).find('.modal-content-image').attr('src',imgClick.data('image-url'));
            });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!--More Movie Information Modal -->
    <div id="info" class="modal fade" role="dialog">
      <div class="modal-dialog">
        <!-- Modal content-->
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">&times;</button>
            <h4 class="modal-title modal-movie-title">movie title</h4>
          </div>
          <div class="modal-body">
            <div class="container-fluid">
              <div class="row">
                <div class="col-sm-5">
                  <img src="poster_image_url.jpg" width="220" height="342" class="mod-movie-poster">
                </div>
                <div class="col-sm-7">
                  <div>
                    <p class="mod-movie-storyline">movie_storyline</p>
                  </div>
                  <div class="container-fluid">
                    <dl class="row">
                      <dt class="col-sm-5 text-right">Rating:</dt>
                      <dd class="mod-movie-rating col-sm-7"> </dd>
                      <dt class="col-sm-5 text-right">Genre:</dt>
                      <dd class="mod-movie-genre col-sm-7"> </dd>
                      <dt class="col-sm-5 text-right">Director:</dt>
                      <dd class="mod-movie-director col-sm-7"> </dd>
                      <dt class="col-sm-5 text-right">Screenwriter:</dt>
                      <dd class="mod-movie-screenwriter col-sm-7"> </dd>
                      <dt class="col-sm-5 text-right">Release Date:</dt>
                      <dd class="mod-movie-date col-sm-7"> </dd>
                      <dt class="col-sm-5 text-right">Runtime:</dt>
                      <dd class="mod-movie-runtime col-sm-7"> </dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Enlarge Image Modal -->
    <div class="modal fade modalImg" id="myModalImage" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <button type="button" class="close close-icon" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <img src="" class="modal-content-image content-center" >
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-light navbar-fixed-top" role="navigation" style="background-color: #203941;">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand page-title" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" >
  <img src="{poster_image_url}" width="220" height="342" class="poster-tile" alt="{movie_title}" title="{movie_title}" data-image-url="{poster_image_url}"
    data-toggle="modal" data-target="#myModalImage">
  <h3>{movie_title} ({movie_year})</h3>
  <div class = "button-row" >
    <button type="button" class="btn btn-primary btn-md movie-trailer" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    Watch Trailer
    </button>
    <button type="button" class="btn btn-info btn-md movie-info" data-toggle="modal" data-target="#info" data-title="{movie_title}"
      data-storyline="{movie_storyline}" data-rating="{movie_rating}" data-genre="{movie_genre}" data-runtime="{movie_runtime}"
      data-director="{movie_director}" data-screenwriter="{movie_screenwriter}" data-release-date="{movie_release_date}" data-poster="{poster_image_url}">
    More Info
    </button>
  </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            poster_image_url=movie.poster_image_url,
            movie_title=movie.title,
            movie_year=movie.year,
            movie_storyline=movie.storyline,
            movie_rating=movie.rating,
            movie_genre=movie.genre,
            movie_director=movie.director,
            movie_screenwriter=movie.screenwriter,
            movie_release_date=movie.release_date,
            movie_runtime=movie.runtime,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('index.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
