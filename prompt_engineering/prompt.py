from base import get_completion

text = f"""
The 1983 Cricket World Cup marked one of the greatest moments in Indian sports history. \
India entered the tournament as underdogs, with little expectation of winning against dominant \
teams like the West Indies and England. India played in Group B, facing the West Indies, Australia, and Zimbabwe. \
The campaign began with a historic win against the West Indies, where Kapil Dev’s all-round performance shocked the \
cricketing world. Although India lost one match to the West Indies, they won crucial games against Australia \
and Zimbabwe to reach the semifinals. One of the most memorable matches was against Zimbabwe, where Kapil Dev \
scored an unbeaten 175 to rescue India from collapse. In the semifinal, India defeated England convincingly, \
thanks to disciplined bowling and steady batting. The final was played at Lord’s against the mighty West Indies. \
India scored a modest total of 183, with contributions from Kris Srikkanth and Mohinder Amarnath. India’s bowlers, \
led by Kapil Dev, Madan Lal, and Mohinder Amarnath, bowled brilliantly to dismiss the West Indies for 140. \
India won the World Cup by 43 runs, lifting their first-ever World Cup trophy. This victory transformed Indian \
cricket and inspired generations to believe that anything was possible.
"""

prompt = f"""
Use the below text and narrate the same in a kid friendly poem of Dr. Seuss short sentences. Keep to 7-8 likes maximum. text={text}
"""
print(get_completion(prompt=prompt))
