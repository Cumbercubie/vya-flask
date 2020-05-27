import praw
from validator_collection import validators, checkers
# import pandas as pd
# import datetime as dt
CLIENT_ID = "-wXVoB6KYkwzDA"
CLIENT_SECRET = "i_LBZC-5ce9caaqrcNDBCwHnKbw"
# dict = {
#     "post_author": "",
#     "post_content":"",
#     "comments":
#     [
#         {
#             "parents_Id":"",
#             "user": "u/hello",
#             "comment": "",
#             "upvotes":"",
#             "replies":
#             [
#                 {
#                     "parents_Id":"",
#                     "user": "u/hello",
#                     "comment": "",
#                     "upvotes":""
#                 }
#             ]
#         }
#     ]
# }
list = []

# This is pure ugly codes, doesn't cover all test cases.
def splitUrl(url):
    if len(str(url))==6:
        return url
    elif len(str(url)) > 6 and checkers.is_url(url):
        UrlAsList = str(url).split(sep="/")
        if len(UrlAsList)<6:
            return UrlAsList[3]
        else: 
            return UrlAsList[6]
    return 
    

class RedditExtractor:
    def __init__(self):
        self.reddit = praw.Reddit(user_agent="VYA_Extractor",client_id=CLIENT_ID,client_secret=CLIENT_SECRET)

   
    def getComments(self,url):
        cmts={}
        sub_id = splitUrl(url)
        submission = self.reddit.submission(id=sub_id)
        submission.comments.replace_more(limit=None)
        for top_level_comment in submission.comments:
            print(top_level_comment)
            cmts['author']= str(top_level_comment.author)
            cmts['body']= str(top_level_comment.body).strip()
            cmts['upvotes'] = str(top_level_comment.score)
        return cmts
    
    def getAllComments(self,url,limit):
        ListAllComments=[]
        count = limit # for the sake of being afraid limit would gone wrong
        sub_id = splitUrl(url)
        submission = self.reddit.submission(id=sub_id)
        submission.comments.replace_more(limit=5)
        # listCmts = submission.comments
        for comment in submission.comments[:count]:
            ListAllComments.append(getCommentReplies(comment,limit))
        return ListAllComments


def getCommentReplies(cmt,limit):
        cmts = {}
        if limit == 0:
            return cmts
        cmts["author"] = str(cmt.author)
        cmts["body"] = str(cmt.body).strip()
        cmts["upvotes"] = str(cmt.score)
        if len(cmt.replies)!=0:
            cmts["replies"] = []
            for reply in cmt.replies:
                cmts["replies"].append(getCommentReplies(reply,limit-1))
        return cmts
    
# def main():
#     red = RedditExtractor()
#     print(red.getAllComments('3g1jfi'))
# if __name__ == '__main__':
#     main()