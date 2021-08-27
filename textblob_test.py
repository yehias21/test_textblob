import test_twitter as twitter
from textblob import TextBlob
import rotten_tomatto as movies
if __name__ == "__main__":
    # accuracy metric is calculated using (TP+TN)/PP method
    print(TextBlob("This marvelous short will hit home with everyone who, as a child, specifically asked for something because it was hip or cool, only to be given something that would mark you for life with your peers and were told by your Mom or Dad (or both) that it didn't matter, as you earnestly began considering enlisting in a Witness Protection Program in order to avoid ridicule. For those U.S. residents who don't get the horror because you don't follow hockey, it's like a Dallas Cowboy fan getting a Washington Redskins jersey or a Yankees fan getting a Red Sox jersey. It isn't pretty. For our European friends, think of two great rival football (soccer to us) clubs and imagine a fan of one getting a jersey from the other. Ouch!!! NFB of C outdid themselves here!<br /><br />Une hommage du Maurice Rocket Richard, merci, M. Richard.").sentiment)
    print("Acuracy for twitter dataset: "+twitter())
    print("Acuracy for rotten_tomato dataset: "+movies())