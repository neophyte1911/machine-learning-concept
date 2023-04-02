from datetime import datetime

class Review:
    def __init__(self, reviewJsonDump):
        self.text = self.reviewJsonDump.get('reviewText','')
        self.summary = self.reviewJsonDump.get('summary','')
        self.reviewer = self.reviewJsonDump.get('reviewerName','')
        self.itemTitle = self.reviewJsonDump.get('itemName','')
        self.score = self.reviewJsonDump.get('overall',3)
        self.reviewer = self.reviewJsonDump.get('reviewerName','')
        self.sentiment = self.getSentiment(self.score)
        self.time = self.formatDatetime(self.reviewJsonDump.get('unixReviewTime',0))
        self.helpful = self.getHelpful(self.reviewJsonDump.get('helpful',[0,0]))
        
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