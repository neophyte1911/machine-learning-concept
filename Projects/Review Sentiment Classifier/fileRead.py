import json
import random
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import review_helper

class FileLoader():
    def __init__(self, filePaths):
        self.filePaths = filePaths
        self.reviews, self.reviewCount = self.getReviews()

    def getReviews(self):
        '''
        
        returns 
            list -- reviews
            int  -- length

        '''
        reviews = []
        count = 0

        #########################################################################
        for file in self.filePaths:
            print(f"File {file} will be read")
            
            with open(file) as f:
                lines = f.readlines()
                for i in tqdm(range(len(lines))):
                    reviewJsonDump = json.loads(lines[i])

                    reviews.append(review_helper.Review(reviewJsonDump))
                    count+=1
                    
        #########################################################################

        print("All files have been read and reviews have been loaded.\n\n")
        return reviews, count
    
    def printReview(self, idx):
        '''
        
        Print a review with given index
        
        '''
        if idx > self.reviewCount:
            print("Index out of bound")
            return
        print("---------")
        print(f"Summary:\n{self.reviews[idx].summary}")
        print("---------")
        print(f"Text:\n{self.reviews[idx].text}")
        print("---------")
        print(f"Score:{self.reviews[idx].score}")
        print("---------")
        print(f"Sentiment:{self.reviews[idx].sentiment}")
        print("---------")
        print(f"Reviewer:{self.reviews[idx].reviewer}")
        print("---------")
        print(f"Time:{self.reviews[idx].time}")
        print("---------")
        print(f"Helpful:{self.reviews[idx].helpful}")
        print("---------")

        return
        
    def evenlyDistribute(self, reviewList):
        '''
        
        Distributes a review list evenly for positive and negative sentiment

        Returns: list
        '''
        negative = list(filter(lambda x: x.sentiment == "NEGATIVE", reviewList))
        positive = list(filter(lambda x: x.sentiment == "POSITIVE", reviewList))

        if len(negative)<len(positive):
            positive_shrunk = positive[:len(negative)]
            DistributedReviews = negative + positive_shrunk
        else:
            negative_shrunk = negative[:len(positive)]
            DistributedReviews = positive + negative_shrunk

        random.shuffle(DistributedReviews)

        return DistributedReviews

    def getRandomReview(self, sentimentToFind=None, printKey=False):
        if sentimentToFind==None:
            print("Picking random sentiment")
            idx = random.randint(0,self.reviewCount)
            if printKey:
                self.printReview(idx)
            return self.reviews[idx]
        
        print(f"Picking {sentimentToFind} for random review")
        sentimentIndexList = [i for i in range(self.reviewCount) if self.reviews[i].sentiment == sentimentToFind]
        
        randomIndex = random.choice(sentimentIndexList)
        
        if printKey:
                self.printReview(randomIndex)
        return self.reviews[randomIndex]
    
    def trainTestSplit(self, testSize = 0.3, randomState=42):
        training, test = train_test_split(self.reviews, test_size=testSize, random_state=randomState)

        trainEqualDistributedData = self.evenlyDistribute(training)
        testEqualDistributedData = self.evenlyDistribute(test)
        
        return trainEqualDistributedData, testEqualDistributedData

