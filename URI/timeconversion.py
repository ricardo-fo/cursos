# https://www.urionlinejudge.com.br/judge/en/problems/view/1019
seconds= int(input())
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print("{}:{}:{}".format(hours,minutes,seconds))