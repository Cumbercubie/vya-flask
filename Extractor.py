import praw
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
class RedditExtractor:
    def __init__(self):
        self.reddit = praw.Reddit(user_agent="VYA_Extractor",client_id=CLIENT_ID,client_secret=CLIENT_SECRET)

    def getComments(self,url):
        cmts={}
        sub_id = "3g1jfi"
        submission = self.reddit.submission(id=sub_id)
        submission.comments.replace_more(limit=5)
        for top_level_comment in submission.comments[2:3]:
            cmts['author']= str(top_level_comment.author)
            cmts['body']= str(top_level_comment.body).strip()
            cmts['upvotes'] = str(top_level_comment.score)
            cmts['replies'] = []
            for second_level_comment in top_level_comment.replies:
                reply = {}
                reply['author']= str(second_level_comment.author)
                reply['body']= str(second_level_comment.body).strip()
                reply['upvotes'] = str(second_level_comment.score)
                cmts['replies'].append(reply)
        return cmts
            
#
# def main():
#     sub_id = "3g1jfi"
#     red = RedditExtractor()
#     red.getComments(sub_id)
# if __name__ == '__main__':
#     main()