import media, fresh_tomatoes

wall_e = media.Movie("WALL-E", 2008,
                    "A small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind",
                    "G", "Action & Adventure, Animation, Science Fiction & Fantasy",
                    "Jim Reardon, Andrew Stanton", "Andrew Stanton",
                    "Nov 18, 2008", 97,
                    "http://www.pixartalk.com/wp-content/uploads/2009/06/wallefinal.jpg",
                    "https://www.youtube.com/watch?v=alIq_wG9FNk")

logan = media.Movie("Logan", 2017,
                    "Logan's attempts to hide from the world, and his legacy, are upended when a young mutant arrives, pursued by dark forces",
                    "R","Action & Adventure, Drama, Science Fiction & Fantasy",
                    "James Mangold, Scott Frank, Michael Green", "James Mangold",
                    "May 23, 2017", 135,
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

conjuring = media.Movie("The Conjuring", 2013,
                        "A real-life story of the Warrens come to the assistance of the Perron family who are experiencing increasingly disturbing events in their farmhouse.",
                        "R","Horror, Mystery & Suspense",
                        "Carey Hayes, Chad Hayes", "James Wan",
                        "Oct 22, 2013", 112,
                        "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg",
                        "https://www.youtube.com/watch?v=k10ETZ41q5o")

days_of_summer = media.Movie("500 Days of Summer", 2009,
                            "A man who falls head over heels for a woman who doesn't believe in love",
                            "PG-13", "Comedy, Drama, Romance",
                            "Scott Neustadter, Michael H. Weber", "Marc Webb",
                            "Dec 22, 2009", 95,
                            "https://upload.wikimedia.org/wikipedia/en/d/d1/Five_hundred_days_of_summer.jpg",
                            "https://www.youtube.com/watch?v=PsD0NpFSADM")

despicable_me = media.Movie("Despicable Me", 2010,
                            "A supervillian, who adopts three girls, plans to shrink and steal moon",
                            "PG", "Animation, Comedy, Kids & Family",
                            " Ken Daurio, Cinco Paul", "Pierre Coffin, Chris Renaud",
                            "Dec 14, 2010", 95,
                            "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Despicable_Me_Poster.jpg/220px-Despicable_Me_Poster.jpg",
                            "https://www.youtube.com/watch?v=j2bAEnBQWvM")

identity=media.Movie("Identity", 2003,
                    "10 strangers arrive at an isolated location and are mysteriously killed off one by one.",
                    "R","Horror, Mystery & Suspense",
                    "Michael Cooney", "James Mangold", "Apr 25, 2003", 90,
                    "https://upload.wikimedia.org/wikipedia/en/thumb/4/44/Identity_poster.jpg/220px-Identity_poster.jpg",
                    "https://www.youtube.com/watch?v=S8fjyxM7DgU")

movie=[wall_e, logan, conjuring, days_of_summer, despicable_me, identity]
# Open movie pages
fresh_tomatoes.open_movies_page(movie);
