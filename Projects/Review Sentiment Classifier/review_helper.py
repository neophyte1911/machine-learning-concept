from datetime import datetime

class Review:
    def __init__(self, reviewJsonDump):
        self.text = reviewJsonDump.get('reviewText','')
        self.summary = reviewJsonDump.get('summary','')
        self.reviewer = reviewJsonDump.get('reviewerName','')
        self.itemTitle = reviewJsonDump.get('itemName','')
        self.score = reviewJsonDump.get('overall',3)
        self.reviewer = reviewJsonDump.get('reviewerName','')
        self.sentiment = self.getSentiment(self.score)
        self.time = self.formatDatetime(reviewJsonDump.get('unixReviewTime',0))
        self.helpful = self.getHelpful(reviewJsonDump.get('helpful',[0,0]))
        
    def getSentiment(self, score):
        if score <= 2:
            return "NEGATIVE"
        elif score == 3:
            return "NEUTRAL"
        else:
            return "POSITIVE"
    
    def formatDatetime(self, timestamp):
        return datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d')
    
    def getHelpful(self, helpRating):
        if helpRating[1]!=0:
            return helpRating[0]/helpRating[1]
        else:
            return 0.0