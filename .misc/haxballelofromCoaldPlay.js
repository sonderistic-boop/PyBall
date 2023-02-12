//credit to CoaldPlay for the elo system



//Znaleziono nowego gracza! "localStorage.setItem(authArray[player.id][0], JSON.stringify(stats))" użyto.

  if (eloteamblue > eloteamred){
        ratdiff = ((eloteamblue/4) - (eloteamred/4))/400;
    }
    if (eloteamred > eloteamblue){
        ratdiff = ((eloteamred/4) - (eloteamblue/4))/400
    }
    if (eloteamred == eloteamblue){
        ratdiff = 0;
    }
    var expectedscore = (1/(1+(10**ratdiff)));
    var ratingchange = (kfactor*(1-(expectedscore*1))).toFixed(0); 
    //stats.rating = (((stats.opponentrating*1) + (400*((stats.wins*1) - loses)))/(stats.games*1)).toFixed(0);
    if (lastWinner == teamStats){
        stats.rating += (ratingchange*1)
        var stareelo = stats.rating - (ratingchange*1)
        room.sendAnnouncement(
            `Twoje nowe ELO: ${stareelo}+${ratingchange}=${stats.rating}.`,
            player.id,
            goldenColor,
            "bold",
        );
    }
    if (lastWinner != teamStats){
        stats.rating += -(ratingchange*1)
        var stareelo = stats.rating + (ratingchange*1)
        room.sendAnnouncement(
            `Twoje nowe ELO: ${stareelo}-${ratingchange}=${stats.rating}.`,
            player.id,
            goldenColor,
            "bold",
        );
    }
